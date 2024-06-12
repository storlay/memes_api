from fastapi import APIRouter, status, UploadFile, File
from fastapi_pagination import Page, paginate

from exceptions import FailedToCreateMemeException, IncorrectFileFormatException, IncorrectIDException
from memes.service import MemesService
from memes.shemas import GetMemeDTO

router = APIRouter(
    tags=["Public memes API"],
    prefix="/memes"
)


@router.get(
    "",
    status_code=status.HTTP_200_OK
)
async def get_list_memes() -> Page[GetMemeDTO]:
    list_memes = await MemesService.get_list()
    return paginate(list_memes)


@router.get(
    "/{meme_id}",
    status_code=status.HTTP_200_OK
)
async def get_meme(meme_id: int) -> GetMemeDTO:
    meme = await MemesService.get_by_id(meme_id)

    if not meme:
        raise IncorrectIDException

    return meme


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


@router.delete(
    "/{meme_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_meme(meme_id: int) -> None:
    await MemesService.delete(meme_id)
