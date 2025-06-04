# Luminary Python Wrapper Documentation

A Open WebUI API Wrapper: Cleans up the Open WebUI api, making it easier to use.


## Overview

The wrapper simplifies the process of sending prompts to a local AI model and receiving responses. It leverages the `requests` library for making HTTP requests and includes functionality to manage the default AI model.

## Core Components

*   **`prompt(prompt, token, api_server, model (optional), defaultPrompt(optional) )`**:  This function sends a prompt to the AI server and returns the response.
    *   `prompt`: The user's input prompt.
    *   `token`: Your API token (obtained from the Open Web UI settings).
    *   `api_server`: The URL of the AI server.
    *   `model`:  (Optional) The name of the AI model to use. If not provided, it defaults to the `CURRENT_MODEL`, set to gemma3:4b.
    *   `defaultPrompt`: (Optional) A default prompt to prepend to the user's prompt.
 
     **`setDefaultModel(defaultModel)`**: This function changes the default AI model used by the wrapper.
    *   `defaultModel`: The name of the new default AI model.

## Usage Example

# Replace with your actual token and API server address
token = "sk-09d6492196554b29b94940674f90ab73" **your api token, get this from clicking on your user in the bottom left, settings > account > api keys**
api_server = "http://192.168.50.39:8080/api/chat/completions" **Might not be port 8080**

# Send the prompt to the AI server using the default model
response = luminary.prompt(user_input, token, api_server, "gemma3:1b", "Make sure to greet the user")

print(response)

# Change the default model
luminary.setDefaultModel("phi4-14b")
