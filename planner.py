def generate_study_plan(topic):
    """
    Creates a simple 3-step study plan for the topic.
    """
    plan = [
        {"step": 1, "task": f"Explain the core concept of {topic}"},
        {"step": 2, "task": f"Retrieve important notes related to {topic}"},
        {"step": 3, "task": f"Create a short quiz about {topic}"}
    ]
    return plan

