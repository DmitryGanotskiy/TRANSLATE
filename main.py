import tkinter as tk
from tkinter import ttk
from translate import Translator
from langdetect import detect


def on_click(event, text_widget, default_text):
    if text_widget.get("1.0", tk.END).strip() == default_text:
        text_widget.delete("1.0", tk.END)
        text_widget.config(fg="black")


def on_focus_out(event, text_widget, default_text):
    if not text_widget.get("1.0", tk.END).strip():
        text_widget.insert(tk.END, default_text)
        text_widget.config(fg="gray")


def translate_text():
    source_text = text_box_source.get("1.0", tk.END).strip()
    if not source_text:
        return

    source_language = detect(source_text)
    target_language = language_combobox.get()

    translator = Translator(from_lang=source_language, to_lang=target_language)
    translation = translator.translate(source_text)

    text_box_target.delete("1.0", tk.END)
    text_box_target.insert(tk.END, translation)


root = tk.Tk()
root.title("Simple Translator")
root.geometry("820x500")
root.resizable(False, False)

default_text_source = "Enter text here..."
default_text_target = "Translated text will appear here..."

text_box_source = tk.Text(root, height=15, width=35, font=("Arial", 14), fg="gray")
text_box_source.grid(row=0, column=0, padx=10, pady=10)
text_box_source.insert(tk.END, default_text_source)
text_box_source.bind("<FocusIn>", lambda event: on_click(event, text_box_source, default_text_source))
text_box_source.bind("<FocusOut>", lambda event: on_focus_out(event, text_box_source, default_text_source))

# Target Text Box
text_box_target = tk.Text(root, height=15, width=35, font=("Arial", 14), fg="gray")
text_box_target.grid(row=0, column=1, padx=10, pady=10)
text_box_target.insert(tk.END, default_text_target)
text_box_target.bind("<FocusIn>", lambda event: on_click(event, text_box_target, default_text_target))
text_box_target.bind("<FocusOut>", lambda event: on_focus_out(event, text_box_target, default_text_target))

# Language Selection Combobox
languages = ["en", "fr", "es", "de", "it", "ru", "zh", "ja"]  # Add more languages as needed
language_combobox = ttk.Combobox(root, values=languages, font=("Arial", 14))
language_combobox.grid(row=1, column=0, padx=10, pady=10)
language_combobox.set("en")  # Default to English

# Translate Button
translate_button = tk.Button(root, text="Translate", font=("Arial", 14), command=translate_text)
translate_button.grid(row=1, column=1, padx=10, pady=20)

#LOOP
root.mainloop()