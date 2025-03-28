import tkinter as tk
from tkinter import ttk, messagebox
import random

# Quizfragen und Antworten
quiz_fragen = [
    {
        "frage": "Was bewirkt wrap='none' in einem Tkinter Text-Widget?",
        "optionen": ["A) Aktiviert automatische Zeilenumbrüche", "B) Deaktiviert automatische Zeilenumbrüche", "C) Ermöglicht Umbruch bei Leerzeichen", "D) Schneidet Text am Rand ab"],
        "antwort": "B"
    },
    {
        "frage": "Welches Modul wird für QR-Codes in Python verwendet?",
        "optionen": ["A) qrtools", "B) qrcode", "C) pyqrcode", "D) barcode"],
        "antwort": "C"
    },
    {
        "frage": "Welche Funktion speichert ein QR-Code als PNG?",
        "optionen": ["A) qr.save()", "B) qr.generate()", "C) qr.png()", "D) qr.export()"],
        "antwort": "C"
    },
    {
        "frage": "Welches Widget wird für Scrollbars in Tkinter verwendet?",
        "optionen": ["A) ScrollFrame", "B) ttk.Scroll", "C) tk.Scrollbar", "D) tk.Scroll"],
        "antwort": "C"
    },
        {
        "frage": "Wie fängt man alle Exceptions in Python?",
        "optionen": ["A) try:", "B) except Exception:", "C) catch:", "D) finally:"],
        "antwort": "B"
    },
    {
        "frage": "Welche Methode wird verwendet, um eine Liste in Python umzukehren?",
        "optionen": ["A) list.reverse()", "B) list.flip()", "C) list.invert()", "D) list.sort(reverse=True)"],
        "antwort": "A"
    },
    {
        "frage": "Welches Modul wird für HTTP-Anfragen in Python verwendet?",
        "optionen": ["A) http", "B) requests", "C) urllib", "D) socket"],
        "antwort": "B"
    },
    {
        "frage": "Was ist der Output von 'Hello' + 3 in Python?",
        "optionen": ["A) 'Hello3'", "B) TypeError", "C) 'HelloHelloHello'", "D) '3Hello'"],
        "antwort": "B"
    },
    {
        "frage": "Wie importiert man eine Funktion aus einem Modul?",
        "optionen": ["A) import function from module", "B) from module import function", "C) include module.function", "D) using module.function"],
        "antwort": "B"
    },
    {
        "frage": "Was macht die 'with'-Anweisung in Python?",
        "optionen": ["A) Erstellt einen Context Manager", "B) Definiert einen Codeblock", "C) Importiert mehrere Module", "D) Führt parallele Ausführung durch"],
        "antwort": "A"
    },
]

# Initialisierung der App
root = tk.Tk()
root.title("Python Quiz")
root.geometry("500x400")

# Punkte-Tracker
punkte = 0
frage_index = 0
ausgewählte_fragen = random.sample(quiz_fragen, len(quiz_fragen))  # Fragen mischen

def überprüfe_antwort(auswahl):
    global frage_index, punkte
    richtige_antwort = ausgewählte_fragen[frage_index]["antwort"]
    
    if auswahl == richtige_antwort:
        punkte += 1
        messagebox.showinfo("Ergebnis", "✅ Richtig!")
    else:
        messagebox.showerror("Ergebnis", f"❌ Falsch! Richtige Antwort: {richtige_antwort}")
    
    frage_index += 1
    if frage_index < len(ausgewählte_fragen):
        lade_frage()
    else:
        messagebox.showinfo("Quiz beendet", f"Dein Punktestand: {punkte}/{len(quiz_fragen)}")
        root.quit()

def lade_frage():
    frage = ausgewählte_fragen[frage_index]
    frage_label.config(text=frage["frage"])

    for i in range(4):
        buttons[i].config(text=frage["optionen"][i], command=lambda opt=chr(65+i): überprüfe_antwort(opt))

# UI-Elemente
frage_label = ttk.Label(root, text="", font=("Arial", 14), wraplength=450)
frage_label.pack(pady=20)

buttons = []
for i in range(4):
    btn = ttk.Button(root, text="", width=40)
    btn.pack(pady=5)
    buttons.append(btn)

# Erste Frage laden
lade_frage()

# App starten
root.mainloop()
