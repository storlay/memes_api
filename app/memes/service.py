import os

import requests
from fastapi import UploadFile, status
from sqlalchemy import insert, select

from db.db import async_session_maker
from exceptions import FailedToUploadFileException
from memes.models import Memes
from memes.shemas import GetMemeDTO


class MemesService:

    @classmethod
    async def get_list(cls) -> list[GetMemeDTO]:
        query = select(Memes.__table__.columns)
        async with async_session_maker() as session:
            list_memes = await session.execute(query)
            return list_memes.mappings().all()

    @classmethod
    async def get_by_id(cls, meme_id: int) -> GetMemeDTO | None:
        query = (
            select(Memes.__table__.columns)
            .where(Memes.id == meme_id)
        )
        async with async_session_maker() as session:
            meme = await session.execute(query)
            return meme.mappings().one_or_none()

    @classmethod
    async def add(
            cls,
            description: str,
            file: UploadFile
    ) -> GetMemeDTO | None:
        upload_url = os.environ.get("MEDIA_UPLOAD_ENDPOINT")
        auth = (os.environ.get("MINIO_ROOT_USER"), os.environ.get("MINIO_ROOT_PASSWORD"))
        files = {"file": (file.filename, file.file, file.content_type)}
        response = requests.post(upload_url, files=files, auth=auth)

        if response.status_code != status.HTTP_201_CREATED:
            raise FailedToUploadFileException

        image_url = response.json()["url"]

        query = (
            insert(Memes)
            .values(
                description=description,
                image_url=image_url
            )
            .returning(
                Memes.__table__.columns
            )
        )

        async with async_session_maker() as session:
            new_meme = await session.execute(query)
            await session.commit()
            return new_meme.mappings().one_or_none()

    @classmethod
    def validate_file_format(cls, file: UploadFile) -> bool:
        file_format = file.filename.split(".")[-1].lower()
        correct_formats = {"png", "jpg", "jpeg", "webp"}
        return file_format in correct_formats
