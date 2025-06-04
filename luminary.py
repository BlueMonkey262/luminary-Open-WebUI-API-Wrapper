import requests

CURRENT_MODEL = "gemma3:1b" #the default model to use, can be changed during run with luminary.changeDefaultModel(model)

def prompt(prompt, token, api_server, model=None, defaultPrompt=""):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    if model is None:
        model = CURRENT_MODEL  #use default model if not provided

    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": defaultPrompt + prompt
            }
        ]
    }

    try:
        response = requests.post(api_server, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except (KeyError, IndexError):
        return "Error: Unexpected response format"

def setDefaultModel(defaultModel):
    global CURRENT_MODEL
    CURRENT_MODEL = defaultModel
    print(f"Default model changed to: {CURRENT_MODEL}")
