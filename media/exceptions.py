from fastapi import HTTPException, status


class MediaException(HTTPException):
    detail = ""
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self):
        super().__init__(
            detail=self.detail,
            status_code=self.status_code
        )


class IncorrectUsernameOrPasswordException(MediaException):
    detail = "Неверное имя или пароль"
    status_code = status.HTTP_401_UNAUTHORIZED
