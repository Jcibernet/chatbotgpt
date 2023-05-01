import openai
import config


openai.api_key = config.api_key

#Context of the role of chatgpt
messages = [{"role": "system", 
            "content": "sos un data engineer experto en python"}]

while True:

    content = input("Sobre qué quieres hablar?")

    if content == "exit":
        break

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.crgiteate(model="gpt-3.5-turbo", messages=messages)

