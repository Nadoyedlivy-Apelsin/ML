import openai
import os

with open('file_id.txt', 'r') as file:
    file_id = file.read()

# Установите ваш ключ API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.FineTuningJob.create(
    training_file = file_id,
    model = 'gpt-3.5-turbo'
)

job_id = response['id']
print(job_id)

