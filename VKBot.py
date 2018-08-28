import vk_api
import data
import time
import json
import datetime

vk = vk_api.VkApi(token=data.key)


def send_msg(peer_id, text):
    vk.method("messages.send", {'peer_id': peer_id, 'message': text})


def send_keyboard(peer_id, text, keyboard):
    vk.method("messages.send", {'peer_id': peer_id, 'message': text, 'keyboard': keyboard})


def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


keyboard = {
    "one_time": True,
    "buttons": [
        [
            get_button(label="Время", color="positive"),
            get_button(label="Дата", color="negative")
        ]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


while True:
    # главный цикл
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages["count"] >= 1:
        user_id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        text = ""
        if body.lower() == "клавиатура":
            send_keyboard(user_id, "Выберите нужный вариант", keyboard)
        elif body.lower() == "время":
            now = datetime.datetime.now()
            text = "Текущее время: "+now.strftime("%H:%M")
        elif body.lower() == "дата":
            now = datetime.datetime.now()
            text = "Текущая дата: " + now.strftime("%d-%m-%Y")
        else:
            text = "Я тебя не понял";
        send_msg(user_id, text)
    time.sleep(1)



