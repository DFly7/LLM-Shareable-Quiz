from services.openAI import OpenAIService

def create_quiz(topic: str, num_questions: int) -> str:
    """
    Create a quiz using the OpenAI API.
    The quiz is generated using the OpenAI API and stored in the database.
    Args:
        topic: The topic of the quiz.
        num_questions: The number of questions in the quiz.
    Returns:
        Quiz ID
    """
    openai_service = OpenAIService()
    quiz = openai_service.generate_quiz(topic, num_questions)
    print(quiz)
    return quiz