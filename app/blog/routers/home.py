from fastapi import APIRouter
from starlette import status

router = APIRouter(
    tags=["Home"]
)

@router.get('/',status_code=status.HTTP_200_OK)
def home():
    return {
        "Welcome to Blog Base"
    }