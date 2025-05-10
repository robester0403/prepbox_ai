QUESTION_CLASSIFIER_PROMPT = """
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
"""

__all__ = ['QUESTION_CLASSIFIER_PROMPT']