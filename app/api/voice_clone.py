from app.core.api_request import get
from app.core.error_code import ErrorCode
from app.msg.base_resp import BaseResponse
from app.msg.voice_clone_msg import VoiceCloneModelsResponse


async def get_voice_clone_models():
    resp = await get(
        "/api/voice_clone/models", response_model=BaseResponse[VoiceCloneModelsResponse]
    )
    if resp is None:
        return "Failed to get voice clone models"
    if resp.code != ErrorCode.SUCCESS.code:
        return "Failed to get voice clone models"
    if resp.data is None:
        return "No voice clone models found"
    return resp.data.model_dump()
