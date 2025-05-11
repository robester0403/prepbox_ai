from dotenv import load_dotenv
from typing import Annotated, List, Tuple
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage

from src.prompts.system_message import SYSTEM_MESSAGE
from src.prompts.question_classifer import QUESTION_CLASSIFIER_PROMPT

import json

load_dotenv()  # Load environment variables from .env file

# 1 Define shared state schema with Pydantic
class State(BaseModel):
    # This only accumulates messages like Human Ai and System
    messages: Annotated[List[BaseMessage], add_messages] = Field(default_factory=list)

#--- Refactorable functions ---#
def print_last_message(state: State) -> None:
    """Helper function to print the last message's content"""
    if state.messages:
        print(state.messages[-1].content)

def get_user_message() -> HumanMessage:
    # can't get interrupt to work
    """Get user input and return it as a HumanMessage"""
    return HumanMessage(content=input("You: "))

#--- Conditional Edge Functions ---#
# this needs complete rework and we don't need it right now
# def should_continue(state: State) -> str:
#     """
#     Use AI to determine if the conversation should continue based on the last message
#     """
#     if not state.messages:
#         return "continue"
    
#     # Create a prompt to analyze if the conversation should end
#     analysis_prompt = [
#         SystemMessage(content="""You are a conversation analyzer. Your task is to determine if the user wants to end the conversation.
#         Respond with exactly 'end' if the user clearly wants to end the conversation, or 'continue' if they want to keep talking.
#         Consider:
#         1. Explicit goodbyes (bye, goodbye, see you)
#         2. Implicit goodbyes (gotta go, talk later)
#         3. Conversation-ending statements
#         Only respond with 'end' or 'continue', nothing else."""),
#         *state.messages[-2:]  # Only send the last exchange for context
#     ]
    
#     response = llm.invoke(analysis_prompt)
#     decision = response.content.strip().lower()
    
#     return "end" if decision == "end" else "continue"

#--- Initialize ---#
builder = StateGraph(State)

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.9,
    streaming=False
)

#--- Nodes ---#

def a(state: State) -> State:
    """
    Set up initial system message for the workflow
    """
    if not state.messages:
        return {
            "messages": [
                SystemMessage(content=SYSTEM_MESSAGE),
                SystemMessage(content="Please provide your math questions")
            ]
        }
    return {"messages": []}


def b(state: State) -> State:
    """
    Process user's response and generate conversational reply
    """
    state.messages.append(SystemMessage(content=QUESTION_CLASSIFIER_PROMPT))
    state.messages.append(get_user_message())
    
    response = llm.invoke(state.messages)
    state.messages.append(AIMessage(content=response.content))
    
    return state


SPRINT_1_MATH_TOPIC = """
For the given array of math questions, keep only the questions that are conceptually wrong.
"""

def c(state: State) -> State:
    """
    For Sprint 1 we are mocking the response straight to the planner. Let's just get all the conceptual mistakes and send them to the planner.
    """

    questions = json.loads(state.messages[-1].content)
    conceptual_mistakes = []
    for question in questions:
        if question["mistake_type"] == "conceptual_mistake":
            conceptual_mistakes.append(question)

    stringified_mistakes = json.dumps(conceptual_mistakes)
    state.messages.append(AIMessage(content=stringified_mistakes))

    return state

# need to make this a real prompt
# need to make a mix of real and generated questions
PLANNER_PROMPT = """
You are a planner. You are given a list of questions that the student got conceptually wrong.
Your job is to create a number of lessons of 10 questions each to address the conceptual mistakes by topic.
Each question should be worded differently and if appropriate be worded in a real word problem scenario.
Create 3 arrays of questions and step by step answers that will help the student correct the conceptual mistakes.
Think step by step and reason through the topics and questions to generate new questions that will help the student practice the topics they got wrong.
"""
def d(state: State) -> State:
    """
    Simple 1 step Planner. We need 
    """
    state.messages.append(AIMessage(content=PLANNER_PROMPT))
    response = llm.invoke(state.messages)
    state.messages.append(AIMessage(content=response.content))
    return state

#--- Build the Graph ---#
builder.add_node("a", a)
builder.add_node("b", b)
builder.add_node("c", c)
builder.add_node("d", d)

builder.add_edge(START, "a")
builder.add_edge("a", "b")
builder.add_edge("b", "c")
builder.add_edge("c", "d")
# builder.add_conditional_edges(
#     "b",
#     should_continue,
#     {
#         "continue": "b",
#         "end": "c"
#     }
# )
builder.add_edge("d", END)

graph = builder.compile()

#--- Run in Terminal ---#
def main():
    initial_state = {"messages": []}
    previous_messages = set()

    for chunk in graph.stream(
        initial_state,
        stream_mode="updates"
    ):
        for node_key, node_data in chunk.items():
            if isinstance(node_data, dict) and "messages" in node_data:
                for message in node_data["messages"]:
                    # Create a unique identifier for the message
                    message_id = f"{message.type}:{message.content}"
                    # Only print if we haven't seen this message before
                    if message_id not in previous_messages:
                        print(message.content)
                        previous_messages.add(message_id)

if __name__ == "__main__":
    main()
