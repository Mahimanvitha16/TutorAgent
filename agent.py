from .planner import generate_study_plan
from .retriever import retrieve_notes
from .evaluator import make_quiz, evaluate_quiz
from .mock_llm import mock_llm

class TutorAgent:
    def _init_(self):
        pass

    def run(self, topic):
        output = {}

        # Step 1 — Planning
        plan = generate_study_plan(topic)
        output["plan"] = plan

        # Step 2 — Retrieval
        notes = retrieve_notes(topic)
        output["notes"] = notes

        # Step 3 — Explanation
        explanation = mock_llm("Explain: " + " ".join(notes))
        output["explanation"] = explanation

        # Step 4 — Quiz
        quiz = make_quiz(topic)
        output["quiz"] = quiz

        return output

    def evaluate(self, user_answer, correct_answer):
        return evaluate_quiz(user_answer, correct_answer)
