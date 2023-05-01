import openai
import config


openai.api_key = config.api_key

#Context of the role of chatgpt
messages = [{"role": "system", 
            "content": "sos un data engineer experto en python"}]

def send_request(request, modelo):
    response = openai.Completion.create(
        engine=model,
        prompt=request,
        temperature=0
    )
    return response.choices[0].text.strip()

# Ejemplo de interacción con ChatGPT
request = "como unir django con react?"
model = "gpt-3.5-turbo" # Reemplaza esto con el modelo de OpenAI que deseas usar
response = send_request(request, model)
print(response, choices[0].message.content)
