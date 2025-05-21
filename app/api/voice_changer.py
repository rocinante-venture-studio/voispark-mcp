from app.core.api_request import get
from app.core.error_code import ErrorCode
from app.msg.base_resp import BaseResponse
from app.msg.voice_changer_msg import VoiceChangerModelsResponse


async def get_voice_changer_models():
    resp = await get(
        "/api/voice_changer/models",
        response_model=BaseResponse[VoiceChangerModelsResponse],
    )
    if resp is None:
        return "Failed to get voice changer models"
    if resp.code != ErrorCode.SUCCESS.code:
        return "Failed to get voice changer models"
    if resp.data is None:
        return "No voice changer models found"
    return resp.data.model_dump()
