import openai
import tkinter as tk

# Klucz API OpenAI
openai.api_key = 'your api key'

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response.choices[0].message['content'].strip()

def send_message():
    user_message = user_input.get("1.0", tk.END).strip()
    if user_message:
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, "Ty: " + user_message + "\n")
        chat_history.config(state=tk.DISABLED)

        response = get_openai_response(user_message)
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, "Chatbot: " + response + "\n")
        chat_history.config(state=tk.DISABLED)

        user_input.delete("1.0", tk.END)

root = tk.Tk()
root.title("Chatbot OpenAI")

chat_history = tk.Text(root, state=tk.DISABLED, width=80, height=20)
chat_history.pack()

user_input = tk.Text(root, height=3, width=80)
user_input.pack()

send_button = tk.Button(root, text="Wyślij", command=send_message)
send_button.pack()

root.mainloop()
