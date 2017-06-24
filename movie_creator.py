from movie import Movie


def fetch_movies():
    """ fetches data from data.txt file and
        returns a list of  Movie objects
    """
    movies = []
    # Read data from data.txt
    with open("data.txt") as f:
        content = f.readlines()

    # Create movie objects from the data collected
    for c in content:
        m = c.split(";")
        movies.append(Movie(m[0], m[1], m[2], m[3], m[4]))
    return movies
