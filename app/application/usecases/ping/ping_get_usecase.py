from app.domain.dtos import ResponseDTO


class PingGetUsecase:
    async def execute(self):
        return ResponseDTO.model_validate({
            "message": "pong"
        })