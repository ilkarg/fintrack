from fastapi import APIRouter

from app.domain.dtos import ResponseDTO
from app.application.usecases.ping.ping_get_usecase import PingGetUsecase

router = APIRouter()


@router.get("/", response_model=ResponseDTO, status_code=200)
async def ping_get_route():
    return await PingGetUsecase().execute()