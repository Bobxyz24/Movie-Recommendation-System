# movie_recommendation.py

movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
    "comedy": ["Superbad", "The Hangover", "Step Brothers"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"]
}

def recommend_movie(genre):
    return movies.get(genre, ["No movies found in this genre."])

# Sample usage
genre = input("Enter a genre (action, comedy, drama): ").lower()
print("Recommended movies:", recommend_movie(genre))
