from app.core.api_request import get
from app.core.error_code import ErrorCode
from app.msg.base_resp import BaseResponse
from app.msg.tts_msg import TTSProviderListResponse


async def get_tts_models():
    resp = await get(
        "/api/tts/models",
        response_model=BaseResponse[TTSProviderListResponse],
    )
    if resp is None:
        return "Failed to get tts models"
    if resp.code != ErrorCode.SUCCESS.code:
        return "Failed to get tts models"
    if resp.data is None:
        return "No tts models found"
    return resp.data.model_dump()
