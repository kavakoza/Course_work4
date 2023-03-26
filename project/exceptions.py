class BaseServiceError(Exception):
    code = 500
    message = 'Unexpected error'


class ItemNotFound(BaseServiceError):
    code = 404
    message = 'Not found'


class UserAlreadyExists(BaseServiceError):
    code = 400
    message = 'User already exists'
