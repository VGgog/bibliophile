from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .scheme import AddBookValidation, BookScheme
from .services.admin_service import AdminService
from ..database import get_db
from config import Config

admin_route = APIRouter(tags=['admin'])


@admin_route.post(
    '/add_book',
    status_code=status.HTTP_200_OK,
    response_model=BookScheme
)
async def add_book_route(
    add_book_scheme: AddBookValidation,
    admin_service: AdminService = Depends(),
    db: Session = Depends(get_db)
):
    """Route for add new book in db"""
    if Config.admin_token != add_book_scheme.token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission"
        )

    elif not admin_service.add_book(db=db, book_data=add_book_scheme):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Book already added"
        )

    return BookScheme(
        author=add_book_scheme.author,
        title=add_book_scheme.title,
        text=add_book_scheme.text
        )
