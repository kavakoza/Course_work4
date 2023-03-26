from .auth import auth_ns, user_ns
from .main import genres_ns
from .main.directors import director_ns
from .main.movies import movies_ns
__all__ = [
    'auth_ns',
    'genres_ns',
    'user_ns',
    'director_ns',
    'movies_ns'
]
