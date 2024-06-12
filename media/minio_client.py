import os
import uuid
from contextlib import asynccontextmanager
from io import BytesIO

from aiobotocore.session import get_session
from fastapi import UploadFile


class MinioClient:

    def __init__(self):
        self.url = os.environ.get("MINIO_ENDPOINT")
        self.root_user = os.environ.get("MINIO_ROOT_USER")
        self.root_password = os.environ.get("MINIO_ROOT_PASSWORD")
        self.bucket = "memes"
        self.session = get_session()
        self.config = {
            "endpoint_url": self.url,
            "aws_access_key_id": self.root_user,
            "aws_secret_access_key": self.root_password
        }

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(self, file: UploadFile) -> tuple[str, str]:
        filename = f"{uuid.uuid4()}.jpg"
        params = {"Bucket": self.bucket, "Key": filename}
        file_content = await file.read()

        async with self.get_client() as client:
            await self.check_bucket(client)
            await client.put_object(
                Bucket=self.bucket,
                Key=filename,
                Body=BytesIO(file_content)
            )
            url = await client.generate_presigned_url(
                "get_object",
                Params=params
            )
            return url, filename

    async def delete_file(self, filename: str):
        async with self.get_client() as client:
            await client.delete_object(Bucket=self.bucket, Key=filename)

    async def check_bucket(self, client):
        response = await client.list_buckets()
        if self.bucket not in (b["Name"] for b in response["Buckets"]):
            await client.create_bucket(Bucket=self.bucket)
