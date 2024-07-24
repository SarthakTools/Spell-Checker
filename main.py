from customtkinter import *
from textblob import TextBlob
import cProfile, threading, os
from PIL import Image

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
spell_checker_img = CTkImage(Image.open(os.path.join(image_path, "spell_checker.png")), size=(40, 40))

class App(CTkFrame):
    def __init__(self, parent):
        self.parent = parent
        self.setup_widgets()
        self.bind_them()

    def setup_widgets(self):
        self.frame = CTkFrame(self.parent, fg_color="transparent")

        CTkLabel(self.frame, text="Spell Checker", font=("Canbera", 30, "bold"), text_color="white", image=spell_checker_img, compound=LEFT).pack(side=TOP, anchor="nw", padx=50, pady=20)

        self.message_text = CTkLabel(self.frame, text="Type a sentence to check its accuracy", font=("Poppins", 20, "bold"))
        self.message_text.pack(side=TOP, anchor="nw", padx=50, pady=10)

        self.sentence_entry = CTkEntry(self.frame, font=("Verdana", 15, "normal"), text_color="white", placeholder_text="Type your sentence here ...", border_color="#111")
        self.sentence_entry.pack(side=TOP, fill=X, ipady=10, padx=50, pady=0)

        CTkButton(self.frame, text="Correct", font=("Corbel", 22), width=0, command=lambda : threading.Thread(target=self.correct_sentence).start()).pack(side=TOP, anchor="nw", padx=50, pady=10, ipadx=20, ipady=3)

        self.frame.pack(side=TOP, fill=BOTH, expand=True, padx=60, pady=40)

    def bind_them(self):
        self.sentence_entry.bind("<KeyRelease>", self.validate_sent)

    def validate_sent(self, *_):
        sentence = self.sentence_entry.get().strip()
        correct_sentence = TextBlob(sentence).correct()
        if len(sentence) == 0:
            self.sentence_entry.configure(border_width=2, border_color="#b5314a")

        elif sentence == correct_sentence:
            self.sentence_entry.configure(border_width=2, border_color="#4187AA")
        else:
            self.sentence_entry.configure(border_width=2, border_color="#b5314a")

    def correct_sentence(self):
        sentence = self.sentence_entry.get()
        blob = TextBlob(sentence)
        corrected_sentence = str(blob.correct())
        self.sentence_entry.delete(0, 'end')
        self.sentence_entry.insert(0, corrected_sentence)
        self.sentence_entry.configure(border_width=2, border_color="#4187AA")

set_appearance_mode("dark")
set_default_color_theme("blue")
root = CTk(fg_color="#111")
root.title("Spell Checker")
root.iconbitmap("spell_checker.ico")

app = App(root)

root.resizable(False, False)
root.geometry("800x450")

cProfile.run("root.mainloop()")