import vk_api
import data
import time
import json


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
            get_button(label="Кнопка 1", color="positive"),
            get_button(label="Кнопка 2", color="negative"),
            get_button(label="Кнопка 3", color="primary"),
            get_button(label="Кнопка 4", color="default"),
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
        if body.lower() == "привет":
            send_msg(user_id, "Здарова")
        else:
            send_msg(user_id, "Я тебя не понял")
    time.sleep(1)



