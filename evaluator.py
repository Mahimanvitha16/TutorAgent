
def make_quiz(topic):
    """
    Generates a simple quiz for the topic.
    """
    return [
        {
            "question": f"What is the main idea of {topic}?",
            "answer": "photosynthesis" if "photo" in topic.lower() else topic
        }
    ]


def evaluate_quiz(user_answer, correct_answer):
    """
    Returns correctness feedback for the answer.
    """
    if user_answer.lower().strip() == correct_answer.lower().strip():
        return "Correct!"
    return "Almost there! Review again."
