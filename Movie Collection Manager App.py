# Defining a class to represent a movie

class Movie:
    def __init__(self, movie_id, title, director, release_year, genre):
        self.movie_id = movie_id                                          # unique ID for each movie
        self.title = title                                                # Title of the movie
        self.director = director                                          # The person who directed the movie
        self.release_year = release_year                                  # Year the movie was released
        self.genre = genre                                                # Category that describes the content and style of each film

    # Defining how the movie should be printed

    def __str__(self):
        return (
            f"ID:{self.movie_id}\n"
            f"Title:{self.title}\n"
            f"Director:{self.director}\n"
            f"Year:{self.release_year}\n"
            f"Genre:{self.genre}"
        )


# Defining a class to manages a collection of movies

class MovieManager:
    def __init__(self):
        self.movies = []                                                 # Using a list data structure to store movies

    # Adding a new movie to the collection

    def add_movie(self):
        movie_id = input("Enter unique Movie ID:")

        # Check if Movie ID is already used
        for movie in self.movies:
              if movie.movie_id == movie_id:
                  print("Movie ID already exists. Please try again.")
                  return

# Getting the other relevant details about the movie from the user
        title=input("Enter Movie Title:")
        director=input("Enter Movie Director:")

        #Validate that release_year must be a number
        release_year_input=input("Enter Movie Release Year:")

        if release_year_input.isdigit():
            release_year=int(release_year_input)
        else:
            print("Invalid year. It must be a number.")
            return

        genre=input("Enter Movie Genre:")

        #Create and add the movie to the list

        movie =Movie(
            movie_id,
            title,
            director,
            release_year,
            genre
        )
        self.movies.append(movie)
        print("Movie added successfully!")

    #View all the movies in the list

    def view_movies(self):
        if not self.movies:
            print("No movies in the collection.")
            return

        print("All movies in the collection:")
        count = 1
        for movie in self.movies:
            print(f"{count}. {movie}")
            count += 1

    #Search for a movie by title

    def search_movie(self):
        title=input("Enter Movie Title to search:").lower()
        found = False

        for movie in self.movies:
            if title in movie.title.lower():
                print(movie)
                found = True
        if not found:
            print("Movie title not found.")

#Update an existing movie

    def update_movie(self):
        movie_id = input("Enter Movie ID to update:")
        for movie in self.movies:
            if movie.movie_id == movie_id:
                print("Leave input empty to keep the current value.")

#Get other relevant new values
                new_title=input(f"Enter the new title({movie.title}):")
                new_director=input(f"Enter the new director({movie.director}):")
                new_year_input=input(f"Enter the new release year({movie.release_year}):")
                new_genre=input(f"Enter the new genre({movie.genre}):")

#Update attributes if new input is provided
                if new_title :
                    movie.title=new_title
                if new_director :
                    movie.director=new_director
                if new_year_input:
                    if new_year_input.isdigit():
                        movie.release_year = int(new_year_input)
                    else:
                        print("Invalid year. Release year must be a number.")
                        return
                if new_genre :
                    movie.genre=new_genre

                print("Movie updated successfully!")
                return
        print("Movie not found.")

#Delete a movie by ID

    def delete_movie(self):
        movie_id = input("Enter Movie ID to delete:")

        for movie in self.movies:
            if movie.movie_id == movie_id:
                self.movies.remove(movie)
                print("Movie deleted successfully!")
                return
        print("Movie not found.")

#Main function that runs the menu loop

def main():
        manager = MovieManager()

        while True:
            print("Welcome to Movie Collection Manager App")
            print("1.Add a New Movie")
            print("2.View All Movies")
            print("3.Search a Movie by Title")
            print("4.Update Existing Movie")
            print("5.Delete a Movie")
            print("6.Exit")

            choice = input("Enter your choice(1-6):")

            if choice == "1":
                manager.add_movie()
            elif choice == "2":
                manager.view_movies()
            elif choice == "3":
                manager.search_movie()
            elif choice == "4":
                manager.update_movie()
            elif choice == "5":
                manager.delete_movie()
            elif choice == "6":
                print("Thank you for using Movie Collection Manager App! Have a great day!")
                break
            else:
                print("Invalid choice. Please select from 1-6 again.")


#Run the program
if __name__ == "__main__":
        main()




