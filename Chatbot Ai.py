import customtkinter as ctk

# === Configuration UI ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("520x620")
app.title("💬 ChatBot Stylé")

# === Titre principal ===
title_label = ctk.CTkLabel(
    app, text="🤖 ChatBot Stylé", font=("Arial", 24, "bold"), text_color="#00ace6"
)
title_label.pack(pady=15)

# === Zone de texte (affichage messages) ===
chat_frame = ctk.CTkFrame(app)
chat_frame.pack(padx=10, pady=5, fill="both", expand=True)

chat_display = ctk.CTkTextbox(chat_frame, wrap="word", font=("Arial", 14))
chat_display.pack(padx=10, pady=10, fill="both", expand=True)
chat_display.insert("end", "🤖 Bot : Bonjour ! Je suis prêt à discuter 💬\n\n")
chat_display.configure(state="disabled")

# === Frame d'entrée utilisateur ===
entry_frame = ctk.CTkFrame(app)
entry_frame.pack(pady=10)

user_input = ctk.CTkEntry(
    entry_frame, width=360, font=("Arial", 14), placeholder_text="Tapez un message ici..."
)
user_input.grid(row=0, column=0, padx=5)

# === Réponses prédéfinies ===
responses = {
    "bonjour": "Salut ! Comment puis-je t’aider ? 😊",
    "merci": "Avec plaisir ! 🙌",
    "au revoir": "À bientôt ! 👋",
    "ton nom": "Je suis BotStylé, enchanté ! 🤖",
    "comment tu vas": "Je vais super bien, merci ! Et toi ?",
    "qui es tu": "Je suis un chatbot écrit en Python avec du style 😎",
}

# === Fonction de réponse ===
def send_message():
    msg = user_input.get().lower().strip()
    if not msg:
        return

    response = responses.get(msg, "😕 Je ne comprends pas encore cette question.")

    chat_display.configure(state="normal")
    chat_display.insert("end", f"👤 Vous : {msg}\n", "user")
    chat_display.insert("end", f"🤖 Bot : {response}\n\n", "bot")
    chat_display.configure(state="disabled")
    chat_display.see("end")
    user_input.delete(0, "end")

# === Bouton envoyer ===
send_button = ctk.CTkButton(entry_frame, text="Envoyer", command=send_message)
send_button.grid(row=0, column=1, padx=5)

app.mainloop()
