chat_history = {}

def add_user_message(user_id: int, text: str):
    if user_id not in chat_history:
        chat_history[user_id] = []
    chat_history[user_id].append({"role": "user", "content": text})
    return chat_history[user_id]

def add_bot_message(user_id: int, text: str):
    chat_history[user_id].append({"role": "assistant", "content": text})
    return chat_history[user_id]

def get_history(user_id: int):
    return chat_history.get(user_id, [])
