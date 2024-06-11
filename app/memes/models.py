from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Memes(Base):
    __tablename__ = "memes"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    image_url: Mapped[str]
