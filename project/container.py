from project.dao import GenresDAO
from project.dao.director import DirectorsDAO
from project.dao.movie import MoviesDAO
from project.dao.user import UserDAO
from project.services.auth_service import AuthService

from project.services.genres_service import GenresService
from project.services.directors_service import DirectorsService
from project.services.movies_service import MoviesService
from project.services.users_service import UsersService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
user_dao = UserDAO(db.session)
movie_dao = MoviesDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UsersService(dao=user_dao)
movie_service = MoviesService(dao=movie_dao)
auth_service = AuthService(user_service=user_service)
