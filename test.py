import luminary
import time

#

#------------------------------------------------------------------------------------------------------#
#local_ai_api(prompt, token, api_server, model, descriptionPrompt)
#model is NOT required if not provided it defaults to gemma3:4b, edit luminary.py to change the default.
#The default prompt argument places

#------------------------------------------------------------------------------------------------------#

token = "sk-09d6492196554b29b94940674f90ab73" #your api token, get this from clicking on your user in the bottom left, settings > account > api keys
api_server = "http://192.168.50.39:8080/api/chat/completions" #set this to the server where open web-ui is installed. May not be port 8080, localhost is fine too.

userInput = input()

print(luminary.prompt(userInput, token, api_server, "gemma3:1b", "THIS IS ADDED AUTOATICALLY: USER PROMPT:"))