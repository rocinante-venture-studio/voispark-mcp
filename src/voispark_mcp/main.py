from contextlib import asynccontextmanager
from dataclasses import dataclass
import logging
from typing import AsyncIterator, Literal, Union
from mcp.server.fastmcp import FastMCP

from voispark_mcp.api.conversation import (
    get_conversation_models as _get_conversation_models,
    generate_conversation as _generate_conversation,
    get_speaker_details as _get_speaker_details,
    get_speakers as _get_speakers,
)
from voispark_mcp.api.tts import get_tts_models as _get_tts_models
from voispark_mcp.api.tts import generate_tts as _generate_tts
from voispark_mcp.api.voice_clone import (
    get_voice_clone_models as _get_voice_clone_models,
    clone_voice as _clone_voice,
)
from voispark_mcp.api.voice_changer import (
    get_voice_changer_models as _get_voice_changer_models,
    change_voice as _change_voice,
)
from voispark_mcp.api.voices import list_all_voices as _list_all_voices
from voispark_mcp.api.voices import get_providers as _get_providers
from voispark_mcp.api.history import (
    get_history_list as _get_history_list,
    get_history as _get_history,
)
from voispark_mcp.msg.conversation_msg import (
    GenerateConversationRequest,
    ConversationTurn,
    SpeakerConfigItem,
)
from voispark_mcp.msg.tts_msg import GenerateTTSRequest
from voispark_mcp.msg.voice_changer_msg import ChangeVoiceRequest
from voispark_mcp.msg.voice_clone_msg import (
    CartesiaVoiceCloneConfig,
    CloneVoiceRequest,
    MiniMaxVoiceCloneConfig,
)


@dataclass
class AppContext:
    pass


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context"""
    # Initialize on startup
    logging.info("Starting MCP server")
    try:
        yield AppContext()
    finally:
        # Cleanup on shutdown
        logging.info("Shutting down MCP server")


# Create an MCP server
mcp = FastMCP("Demo", lifespan=app_lifespan)


# -*- conversation -*-


@mcp.resource(uri="conversation://models")
async def get_conversation_models() -> str | dict:
    """
    Get all conversation models
    """
    return await _get_conversation_models()


@mcp.tool()
async def generate_conversation(
    provider: str,
    conversation: list[ConversationTurn],
    speaker: list[SpeakerConfigItem],
) -> str | dict:
    """
    Generate conversation
    """
    request = GenerateConversationRequest(provider="", conversation=[], speaker=[])
    return await _generate_conversation(request)


@mcp.tool()
async def get_speaker_details(speaker_id: str) -> str | dict:
    """
    Get speaker details
    """
    return await _get_speaker_details(speaker_id)


@mcp.tool()
async def get_speakers() -> str | dict:
    """
    Get speakers
    """
    return await _get_speakers()


# -*- text_to_speech -*-


@mcp.resource(uri="textToSpeech://models")
async def get_tts_models() -> str | dict:
    """
    Get all TTS models
    """
    return await _get_tts_models()


@mcp.tool()
async def generate_tts(
    provider: str,
    text: str,
    model_id: str,
    voice_id: str,
) -> str | dict:
    """
    Generate TTS
    """
    request = GenerateTTSRequest(
        provider=provider,
        text=text,
        model_id=model_id,
        voice_id=voice_id,
    )
    return await _generate_tts(request)


# -*- voice_changer -*-


@mcp.resource(uri="voiceChanger://models")
async def get_voice_changer_models() -> str | dict:
    """
    Get all voice changer models
    """
    return await _get_voice_changer_models()


@mcp.tool()
async def change_voice(
    provider: str,
    model_id: str,
    voice_id: str,
    audio_data: str,
) -> str | dict:
    """
    Change voice
    """
    request = ChangeVoiceRequest(
        provider=provider,
        model_id=model_id,
        voice_id=voice_id,
        audio_data=audio_data,
    )
    return await _change_voice(request)


# -*- voice_clone -*-


@mcp.resource(uri="voiceClone://models")
async def get_voice_clone_models() -> str | dict:
    """
    Get all voice clone models
    """
    return await _get_voice_clone_models()


@mcp.tool()
async def clone_voice(
    provider: str,
    model_id: str,
    audio_data: str,
    configs: Union[CartesiaVoiceCloneConfig, MiniMaxVoiceCloneConfig],
) -> str | dict:
    """
    Clone voice
    """
    request = CloneVoiceRequest(
        provider=provider, model_id=model_id, audio_data=audio_data, configs=configs
    )
    return await _clone_voice(request)


# -*- voices -*-


@mcp.resource(uri="voices://providers")
async def get_providers() -> str | dict:
    """
    Get all voice providers
    """
    return await _get_providers()


@mcp.resource(uri="voices://{provider_id}/{voice_type}/list")
async def list_all_voices(provider_id: str, voice_type: str) -> str | dict:
    """
    List all voices
    """
    return await _list_all_voices(provider_id, voice_type)


# -*- history -*-


@mcp.resource(uri="history://list")
async def get_history_list(
    source: Literal["tts", "voice_changer", "conversation"] = "tts",
) -> str | dict:
    """
    Get history list
    """
    return await _get_history_list(source)


@mcp.resource(uri="history://{history_id}")
async def get_history(history_id: str) -> str | dict:
    """
    Get history
    """
    return await _get_history(history_id)


def main():
    """Entry point for the voispark_mcp command."""
    mcp.run()
