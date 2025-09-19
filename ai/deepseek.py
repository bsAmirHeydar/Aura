# import requests
# def ask_deepseek(system_role, context, user_query, model="tinyllama"):
#     url = "http://localhost:11434/api/generate"
    
#     prompt = f"""
# [System Role]
# {system_role}

# [Context]
# {context}

# [User]
# {user_query}
# """
#     payload = {
#         "model": model,
#         "prompt": prompt,
#         "stream": False
#     }

#     r = requests.post(url, json=payload, timeout=None)
#     r.raise_for_status()
#     return r.json()["response"]


import requests
from ai.memory import add_user_message, add_bot_message, get_history
from ai.rag import RAG
import yaml

# تنظیمات
with open("configs/settings.yaml", "r", encoding="utf-8") as f:
    settings = yaml.safe_load(f)

SYSTEM_ROLE = settings.get("system_role", "You are a helpful assistant.")
DEFAULT_MODEL = settings.get("model", "tinyllama")

# ساخت یک RAG برای همه‌ی فایل‌های پوشه data
rag = RAG(folder_path="data")

def ask_deepseek(user_id: int, user_text: str, model: str = DEFAULT_MODEL):
    # پیام کاربر → تاریخچه
    add_user_message(user_id, user_text)

    # جستجو در همه‌ی فایل‌های پوشه data
    context = "\n".join(rag.search(user_text, k=3))

    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": f"{SYSTEM_ROLE}\n\nاطلاعات:\n{context}"},
            *get_history(user_id)
        ],
        "stream": False
    }

    r = requests.post(url, json=payload, timeout=None)
    r.raise_for_status()
    response = r.json()["message"]["content"]

    # ذخیره جواب در تاریخچه
    add_bot_message(user_id, response)
    return response
