def update(context: dict, intent: str, message: str) -> dict:
    """
    Baseline-Dialogue-Manager: speichert minimalen Kontext.
    """
    context["last_intent"] = intent
    context["last_message"] = message
    return context
