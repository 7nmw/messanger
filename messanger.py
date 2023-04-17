import datetime as dt

guest_list= ['Ola', 'Max', 'Ignat']

def print_mes(sample_list):
    for i in sample_list:
        print(i, ', Come in')
print_mes(guest_list)

all_mesages = []

def add_message(sender, text):
    #функция добавления сообщения
    new_message = {
        'sender': sender,
        'text': text,
        'time': dt.datetime.now()
    }
    all_mesages.append(new_message) #добавляем значения

def print_all_messages(all_mesages):
    #функция выводит на печать сообщения
    for msg in all_mesages:
        print(msg['sender'], ']:', msg['text'], '|Time:', msg['time'])
add_message('Valg', 'Hi')