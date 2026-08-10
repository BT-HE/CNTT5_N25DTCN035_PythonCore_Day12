from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from database import Base


class AuthorModel(Base):
    __tablename__ = "authors"
    id = Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    name = Mapped[str] = mapped_column(String(100), nullable = False)
    email = Mapped[str] = mapped_column(String(100), nullable = False, unique = False)
    bio = Mapped[str] = mapped_column(Text, nullable = False)

    books = relationship(
        "BookModel",
        back_populates = False
    )

