class AppException(Exception):
    status_code: int = 400
    detail: str = "Application error"

    def __init__(self, detail: str | None = None):
        if detail:
            self.detail = detail


class InvalidFileTypeError(AppException):
    status_code = 400
    detail = "Invalid file type"


class FileNotProvided(AppException):
    status_code = 400
    detail = "File not provided"


class ConfigsNotProvided(AppException):
    status_code = 400
    detail = "Configurations not provided"


# class UserNotFoundError(AppException):
#     status_code = 404
#     detail = "User not found"


# class UnauthorizedError(AppException):
#     status_code = 401
#     detail = "Unauthorized"
