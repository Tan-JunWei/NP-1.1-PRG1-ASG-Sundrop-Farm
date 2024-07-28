import tkinter as tk
from tkinter import scrolledtext
import openai

client = openai.OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="sk-no-key-required"
)

def send_message():
    user_message = entry.get()
    if user_message.strip() == "":
        return
    
    chat_history.insert(tk.END, "You: " + user_message + "\n")
    chat_history.yview(tk.END)
    entry.delete(0, tk.END)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_message = response.choices[0].message.content
    chat_history.insert(tk.END, "Chatbot: " + bot_message[:-4] + "\n")
    chat_history.yview(tk.END)

root = tk.Tk()
root.title("Chatbot Client")

title = tk.Label(root, text="Chatbot Client")
title.pack(padx=10, pady=10)

chat_history = scrolledtext.ScrolledText(root, wrap = tk.WORD, width=60, height=20, state='normal')
chat_history.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60)
entry.pack(padx=10, pady=10, side=tk.LEFT)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

root.mainloop()
