import requests

name = input("Введите ваше имя: \n")

while True:
    text = input("Введите текст: \n")
    response = requests.post('http://127.0.0.1:5000/send',
                             json={'name': name, 'text': text})