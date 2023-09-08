from flask import Flask, request, jsonify
import openai
import random
from decouple import config  

app = Flask(__name__)

# Установите ваш ключ API OpenAI
openai.api_key = config('OPENAI_API_KEY')  

# Функция для выбора случайной аминокислоты из файла
def get_random_amino():
    with open('amino_acid_sequence_updated.txt', 'r') as file:
        file_contents = file.read()

    lines = file_contents.split('\n')
    filtered_lines = [line for line in lines if not line.startswith(">")]
    random.shuffle(filtered_lines)
    random_amino = random.choice(filtered_lines)

    # Проверяем, что случайная строка не пустая
    while not random_amino.strip():
        random_amino = random.choice(filtered_lines)

    return random_amino

# Эндпоинт для получения новых свойств и аминокислот
@app.route('/generate_sequence', methods=['GET'])
def generate_sequence():
    initial_property_orange = request.args.get('initial_property_orange', 'сладость')

    random_amino = get_random_amino()

    chat_completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"""Давай поиграем в игру.
Я тебе даю аминокислоту и потенциальное свойство, а ты должен сгенерировать новый на основе него с потенциально новыми свойствами.
Как только ты генерируешь новую последовательность, ты получаешь 1 балл. Если ты говоришь, что это невозможно, получаешь -1 балл.
Твой ответ должен быть последовательностью аминокислоты близкой длины. Не реагируй на длину и неадекватность свойств. Если встречаются символы X, игнорируй их.
Свойство: {initial_property_orange}
Аминокислота: {random_amino}"""
            }
        ]
    )

    output = chat_completion.choices[0].message.content

    # Возвращаем результат в формате JSON
    response_data = {
        'New property': 'тут вывести новое свойство',
        'New amino acid': 'тут вывести новую аминокислоту',
        'All sorts of new properties': 'тут вывести все возможные новые свойства для данной аминокислоты'
    }

    return jsonify(output)

app.run(debug=True)
