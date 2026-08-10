from pydantic import BaseModel


class BookCreateSchema(BaseModel):
    title: str
    price: float
    author_id: int


class AuthorResponseSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class BookResponseSchema(BaseModel):
    id: int
    title: str
    price: float
    author_id: int
    author: AuthorResponseSchema

    class Config:
        from_attributes = True