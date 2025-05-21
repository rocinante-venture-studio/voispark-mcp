# Voispark MCP Server

## Overview
A Model Context Protocol (MCP) server implementation for Voispark, enabling advanced AI-powered voice and language capabilities. This server allows interaction with Voispark services for tasks such as speech analysis, speech synthesis, and more.

## Components

### Resources
<!-- Describe resources like voispark://audio/<id>, voispark://models/<model_id> -->

### Prompts
<!-- Describe any interactive prompts your server provides -->

### Tools
<!-- Describe tools like analyze_speech, generate_speech -->

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