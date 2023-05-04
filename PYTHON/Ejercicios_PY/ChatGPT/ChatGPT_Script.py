import sys
import config
import openai

openai.api_key = config.api_key

while True:
    prompt = input("\nHaz una pregunta: ")
    if prompt == "salir":
        break
    pregunta = openai.Completion.create(engine = "text-davinci-003",
                            prompt = prompt,
                            n = 1, 
                            max_tokens = 2000
    )
    print(pregunta.choices[0].text)
    



