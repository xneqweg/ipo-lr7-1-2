import json
with open('dump.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
num = input("Введите номер квалификации: ")
def findskills():
    for item in data:
        if item['model'] == 'data.skill' and item['fields']['code'].startswith(num):
            print(f"{item['fields']['code']} >> {item['fields']['title']}")
if findskills:
    print("\n==================== Найдено ====================")
    findskills()
else:
    print("==================== Не найдено ====================")