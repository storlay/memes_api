from fastapi import FastAPI, status, UploadFile, File

from minio_client import MinioClient

app = FastAPI(
    title="MinIO storage",
    root_path="/media"
)

minio_client = MinioClient()


@app.post(
    "/upload",
    status_code=status.HTTP_201_CREATED
)
async def upload_image(file: UploadFile = File(...)):
    url = await minio_client.upload_file(file)
    return {"url": url}
