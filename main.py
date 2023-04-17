from flask import Flask, render_template, request
import json
from datetime import datetime


# загрузить сообщения из файла
def load_message():
    with open('db.json', 'r') as json_file:  # чтение файла через контекстный менеджер и сохраняем в переменную
        data = json.load(json_file)  # пересохранение файла для питона
    return data['messages']


# функция для добавления новых сообщений
def add_message(sender, text):
    new_message = {  # создили словарь, где есть тект, имя отправителя и время
        'text': text,
        'sender': sender,
        'time': datetime.now().strftime('%H:%M')
    }
    all_messages.append(new_message)


# функция для сохраниение в файл
def save_messages():
    data = {
        'messages': all_messages
    }
    with open('db.json', 'w') as json_file: # режим редактирования
        json.dump(data, json_file)

all_messages = load_message()

app = Flask(__name__)  # создаем новое приложение


@app.route('/index')  # http://127.0.0.1/index создаем декоратор который по адресу возвращает тект из return
def index_pade():
    return 'Hello World!'


@app.route('/chat')
def display_chat():
    return render_template('form.html')


@app.route('/get_messages')
def get_messages():
    return {'messages': all_messages}

@app.route('/send_message')
def send_message():
    sender = request.args['name']
    text = request.args['text']
    add_message(sender, text)
    save_messages()
    return 'Ok'

app.run(host='0.0.0.0', port=80)  # строчка запуска сервера
