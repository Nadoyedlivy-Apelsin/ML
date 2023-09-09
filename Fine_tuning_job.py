import openai

with open('api_key_open_ai.txt', 'r') as file:
    file_contents_1 = file.read()

with open('file_id.txt', 'r') as file:
    file_id = file.read()

api_key = file_contents_1
openai.api_key = api_key

response = openai.FineTuningJob.create(
    training_file = file_id,
    model = 'gpt-3.5-turbo'
)

job_id = response['id']
print(job_id)

