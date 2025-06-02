# Voispark MCP Server

[![PyPI version](https://badge.fury.io/py/voispark-mcp.svg)](https://badge.fury.io/py/voispark-mcp)
[![Python Version](https://img.shields.io/pypi/pyversions/voispark-mcp.svg)](https://pypi.org/project/voispark-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/voispark-mcp)](https://pepy.tech/project/voispark-mcp)
[![GitHub Stars](https://img.shields.io/github/stars/rocinante-venture-studio/voispark-mcp.svg)](https://github.com/rocinante-venture-studio/voispark-mcp/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/rocinante-venture-studio/voispark-mcp.svg)](https://github.com/rocinante-venture-studio/voispark-mcp/issues)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue.svg)](https://modelcontextprotocol.io/)

## Overview
A Model Context Protocol (MCP) server implementation for Voispark, enabling advanced AI-powered voice and language capabilities. This server allows interaction with Voispark services for tasks such as speech analysis, speech synthesis, and more.

## API

### Resources

- `conversation://models`: Get all available conversation models and their parameters
- `conversation://speakers`: Get all available speakers for conversation generation
- `textToSpeech://models`: Get all available TTS models and their configurations
- `voiceChanger://models`: Get all available voice changer models and their configurations
- `voiceClone://models`: Get all available voice clone models and their configurations
- `voices://providers`: Get all available voice providers and their supported capabilities
- `voices://{provider_id}/{voice_type}/list`: List all available voices from a specific provider for a given voice type
- `history://list`: Get a list of historical tasks for a specific service type
- `history://{history_id}`: Get detailed information about a specific historical task

### Tools

- **generate_conversation**
  - Generate AI conversation with specified parameters
  - Inputs:
    - `provider` (string): The conversation provider obtained from 'conversation://models'
    - `conversation` (array): List of conversation turns defining the dialogue structure
    - `speaker` (array): List of speaker configurations obtained from 'conversation://speakers'
  - Prerequisites: Call 'conversation://models' and 'conversation://speakers' resources first

- **get_speaker_details**
  - Get detailed information about a specific speaker
  - Input: `speaker_id` (string): The unique identifier of the speaker
  - Prerequisites: Obtain speaker_id from 'conversation://speakers' resource first

- **generate_tts**
  - Generate TTS (Text-to-Speech) audio from text input
  - Inputs:
    - `provider` (string): TTS provider name obtained from 'textToSpeech://models'
    - `text` (string): The text content to convert to speech
    - `model_id` (string): The TTS model identifier from the provider's model list
    - `voice_id` (string): The voice identifier compatible with the selected provider and model
  - Prerequisites: Call 'textToSpeech://models' resource first

- **change_voice**
  - Transform an existing audio file to use a different voice
  - Inputs:
    - `provider` (string): Voice changer provider name obtained from 'voiceChanger://models'
    - `model_id` (string): The voice changer model identifier from the provider's model list
    - `voice_id` (string): The target voice identifier to transform the audio into
    - `audio_data` (string): Base64 encoded audio file to be transformed
  - Prerequisites: Call 'voiceChanger://models' resource first

- **clone_voice**
  - Clone a voice from an audio sample to create a new synthetic voice
  - Inputs:
    - `provider` (string): Voice clone provider name obtained from 'voiceClone://models'
    - `model_id` (string): The voice clone model identifier from the provider's model list
    - `audio_data` (string): Base64 encoded audio sample for voice cloning (recommended: 10-30 seconds of clean speech)
    - `configs` (object): Provider-specific configuration (CartesiaVoiceCloneConfig or MiniMaxVoiceCloneConfig)
  - Prerequisites: Call 'voiceClone://models' resource first

## Usage with Client Applications (e.g., Claude Desktop)

To integrate this server with a client application, configure the client to run this MCP server.

### Using `uv` (recommended for local development)

Add the following to your client's server configuration (e.g., `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "voispark": {
      "command": "uvx",
      "args": ["voispark_mcp"],
      "env": {
        "VOISPARK_API_KEY": "<YOUR_API_KEY>"
      }
    }
  }
}
```

## Usage with VS Code

For quick installation, you can adapt the VS Code MCP installation methods.
(The following are conceptual examples and would need actual redirect URLs for Voispark MCP if you create them.)

<!--
[![Install with UV in VS Code](https://img.shields.io/badge/VS_Code-UV-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](your-vscode-uv-install-url)
-->

For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code (`Ctrl + Shift + P` -> `Preferences: Open User Settings (JSON)`) or to a `.vscode/mcp.json` file in your workspace.

### Using `uvx` (for executing installed package)

```json

{
  "mcp": {
    "servers": {
      "voispark": {
        "command": "uvx",
        "args": ["voispark_mcp"],
        "env": {
        "VOISPARK_API_KEY": "<YOUR_API_KEY>"
        }
      }
    }
  }
}
```

## Building

### Local Package
Your package is built/installed when you run:
```bash
uv pip install -e .
```

## Test with MCP Inspector

Ensure you have `mcp[cli]` installed in your environment. You can add it with `uv pip install "mcp[cli]"`.

Run the MCP inspector pointing to your server's wrapper:
```bash
mcp dev app/main.py
```

## Contributing

We encourage contributions to help expand and improve voispark_mcp. Whether you want to add new time-related tools, enhance existing functionality, or improve documentation, your input is valuable.

For examples of other MCP servers and implementation patterns, see: https://github.com/modelcontextprotocol/servers

Pull requests are welcome! Feel free to contribute new ideas, bug fixes, or enhancements to make voispark_mcp even more powerful and useful.

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the `LICENSE` file if one exists in the project repository.