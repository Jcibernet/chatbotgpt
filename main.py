import openai

import config


openai.api_key = config.api_key
model = "text-davinci-002"

context = [
    {"role": "system", "content": "Bienvenido a ChatGPT. ¿En qué puedo ayudarte?"}
]

def chat_with_gpt(prompt):
    context.append({"role": "user", "content": prompt})

    response = openai.Completion.create(
        engine=model,
        prompt="\n".join([f"{message['role']}: {message['content']}" for message in context]),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = response.choices[0].text.strip()
    context.append({"role": "system", "content": message})

    return message

if __name__ == "__main__":
    while True:
        prompt = input("What do you want to know (or 'exit' to finish the query): ")
        if prompt.lower() == "exit":
            break
        response = chat_with_gpt(prompt)
        print(f"ChatGPT: {response}")