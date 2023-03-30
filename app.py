import openai
import config

openai.api_key=config.OPENAI_API_KEY

prompt = input("Enter your prompt: ")

resp = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=100
)
print(resp.choices[0].text)


