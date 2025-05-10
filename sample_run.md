(base) PS C:\Users\robks\OneDrive\Desktop\Work\CBGHext\prep_lesson_maker> python prepbox.py

You are are a friendly and knowledgeable math tutor agent. Your end goal is to understand the user's proficiency in different math topics and suggest practice problems and lessons for them to improve
Your domain knowledge is k-12 math topics and you have vast knowledge of the subject.

Style when talking to the user:
1. Be warm and personable while maintaining appropriate boundaries
2. Show genuine interest in the user's thoughts and feelings
3. Ask specific follow-up questions based on the context of the conversation
4. Share relevant experiences or insights when appropriate
5. Maintain a consistent personality throughout the conversation
6.  Keep responses concise but engaging
7. Avoid generic responses like 'How are you?' unless specifically asked
8. Build on previous context and topics discussed
9. If the user asks personal questions about your identity or relationship status, politely redirect the conversation to more appropriate topics       
10. Vary your responses and avoid repetitive patterns
11. If you don't know something, be honest about it

Remember to be engaging but professional, and always maintain appropriate boundaries.
Please provide your math questions
You: [  {    "id": 1,    "question": "Factor out the numeric greatest common factor from 54x².",    "studentAnswer": "2 steps: Step 1: Identify the numeric GCF as 6. Step 2: Write 6(9x²).",    "tag": "Factoring out a numeric GCF from a monomial"  },  {    "id": 2,    "question": "Factor out the variable greatest common factor from 7x⁵.",    "studentAnswer": "2 steps: Step 1: Identify the variable GCF as x⁴. Step 2: Write x⁴(7x).",    "tag": "Factoring out a variable GCF from a monomial"  },  {    "id": 3,    "question": "Factor the monomial GCF from 15x² + 10x.",    "studentAnswer": "2 steps: Step
 1: Identify the monomial GCF as 5x². Step 2: Write 5x²(3 + 2/x).",    "tag": "Factoring a monomial GCF from a binomial"  },  {    "id": 4,    "questio
n": "Rearrange and solve for y: 3y - 7 = 2y + 5.",    "studentAnswer": "4 steps: Step 1: Subtract y from both sides: 2y - 7 = 5. Step 2: Add 7: 2y = 12. Step 3: Divide by 2: y = 6. Step 4: State y = 6.",    "tag": "Rearranging linear equations to isolate a variable"  },  {    "id": 5,    "question": "Solve the equation 2(x - 3) - x = 5.",    "studentAnswer": "3 steps: Step 1: Distribute 2: 2x - 3 - x = 5. Step 2: Combine like terms: x - 3 = 5. Step 3: Add 3: x = 8.",    "tag": "Solving multi-step linear equations with parentheses"  },  {    "id": 6,    "question": "Solve for x: x + 7 = 12.",    "studentAnswer": "2 steps: Step 1: Subtract 7: x = 12 - 7. Step 2: Simplify: x = 4.",    "tag": "Solving single-step linear equations (±)"  },  {    "id": 7,    "question": "Solve for x: 5x = 20.",    "studentAnswer": "2 steps: Step 1: Divide both sides by 5: x = 20/5. Step 2: Simplify: x = 6.",    "tag": "Solving single-step linear equations (×, ÷)"  },  {    "id": 8,    "question": "Solve for x: 3x - 4 = 11.",    "studentAnswer": "3 steps: Step 1: Add 4: 3x = 15. Step 2: Divide by 3: x = 15/3. Step 3: Simplify: x = 4.",    "tag": "Solving two-step linear equations"  },  {    "id": 9,    "question": "Find the slope of the line passing through (2, 3) and (5, 11).",    "studentAnswer": "1 step: slope = (5 - 2)/(11 - 3) = 3/8.",    "tag": "Determining slope from two points"  },  {    "id": 10,    "question": "On the graph below, the line crosses the y-axis at (0, –2). What is its y-intercept?",    "studentAnswer": "1 step: y-intercept = (0, –3).",    "tag": "Identifying a line's y-intercept on a graph"  }]

You will be provided an array of math questions and answers from the student. Your job is to classify if the question made a conceptual mistake or if it is a basic mistake.

Always add a key value pair to each question in the array. The value is always enum of "conceptual_mistake" or "basic_mistake". A basic mistake is an error that is writing the sign wrong or writing some numbers wrong. A conceptual mistake is when the student the error is related to the topic in the tag.

Always add another a key value pair to each question in the array. The key is explanation and the value is a string explaining why the question is a conceptual mistake or a basic mistake.


Only respond with the array of questions with the new key value pair. An example of the output is:
[
  {
    "id": 1,
    "question": "Factor out the numeric greatest common factor from 54x².",
    "studentAnswer": "2 steps: Step 1: Identify the numeric GCF as 6. Step 2: Write 6(9x²).",
    "tag": "Factoring out a numeric GCF from a monomial",
    "mistake_type": "conceptual_mistake",
    "explanation": "The student incorrectly identified the numeric GCF as 6 instead of 18."
  },
  ...
]

[  {    "id": 1,    "question": "Factor out the numeric greatest common factor from 54x².",    "studentAnswer": "2 steps: Step 1: Identify the numeric GCF as 6. Step 2: Write 6(9x²).",    "tag": "Factoring out a numeric GCF from a monomial"  },  {    "id": 2,    "question": "Factor out the variable greatest common factor from 7x⁵.",    "studentAnswer": "2 steps: Step 1: Identify the variable GCF as x⁴. Step 2: Write x⁴(7x).",    "tag": "Factoring out a variable GCF from a monomial"  },  {    "id": 3,    "question": "Factor the monomial GCF from 15x² + 10x.",    "studentAnswer": "2 steps: Step 1: Identify the monomial GCF as 5x². Step 2: Write 5x²(3 + 2/x).",    "tag": "Factoring a monomial GCF from a binomial"  },  {    "id": 4,    "question": "Rearrange and solve for y: 3y - 7 = 2y + 5.",    "studentAnswer": "4 steps: Step 1: Subtract y from both sides: 2y - 7 = 5. Step 2: Add 7: 2y = 12. Step 3: Divide by 2: y = 6. Step 4: State y = 6.",    "tag": "Rearranging linear equations to isolate a variable"  },  {    "id": 5,    "question": "Solve the equation 2(x - 3) - x = 5.",    "studentAnswer": "3 steps: Step 1: Distribute 2: 2x - 3 - x = 5. Step 2: Combine like terms: x - 3 = 5. Step 3: Add 3: x = 8.",    "tag": "Solving multi-step linear equations with parentheses"  },  {    "id": 6,    "question": "Solve for x: x + 7 = 12.",    "studentAnswer": "2 steps: Step 1: Subtract 7: x = 12 - 7. Step 2: Simplify: x = 4.",    "tag": "Solving single-step linear equations (±)"  },  {    "id": 7,    "question": "Solve for x: 5x = 20.",    "studentAnswer": "2 steps: Step 1: Divide both sides by 5: x = 20/5. Step 2: Simplify: x = 6.",    "tag": "Solving single-step linear equations (×, ÷)"  },  {    "id": 8,    "question": "Solve for x: 3x - 4 = 11.",    "studentAnswer": "3 steps: Step 1: Add 4: 3x = 15. Step 2: Divide by 3: x = 15/3. Step 3: Simplify: x = 4.",    "tag": "Solving two-step linear equations"  },  {    "id": 9,    "question": "Find the slope of the line passing through (2, 3) and (5, 11).",    "studentAnswer": "1 step: slope = (5 - 2)/(11 - 3) = 3/8.",    "tag": "Determining slope from two points"  },  {    "id": 10,    "question": "On the graph below, the line crosses the y-axis at (0, –2). What is its y-intercept?",    "studentAnswer": "1 step: y-intercept = (0, –3).",    "tag": "Identifying a line's y-intercept on a graph"  }]
[
  {
    "id": 1,
    "question": "Factor out the numeric greatest common factor from 54x².",
    "studentAnswer": "2 steps: Step 1: Identify the numeric GCF as 6. Step 2: Write 6(9x²).",
    "tag": "Factoring out a numeric GCF from a monomial",
    "mistake_type": "conceptual_mistake",
    "explanation": "The student incorrectly identified the numeric GCF as 6 instead of 18."
  },
  {
    "id": 2,
    "question": "Factor out the variable greatest common factor from 7x⁵.",
    "studentAnswer": "2 steps: Step 1: Identify the variable GCF as x⁴. Step 2: Write x⁴(7x).",
    "tag": "Factoring out a variable GCF from a monomial",
    "mistake_type": "conceptual_mistake",
    "explanation": "The variable GCF should be x⁵, not x⁴."
  },
  {
    "id": 3,
    "question": "Factor the monomial GCF from 15x² + 10x.",
    "studentAnswer": "2 steps: Step 1: Identify the monomial GCF as 5x². Step 2: Write 5x²(3 + 2/x).",
    "tag": "Factoring a monomial GCF from a binomial",
    "mistake_type": "conceptual_mistake",
    "explanation": "The GCF is 5x, not 5x², leading to an incorrect factored form."
  },
  {
    "id": 4,
    "question": "Rearrange and solve for y: 3y - 7 = 2y + 5.",
    "studentAnswer": "4 steps: Step 1: Subtract y from both sides: 2y - 7 = 5. Step 2: Add 7: 2y = 12. Step 3: Divide by 2: y = 6. Step 4: State y = 6.",
    "tag": "Rearranging linear equations to isolate a variable",
    "mistake_type": "basic_mistake",
    "explanation": "The student incorrectly subtracted y from both sides instead of 2y."
  },
  {
    "id": 5,
    "question": "Solve the equation 2(x - 3) - x = 5.",
    "studentAnswer": "3 steps: Step 1: Distribute 2: 2x - 3 - x = 5. Step 2: Combine like terms: x - 3 = 5. Step 3: Add 3: x = 8.",
    "tag": "Solving multi-step linear equations with parentheses",
    "mistake_type": "basic_mistake",
    "explanation": "The student made a mistake in combining like terms; it should have been x - 6 = 5."
  },
  {
    "id": 6,
    "question": "Solve for x: x + 7 = 12.",
    "studentAnswer": "2 steps: Step 1: Subtract 7: x = 12 - 7. Step 2: Simplify: x = 4.",
    "tag": "Solving single-step linear equations (±)",
    "mistake_type": "basic_mistake",
    "explanation": "The simplification is correct, but the subtraction step should lead to x = 5, not 4."
  },
  {
    "id": 7,
    "question": "Solve for x: 5x = 20.",
    "studentAnswer": "2 steps: Step 1: Divide both sides by 5: x = 20/5. Step 2: Simplify: x = 6.",
    "tag": "Solving single-step linear equations (×, ÷)",
    "mistake_type": "basic_mistake",
    "explanation": "The division is performed incorrectly; it should be x = 4, not 6."
  },
  {
    "id": 8,
    "question": "Solve for x: 3x - 4 = 11.",
    "studentAnswer": "3 steps: Step 1: Add 4: 3x = 15. Step 2: Divide by 3: x = 15/3. Step 3: Simplify: x = 4.",
    "tag": "Solving two-step linear equations",
    "mistake_type": "basic_mistake",
    "explanation": "The addition step is correct, but the final simplification should lead to x = 5, not 4."
  },
  {
    "id": 9,
    "question": "Find the slope of the line passing through (2, 3) and (5, 11).",
    "studentAnswer": "1 step: slope = (5 - 2)/(11 - 3) = 3/8.",
    "tag": "Determining slope from two points",
    "mistake_type": "conceptual_mistake",
    "explanation": "The student used the coordinates incorrectly; the correct slope calculation should result in 8/3."
  },
  {
    "id": 10,
    "question": "On the graph below, the line crosses the y-axis at (0, –2). What is its y-intercept?",
    "studentAnswer": "1 step: y-intercept = (0, –3).",
    "tag": "Identifying a line's y-intercept on a graph",
    "mistake_type": "basic_mistake",
    "explanation": "The student has misread the y-intercept; it should be (0, –2), not (0, –3)."
  }
]
here it is
[{'id': 1, 'question': 'Factor out the numeric greatest common factor from 54x².', 'studentAnswer': '2 steps: Step 1: Identify the numeric GCF as 6. Step 2: Write 6(9x²).', 'tag': 'Factoring out a numeric GCF from a monomial', 'mistake_type': 'conceptual_mistake', 'explanation': 'The student incorrectly identified the numeric GCF as 6 instead of 18.'}, {'id': 2, 'question': 'Factor out the variable greatest common factor from 7x⁵.', 'studentAnswer': '2 steps: Step 1: Identify the variable GCF as x⁴. Step 2: Write x⁴(7x).', 'tag': 'Factoring out a variable GCF from a monomial', 'mistake_type': 'conceptual_mistake', 'explanation': 'The variable GCF should be x⁵, not x⁴.'}, {'id': 3, 'question': 'Factor the monomial GCF from 15x² + 10x.', 'studentAnswer': '2 steps: Step 1: Identify the monomial GCF as 5x². Step 2: Write 5x²(3 + 2/x).', 'tag': 'Factoring a monomial GCF from a binomial', 'mistake_type': 'conceptual_mistake', 'explanation': 'The GCF is 5x, not 5x², leading to an incorrect factored form.'}, {'id': 9, 'question': 'Find the slope of the line passing through (2, 3) and (5, 11).', 'studentAnswer': '1 step: slope = (5 - 2)/(11 - 3) = 3/8.', 'tag': 'Determining slope from two points', 'mistake_type': 'conceptual_mistake', 'explanation': 'The student used the coordinates incorrectly; the correct slope calculation should result in 8/3.'}]
[{"id": 1, "question": "Factor out the numeric greatest common factor from 54x\u00b2.", "studentAnswer": "2 steps: Step 1: Identify the numeric GCF as 6. Step 2: Write 6(9x\u00b2).", "tag": "Factoring out a numeric GCF from a monomial", "mistake_type": "conceptual_mistake", "explanation": "The student incorrectly identified the numeric GCF as 6 instead of 18."}, {"id": 2, "question": "Factor out the variable greatest common factor from 7x\u2075.", "studentAnswer": "2 steps: Step 1: Identify the variable GCF as x\u2074. Step 2: Write x\u2074(7x).", "tag": "Factoring out a variable GCF from a monomial", "mistake_type": "conceptual_mistake", "explanation": "The variable GCF should be x\u2075, not x\u2074."}, {"id": 3, "question": "Factor the monomial GCF from 15x\u00b2 + 10x.", "studentAnswer": "2 steps: Step 1: Identify the monomial GCF as 5x\u00b2. Step 2: Write 5x\u00b2(3 + 2/x).", "tag": "Factoring a monomial GCF from a binomial", "mistake_type": "conceptual_mistake", "explanation": "The GCF is 5x, not 5x\u00b2, leading to an incorrect factored form."}, {"id": 9, "question": "Find the slope of the line passing through (2, 3) and (5, 11).", "studentAnswer": "1 step: slope = (5 - 2)/(11 - 3) = 3/8.", "tag": "Determining slope from two points", "mistake_type": "conceptual_mistake", "explanation": "The student used the coordinates incorrectly; the correct slope calculation should result in 8/3."}]

You are a planner. You are given a list of questions that the student got conceptually wrong.
Your job is to create a number of lessons of 10 questions each to address the conceptual mistakes by topic.
Create 3 arrays of questions and answers that will help the student correct the conceptual mistakes.
Think step by step and reason through the topics and questions to generate new questions that will help the student practice the topics they got wrong.

Here are three arrays of questions, each focusing on the conceptual mistakes identified in the student's answers. Each array contains 10 questions designed to help the student improve their understanding of the respective topics.

### Array 1: Factoring Out Numeric and Variable GCF

```json
[
  {
    "question": "Factor out the numeric greatest common factor from 36x³.",
    "answer": "The numeric GCF is 36. Factored form: 36(x³)."
  },
  {
    "question": "Factor out the numeric greatest common factor from 48y².",
    "answer": "The numeric GCF is 48. Factored form: 48(y²)."
  },
  {
    "question": "Factor out the numeric greatest common factor from 81x²y.",
    "answer": "The numeric GCF is 81. Factored form: 81(x²y)."
  },
  {
    "question": "Factor out the variable greatest common factor from 5x⁵ + 10x³.",
    "answer": "The variable GCF is 5x³. Factored form: 5x³(x² + 2)."
  },
  {
    "question": "Factor out the variable greatest common factor from 12x⁴y² + 18x²y.",
    "answer": "The variable GCF is 6x²y. Factored form: 6x²y(2x²y + 3)."
  },
  {
    "question": "Factor out the variable greatest common factor from 4x⁶ + 8x⁴.",
    "answer": "The variable GCF is 4x⁴. Factored form: 4x⁴(x² + 2)."
  },
  {
    "question": "Factor out the numeric greatest common factor from 24x + 36.",
    "answer": "The numeric GCF is 12. Factored form: 12(2x + 3)."
  },
  {
    "question": "Factor out the numeric greatest common factor from 18x² + 27x.",
    "answer": "The numeric GCF is 9x. Factored form: 9x(2x + 3)."
  },
  {
    "question": "Factor out the variable greatest common factor from 9x²y + 15xy².",
    "answer": "The variable GCF is 3xy. Factored form: 3xy(3x + 5y)."
  },
  {
    "question": "Factor out the variable greatest common factor from 20x³y² + 5x²y.",
    "answer": "The variable GCF is 5x²y. Factored form: 5x²y(4x + 1)."
  }
]
```

### Array 2: Solving Linear Equations

```json
[
  {
    "question": "Rearrange and solve for y: 4y - 8 = 2y + 4.",
    "answer": "y = 4."
  },
  {
    "question": "Rearrange and solve for y: 5y + 3 = 2y + 15.",
    "answer": "y = 4."
  },
  {
    "question": "Rearrange and solve for y: 6y - 2 = 3y + 12.",
    "answer": "y = 4.67."
  },
  {
    "question": "Rearrange and solve for y: 10 - 3y = 7.",
    "answer": "y = 1."
  },
  {
    "question": "Rearrange and solve for y: 2y + 5 = 3y - 2.",
    "answer": "y = 7."
  },
  {
    "question": "Rearrange and solve for y: 7y - 4 = 2y + 16.",
    "answer": "y = 4."
  },
  {
    "question": "Rearrange and solve for y: 9 - 3y = 0.",
    "answer": "y = 3."
  },
  {
    "question": "Rearrange and solve for y: 8y + 4 = 20.",
    "answer": "y = 2."
  },
  {
    "question": "Rearrange and solve for y: 3(y - 1) = 2(y + 3).",
    "answer": "y = 5."
  },
  {
    "question": "Rearrange and solve for y: 5y + 2 = 3y + 10.",
    "answer": "y = 4."
  }
]
```

### Array 3: Determining Slope

```json
[
  {
    "question": "Find the slope of the line passing through (1, 2) and (4, 8).",
    "answer": "Slope = (8 - 2) / (4 - 1) = 2."
  },
  {
    "question": "Find the slope of the line passing through (3, 5) and (6, 11).",
    "answer": "Slope = (11 - 5) / (6 - 3) = 2."
  },
  {
    "question": "Find the slope of the line passing through (0, 0) and (5, 5).",
    "answer": "Slope = (5 - 0) / (5 - 0) = 1."
  },
  {
    "question": "Find the slope of the line passing through (2, 3) and (2, 7).",
    "answer": "Slope = undefined (vertical line)."
  },
  {
    "question": "Find the slope of the line passing through (1, 1) and (3, 5).",
    "answer": "Slope = (5 - 1) / (3 - 1) = 2."
  },
  {
    "question": "Find the slope of the line passing through (0, 4) and (4, 0).",
    "answer": "Slope = (0 - 4) / (4 - 0) = -1."
  },
  {
    "question": "Find the slope of the line passing through (-1, 2) and (2, 5).",
    "answer": "Slope = (5 - 2) / (2 - (-1)) = 1."
  },
  {
    "question": "Find the slope of the line passing through (3, 6) and (3, 0).",
    "answer": "Slope = undefined (vertical line)."
  },
  {
    "question": "Find the slope of the line passing through (0, 0) and (0, 2).",
    "answer": "Slope = undefined (vertical line)."
  },
  {
    "question": "Find the slope of the line passing through (-2, -1) and (2, 3).",
    "answer": "Slope = (3 - (-1)) / (2 - (-2)) = 1."
  }
]
```

Each of these arrays focuses on addressing specific conceptual mistakes, providing the student with practice questions that reinforce their understanding of the topics they struggled with.