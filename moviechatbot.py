import csv

# Define the Movie class (without the summary attribute)
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __repr__(self):
        return f"'{self.title}' ({self.genre}) - Rating: {self.rating}"

# Define the MovieDatabase class to load movies from CSV
class MovieDatabase:
    def __init__(self):
        self.movies = self.load_movies()

    def load_movies(self):
        movies = []
        with open("movies.csv", mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                movies.append(Movie(row["title"], row["genre"], float(row["rating"])))
        return movies

    def get_movies_by_genre(self, genre):
        # Filter the movies by the specified genre
        return [movie for movie in self.movies if movie.genre.lower() == genre.lower()]

# Define the chatbot function
def chatbot():
    print("Welcome to the Movie Recommendation Chatbot!")
    print("I can recommend movies based on genre.")
    
    # Create an instance of the MovieDatabase class
    movie_db = MovieDatabase()

    while True:
        # Ask the user for a genre
        genre = input("\nEnter a movie genre (e.g., Sci-Fi, Drama, Comedy, etc.) or 'exit' to quit: ").strip()

        if genre.lower() == 'exit':
            print("Goodbye!")
            break

        # Get movies by the genre
        movies = movie_db.get_movies_by_genre(genre)

        if movies:
            print(f"\nHere are some {genre} movies you might like:")
            for movie in movies:
                print(movie)
        else:
            print(f"\nSorry, I couldn't find any {genre} movies. Try another genre.")

# Main function to run the chatbot
if __name__ == "__main__":
    chatbot()
