# CodSoft AI Internship - Task 4: Recommendation System
# Built for Python 3.15 Compatibility (No external libraries required)

def get_recommendations():
    # Simple dataset of movies and their genres
    movies = [
        {"title": "The Dark Knight", "genre": "Action"},
        {"title": "Inception", "genre": "Sci-Fi"},
        {"title": "Interstellar", "genre": "Sci-Fi"},
        {"title": "The Avengers", "genre": "Action"},
        {"title": "Finding Nemo", "genre": "Animation"},
        {"title": "Toy Story", "genre": "Animation"},
        {"title": "The Matrix", "genre": "Sci-Fi"},
        {"title": "John Wick", "genre": "Action"}
    ]

    print("--- Movie Recommendation System ---")
    print("Available Genres: Action, Sci-Fi, Animation")
    user_genre = input("Enter your favorite genre: ").strip().capitalize()

    # Content-Based Filtering Logic
    recommendations = [m['title'] for m in movies if m['genre'] == user_genre]

    print(f"\n[AI Analysis] Based on your interest in {user_genre}:")
    if recommendations:
        for i, movie in enumerate(recommendations, 1):
            print(f"{i}. {movie}")
    else:
        print("Sorry, we don't have recommendations for that genre yet!")

if __name__ == "__main__":
    get_recommendations()