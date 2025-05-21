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

## Getting Started

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <your-repository-url> # Replace with your repo URL
    cd voispark_mcp
    ```

2.  **Set up Python Environment and Install Dependencies:**
    This project uses `uv` for dependency management.
    ```bash
    python -m venv .venv # Create a virtual environment (recommended)
    source .venv/bin/activate # On Windows: .\.venv\Scripts\activate
    uv pip install -e . # Install the package and its dependencies in editable mode
    ```

3.  **Configure Voispark API Key:**
    Create a `.env` file in the root of this repository (i.e., next to `pyproject.toml`).
    Add your Voispark API key to this file:
    ```env
    VOISPARK_API_KEY="your_actual_api_key_here"
    ```
    The server will load this key to authenticate with Voispark services. Your `app/main.py` (or equivalent) should be configured to load this (e.g., using `python-dotenv`).

## Usage with Client Applications (e.g., Claude Desktop)

To integrate this server with a client application, configure the client to run this MCP server.

### Using `uv` (recommended for local development)

Add the following to your client's server configuration (e.g., `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "voispark": {
      "command": "uv",
      "args": [
        "run", // uv run will execute the script defined in pyproject.toml
        "voispark_mcp" // This is the script name from [project.scripts]
        // If your server needs to load .env from current dir, ensure `uv run` executes in project root
        // Alternatively, if your script (app/main.py) loads .env relative to itself, this should be fine.
        // You can pass additional arguments your server accepts after "voispark_mcp"
      ],
      "env": {
        // VOISPARK_API_KEY will be loaded from the .env file by the voispark_mcp script
        // If .env is not in the execution directory, you might need to set it explicitly here or ensure your script finds it.
      },
      "working_directory": "/path/to/your/voispark_mcp" // Set this to the root of your voispark_mcp project
    }
  }
}
```
**Note:** Ensure the `working_directory` points to the root of your `voispark_mcp` project so that it can find the `.env` file and any relative paths correctly.

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
    // "inputs": [ // If your server takes dynamic inputs like db_path
    //   {
    //     "type": "promptString",
    //     "id": "api_key",
    //     "description": "Voispark API Key",
    //     "default": "${env:VOISPARK_API_KEY}" // Example: use environment variable
    //   }
    // ],
    "servers": {
      "voispark": {
        "command": "uvx", // uvx runs executables from the environment
        "args": [
          "voispark_mcp" // Script name from pyproject.toml
          // Add any arguments your server needs, e.g., "--api-key", "${input:api_key}"
        ],
        "env": {
          // Ensure VOISPARK_API_KEY is available if your script relies on it from os.environ
          // "VOISPARK_API_KEY": "${env:VOISPARK_API_KEY}" // Redundant if .env is loaded by script
        }
        // "cwd": "${workspaceFolder}" // Ensures .env is found if loaded relative to cwd
      }
    }
  }
}
```

**Note for VS Code**: For API keys, it's often better to use VS Code's environment variable substitution (`${env:YOUR_ENV_VARIABLE}`) or input prompts, rather than hardcoding keys into `settings.json`. Ensure your Voispark server script (`app/main.py`) correctly loads the `VOISPARK_API_KEY` (e.g., from an `.env` file or environment variables).

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
mcp dev app.main:main # Assuming 'main' is the FastAPI app instance or wrapper function
```
Adjust `app.main:main` if your ASGI app instance or MCP-compatible wrapper function is named differently or located elsewhere. This command should be run from the root of your `voispark_mcp` project.

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the `LICENSE` file if one exists in the project repository.