import os

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from exceptions import IncorrectUsernameOrPasswordException

security = HTTPBasic()


def get_current_user(
        credentials: HTTPBasicCredentials = Depends(security),
):
    username = os.environ.get("MINIO_ROOT_USER")
    password = os.environ.get("MINIO_ROOT_PASSWORD")

    if username != credentials.username or password != credentials.password:
        raise IncorrectUsernameOrPasswordException

    return {"username": credentials.username}
