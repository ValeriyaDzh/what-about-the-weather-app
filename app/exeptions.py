from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    def __repr__(self) -> str:
        return self.detail


class UnprocessableEntityException(HTTPException):
    def __init__(self, detail: str = "Unprocessable entity"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail
        )

    def __repr__(self) -> str:
        return self.detail
