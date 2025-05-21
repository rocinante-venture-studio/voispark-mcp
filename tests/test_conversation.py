import unittest
from app.api.conversation import get_conversation_models
from app.msg.conversation_msg import ConversationModelsResponse


class TestConversation(unittest.IsolatedAsyncioTestCase):
    async def test_get_models(self):
        resp = await get_conversation_models()
        self.assertIsInstance(resp, dict)
        resp = ConversationModelsResponse.model_validate(resp)
        self.assertIsInstance(resp, ConversationModelsResponse)
