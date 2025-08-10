# backend/services/openai_client.py
import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Dict, Any
from config.prompts import GENERATE_QUIZ_PROMPT

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def generate_quiz(self, topic: str, num_questions: int = 5) -> Dict[str, Any]:
        """Generate a quiz using GPT."""
        prompt = GENERATE_QUIZ_PROMPT.format(topic=topic, num_questions=num_questions)
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # or "gpt-3.5-turbo" for cheaper
                messages=[
                    {"role": "system", "content": "You are a quiz generator. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            return content
            
        except Exception as e:
            return {"error": f"Failed to generate quiz: {str(e)}"}
    
    def grade_quiz(self, questions: List[Dict], user_answers: List[int]) -> Dict[str, Any]:
        """Grade quiz answers using GPT for detailed feedback."""
        prompt = f"""
        Grade this quiz submission and provide detailed feedback:
        
        Questions and user answers:
        {questions}
        
        User answers (by index): {user_answers}
        
        Provide JSON response:
        {{
            "score": 85,
            "total_questions": {len(questions)},
            "correct_answers": 4,
            "feedback": [
                {{
                    "question_index": 0,
                    "correct": true,
                    "feedback": "Great job! You understood..."
                }}
            ],
            "overall_feedback": "Overall performance summary"
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful teacher providing quiz feedback. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            return content  

        except Exception as e:
            return {"error": f"Failed to grade quiz: {str(e)}"}
    

if __name__ == "__main__":
    openai_service = OpenAIService()
    print(openai_service.generate_quiz("Python"))
    # print(openai_service.grade_quiz([{"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "correct_answer": 0}], [0]))