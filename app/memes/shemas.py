from pydantic import BaseModel


class GetMemeDTO(BaseModel):
    id: int
    description: str
    image_url: str
