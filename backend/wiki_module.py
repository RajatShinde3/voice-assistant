import wikipedia

def wiki_answer(query: str) -> str:
    """
    Searches Wikipedia and returns a short summary of the query.
    Handles disambiguation and missing pages gracefully.
    """
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query was too broad. Try something more specific like: {e.options[0]}"

    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."

    except Exception as e:
        return "Something went wrong while fetching the answer."
