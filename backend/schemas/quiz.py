from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Question(BaseModel):
    question_number: int
    question_type: str
    question: str
    options: Optional[List[str]] = None
    correct_answer: str
    explanation: str

class QuizData(BaseModel):
    questions: List[Question]
    time_limit_minutes: Optional[int] = None

class Quiz(BaseModel):
    id: UUID
    creator_id: UUID
    title: str
    description: Optional[str]
    quiz_data: QuizData
    created_at: datetime
    shareable_link: str
