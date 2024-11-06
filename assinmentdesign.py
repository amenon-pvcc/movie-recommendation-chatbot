# Movie class to create a basic abstraction of a movie
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.title} - Rating: {self.rating}"

# MovieDatabase class to manage a collection of movies and genres
class MovieDatabase:
    def __init__(self):
        self.movies = self.load_movies()

    def load_movies(self):
        # Initialize a small set of sample movies for each genre
        return [
            Movie("Inception", "Sci-Fi", "8.8"),
            Movie("The Godfather", "Crime", "9.2"),
            Movie("The Shawshank Redemption", "Drama", "9.3"),
            # Add additional movies as needed
        ]

    def get_movies_by_genre(self, genre):
        # Filter movies by genre and return the list
        return [movie for movie in self.movies if movie.genre.lower() == genre.lower()]

# Chatbot class to interact with the user and provide movie recommendations
class Chatbot:
    def __init__(self, movie_database):
        self.movie_database = movie_database

    def get_user_genre(self):
        # Prompt user to enter a genre
        genre = input("Enter a movie genre you're interested in: ")
        return genre

    def recommend_movie(self, genre):
        # Get list of movies in the chosen genre
        movies = self.movie_database.get_movies_by_genre(genre)
        
        # If movies exist in the genre, display them
        if movies:
            print("\nHere are some movies you might enjoy:\n")
            for movie in movies:
                print(movie)
        else:
            print("Sorry, no movies found in that genre. Try another one.")

    def run(self):
        # Main function to run the chatbot
        genre = self.get_user_genre()
        self.recommend_movie(genre)

import csv

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

# Main code to initialize and run the chatbot program
if __name__ == "__main__":
    movie_db = MovieDatabase()  # Create movie database instance
    chatbot = Chatbot(movie_db)  # Create chatbot instance with the database
    chatbot.run()  # Run the chatbot
