from fastapi import HTTPException, status


class AppException(HTTPException):
    detail = ""
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self):
        super().__init__(
            detail=self.detail,
            status_code=self.status_code
        )


class FailedToUploadFileException(AppException):
    detail = "Ошибка при загрузке файла"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class FailedToCreateMemeException(AppException):
    detail = "Ошибка при создании мема"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class FailedToUpdateMemeException(AppException):
    detail = "Ошибка при обновлении мема"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class IncorrectFileFormatException(AppException):
    detail = "Неверный формат файла. Допустимые: .png, .jpg, .jpeg, .webp"
    status_code = status.HTTP_400_BAD_REQUEST


class IncorrectIDException(AppException):
    detail = "Неверный ID мема"
    status_code = status.HTTP_400_BAD_REQUEST


class FailedToDeleteImageException(AppException):
    detail = "Ошибка при удалении изображения"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
