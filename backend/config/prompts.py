
GENERATE_QUIZ_PROMPT="""
Create a {num_questions}-question quiz about {topic}. 
        Each question can be multiple choice, numeric, or text.
        Include the question number, question type, question, options (if multiple choice), correct answer, and explanation.
        Format as JSON:
        Example Multiple Choice Question:
        {{
            "title": "Quiz about {topic}",
            "questions": [
                {{
                    "question_number": 1,
                    "question_type": "multiple_choice",
                    "question": "Question text here?",
                    "options": ["A", "B", "C", "D"],
                    "correct_answer": "A",
                    "explanation": "Why this answer is correct"
                }}
            ]
        }}
        Example Numeric Question:
        {{
            "title": "Quiz about {topic}",
            "questions": [
                {{
                    "question_number": 1,
                    "question_type": "numeric",
                    "question": "Question text here?",
                    "options": null,
                    "correct_answer": "10",
                    "explanation": "Why this answer is correct"
                }}
            ]
        }}
        Example Text Question:
        {{
            "title": "Quiz about {topic}",
            "questions": [
                {{
                    "question_number": 1,
                    "question_type": "text",
                    "question": "Question text here?",
                    "options": null,
                    "correct_answer": "Answer text here",
                    "explanation": "Why this answer is correct"
                }}
            ]
        }}
        Only return the JSON object, no other text or comments.
        Select the best fitting question type for each question.
"""