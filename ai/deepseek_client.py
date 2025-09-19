import requests

def call_deepseek(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "deepseek-r1:7b",
        "prompt": prompt,
        "stream": False
    }

    try:
        r = requests.post(url, json=data, timeout=60)
        r.raise_for_status()
        full_text = r.json().get("response", "")
        # بخش <think>...</think> رو حذف کنیم
        if "</think>" in full_text:
            full_text = full_text.split("</think>")[-1].strip()
        return full_text or "⚠️ پاسخی از مدل دریافت نشد."
    except Exception as e:
        return f"⚠️ خطای غیرمنتظره: {e}"
