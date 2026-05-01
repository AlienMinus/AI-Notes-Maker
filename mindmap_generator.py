from keywords import extract_keywords

def generate_mindmap(text):
    keywords = extract_keywords(text)

    if not keywords:
        return {"central_topic": "None", "branches": []}

    return {
        "central_topic": keywords[0],
        "branches": [{"topic": k, "subtopics": []} for k in keywords[1:]]
    }