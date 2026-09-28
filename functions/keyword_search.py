import json

def search_movies(query: str) -> list[dict]:
    """
    Search for movies using the provided query.

    Args:
        query (str): The search query.
    """
    with open("data/movies.json", "r") as file:
        movies = json.load(file).get("movies", [])
    # Simple keyword search (case-insensitive)
    results = [
        movie for movie in movies
        if query.lower() in movie.get("title", "").lower()
    ]
    return results
