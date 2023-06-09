class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        session = self.Session()
        movies = session.query(Movie).all()
        session.close()
        return movies



    def get_movie_by_id(self, movie_id):
        session = self.Session()
        movie = session.query(Movie).filter_by(id=movie_id).first()
        session.close()
        return movie

    def create_movie(self, title, director, rating):
        session = self.Session()
        movie = Movie(title=title, director=director, rating=rating)
        session.add(movie)
        session.commit()
        session.close()

    def search_movies(self, title):
        session = self.Session()
        movies = session.query(Movie).filter(Movie.title.ilike(f'%{title}%')).all()
        session.close()
        return movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
