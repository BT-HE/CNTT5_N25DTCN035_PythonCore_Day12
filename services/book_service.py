from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.book_model import BookModel
from models.author_model import AuthorModel
from schemas.book_schema import (
    BookCreateSchema,
    BookResponseSchema
)


def create_book(
    db: Session,
    book_in: BookCreateSchema
):
    # Kiểm tra author_id có tồn tại không
    author = db.query(AuthorModel).filter(
        AuthorModel.id == book_in.author_id
    ).first()

    # Không tồn tại tác giả
    if not author:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"Mã tác giả author_id = "
                f"{book_in.author_id} không tồn tại "
                f"trong hệ thống CSDL!"
            )
        )

    # Tạo sách mới
    new_book = BookModel(
        title=book_in.title,
        price=book_in.price,
        author_id=book_in.author_id
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book