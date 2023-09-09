import os
import openai

# Установите ваш ключ API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.File.create(
  file=open("data_pr.jsonl", "rb"),
  purpose='fine-tune'
)

file_id = response['id']
print(f'{file_id}')
