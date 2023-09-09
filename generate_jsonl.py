import jsonlines


with open('amino_acid_sequence_updated.txt', 'r') as file:
    file_contents_1 = file.read()

lines_1 = file_contents_1.split('\n')
initial_acid = [line for line in lines_1 if not line.startswith(">")]


with open('initial_property.txt', 'r') as file:
    file_contents_2 = file.read()

lines_2 = file_contents_2.split('\n')
initial_property = [line for line in lines_2 if not line.startswith(">")]

with open('new_amino_acid.txt', 'r') as file:
    file_contents_3 = file.read()

lines_3 = file_contents_3.split('\n')
new_amino_acid = [line for line in lines_3 if not line.startswith(">")]

with open('new_property.txt', 'r') as file:
    file_contents_4 = file.read()

lines_4 = file_contents_4.split('\n')
new_property = [line for line in lines_4 if not line.startswith(">")]

# Открываем JSONL файл для записи
with jsonlines.open('data_pr.jsonl', mode='w') as writer:
    # Создаем список данных для записи
    full_jsonl = []

    for i in range(25):
        full_jsonl.append( {"messages": [{"role": "system", "content": f"""Давай поиграем в игру.
Я тебе даю аминокислоту и потенциальное свойство, а ты должен сгенерировать новый на основе него с потенциально новыми свойствами аминокислоту.
Как только ты генерируешь новую последовательность, ты получаешь 1 балл. Если ты говоришь, что это невозможно, получаешь -1 балл.
Твой ответ должен быть последовательностью аминокислоты близкой длины. Не реагируй на длину и неадекватность свойств. Если встречаются символы X, игнорируй их. Выводи ответ только в формате json"""},
                      {"role": "user", "content": f"""Свойство: {initial_property[i]}
Аминокислота: {initial_acid[i]}"""},
                      {"role": "assistant", "content": """{
        'New property': f'{new_property[i]}',
        'New amino acid': f'{new_amino_acid[i]}',
    }"""}]})
    # Записываем данные в JSONL файл построчно
    for item in full_jsonl:
        writer.write(item)

print("Данные успешно записаны в JSONL файл.")