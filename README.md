# Luminary Python Wrapper Documentation

This document describes the Luminary Python wrapper, designed for interacting with a local AI server (based on the Open Web UI).

## Overview

The wrapper simplifies the process of sending prompts to a local AI model and receiving responses. It leverages the `requests` library for making HTTP requests and includes functionality to manage the default AI model.

## Core Components

*   **`prompt(prompt, token, api_server, model (optional), defaultPrompt(optional) )`**:  This function sends a prompt to the AI server and returns the response.
    *   `prompt`: The user's input prompt.
    *   `token`: Your API token (obtained from the Open Web UI settings).
    *   `api_server`: The URL of the AI server.
    *   `model`:  (Optional) The name of the AI model to use. If not provided, it defaults to the `CURRENT_MODEL`.
    *   `defaultPrompt`: (Optional) A default prompt to prepend to the user's prompt.
 
     **`setDefaultModel(defaultModel)`**: This function changes the default AI model used by the wrapper.
    *   `defaultModel`: The name of the new default AI model.

## Usage Example
import luminary

# Replace with your actual token and API server address
token = "sk-09d6492196554b29b94940674f90ab73"
api_server = "http://192.168.50.39:8080/api/chat/completions" **Might not be port 8080**

# Send the prompt to the AI server using the default model
response = luminary.prompt(user_input, token, api_server, "gemma3:1b", "THIS IS ADDED AUTOATICALLY: USER PROMPT:")

# Change the default model
luminary.setDefaultModel("phi4-14b")

print(response)
