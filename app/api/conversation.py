from app.core.api_request import get
from app.core.error_code import ErrorCode
from app.msg.base_resp import BaseResponse
from app.msg.conversation_msg import ConversationModelsResponse


async def get_conversation_models():
    resp = await get(
        "/api/conversation/models",
        response_model=BaseResponse[ConversationModelsResponse],
    )
    if resp is None:
        return "Failed to get conversation models"
    if resp.code != ErrorCode.SUCCESS.code:
        return "Failed to get conversation models"
    if resp.data is None:
        return "No conversation models found"
    return resp.data.model_dump()
