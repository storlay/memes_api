from fastapi import Depends, FastAPI, File, UploadFile, status

from minio_client import MinioClient
from security.auth import get_current_user

app = FastAPI(
    title="MinIO storage",
    root_path="/media"
)

minio_client = MinioClient()


@app.post(
    "/upload",
    status_code=status.HTTP_201_CREATED
)
async def upload_image(
        user: str = Depends(get_current_user),
        file: UploadFile = File(...),
) -> dict:
    url, filename = await minio_client.upload_file(file)
    return {"url": url, "filename": filename}


@app.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_image(
        filename: str,
        user: str = Depends(get_current_user)
) -> None:
    await minio_client.delete_file(filename)
