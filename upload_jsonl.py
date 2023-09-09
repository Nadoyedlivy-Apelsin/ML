import os
import openai

with open('api_key_open_ai.txt', 'r') as file:
  api_key = file.read()

openai.api_key = api_key

response = openai.File.create(
  file=open("data_pr.jsonl", "rb"),
  purpose='fine-tune'
)

file_id = response['id']
print(f'{file_id}')