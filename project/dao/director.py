from project.models import Director
from project.dao.base import BaseDAO


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director