def clean_ai_response(ai_response: str):

    cleaned = ai_response.strip()

    if "{" in cleaned and "}" in cleaned:
        start = cleaned.find("{")
        end = cleaned.rfind("}") + 1
        cleaned = cleaned[start:end]

    return cleaned