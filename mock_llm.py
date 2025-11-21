
def mock_llm(prompt):
    """
    A simple mock LLM response for offline notebook use.
    Replace with actual ADK model call when deploying.
    """
    return "AI Response: " + prompt[:150]

