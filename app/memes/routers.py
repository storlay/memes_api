from fastapi import APIRouter, status, UploadFile, File

from exceptions import FailedToCreateMemeException, IncorrectFileFormatException
from memes.service import MemesService
from memes.shemas import GetMemeDTO

router = APIRouter(
    tags=["Public memes API"],
    prefix="/memes"
)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
async def add_meme(
        description: str,
        file: UploadFile = File(...)
) -> GetMemeDTO:
    if not MemesService.validate_file_format(file):
        raise IncorrectFileFormatException

    new_meme = await MemesService.add(description, file)

    if not new_meme:
        raise FailedToCreateMemeException

    return new_meme
