import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askquestion
import random

window = tk.Tk()
window.geometry("300x200")
window.title("UTBK")
window.attributes("-fullscreen", True)

frames = [tk.Frame(window) for _ in range(5)]
for frame in frames:
    frame.pack_forget()
frames[0].pack(fill='both', expand=True)

for i, frame in enumerate(frames):
    judul = tk.Label(frame, text='PENALARAN MATEMATIKA',font=("Arial", 27))
    judul.pack(padx=20, pady=5,fill='x')
    judul.configure(bg='dark grey')
    label = tk.Label(frame, text=f"soal {i+1}",font=("Arial", 27))
    label.pack(padx=20, pady=5,anchor="nw")

button_frame = tk.Frame(window)
button_frame.pack(side="bottom", fill="x")

navigation_frame = tk.Frame(window)
navigation_frame.pack(side="bottom", fill="x")

class ExamModel:
    def __init__(self):
        self.username=['Alan','Nazril']
        self.password=['12345','56789']
        self.rn = random.sample(range(0, 5), 5)
        # soal 1
        self.soal1 = ttk.Label(frames[self.rn[0]],text="Himpunan Penyelesaian dari x²-2x-8=0 adalah:",font=("Arial", 20))
        self.jawaban1 = tk.StringVar(value="none")
        self.opsi1_soal1 = tk.Radiobutton(frames[self.rn[0]], text="(-2,4)", value='20', variable=self.jawaban1,font=("Arial", 20))
        self.opsi2_soal1 = tk.Radiobutton(frames[self.rn[0]], text="(4,8)", value='f1', variable=self.jawaban1,font=("Arial", 20))
        self.opsi3_soal1 = tk.Radiobutton(frames[self.rn[0]], text="(3,6)", value='f2', variable=self.jawaban1,font=("Arial", 20))
        self.opsi4_soal1 = tk.Radiobutton(frames[self.rn[0]], text="(21,-8)", value='f3', variable=self.jawaban1,font=("Arial", 20))

        # soal 2
        self.soal2 = ttk.Label(frames[self.rn[1]], text="Hasil dari 4 log 8 + 4 log 32 adalah:",font=("Arial", 20))
        self.jawaban2 = tk.StringVar(value="none")
        self.opsi1_soal2 = tk.Radiobutton(frames[self.rn[1]], text="5", value='f1', variable=self.jawaban2,font=("Arial", 20))
        self.opsi2_soal2 = tk.Radiobutton(frames[self.rn[1]], text="4", value='20', variable=self.jawaban2,font=("Arial", 20))
        self.opsi3_soal2 = tk.Radiobutton(frames[self.rn[1]], text="7", value='f2', variable=self.jawaban2,font=("Arial", 20))
        self.opsi4_soal2 = tk.Radiobutton(frames[self.rn[1]], text="3", value='f3', variable=self.jawaban2,font=("Arial", 20))
        
        # soal 3
        self.soal3 = ttk.Label(frames[self.rn[2]], text="Hasil dari 5!:",font=("Arial", 20))
        self.jawaban3 = tk.StringVar(value="none")
        self.opsi1_soal3 = tk.Radiobutton(frames[self.rn[2]], text="6", value='f1', variable=self.jawaban3,font=("Arial", 20))
        self.opsi2_soal3 = tk.Radiobutton(frames[self.rn[2]], text="63", value='f2', variable=self.jawaban3,font=("Arial", 20))
        self.opsi3_soal3 = tk.Radiobutton(frames[self.rn[2]], text="120", value='20', variable=self.jawaban3,font=("Arial", 20))
        self.opsi4_soal3 = tk.Radiobutton(frames[self.rn[2]], text="9", value='f3', variable=self.jawaban3,font=("Arial", 20))
        
        # soal 4
        self.soal4 = ttk.Label(frames[self.rn[3]], text="Hasil dari 7,5 x 2/3 adalah:",font=("Arial", 20))
        self.jawaban4 = tk.StringVar(value="none")
        self.opsi1_soal4 = tk.Radiobutton(frames[self.rn[3]], text="8", value='f1', variable=self.jawaban4,font=("Arial", 20))
        self.opsi2_soal4 = tk.Radiobutton(frames[self.rn[3]], text="2", value='f2', variable=self.jawaban4,font=("Arial", 20))
        self.opsi3_soal4 = tk.Radiobutton(frames[self.rn[3]], text="7", value='f3', variable=self.jawaban4,font=("Arial", 20))
        self.opsi4_soal4 = tk.Radiobutton(frames[self.rn[3]], text="5", value='20', variable=self.jawaban4,font=("Arial", 20))

        # soal 5
        self.soal5 = ttk.Label(frames[self.rn[4]], text="Hasil dari √841 x √1225 adalah:",font=("Arial", 20))
        self.jawaban5 = tk.StringVar(value="none")
        self.opsi1_soal5 = tk.Radiobutton(frames[self.rn[4]], text="1.015", value='20', variable=self.jawaban5,font=("Arial", 20))
        self.opsi2_soal5 = tk.Radiobutton(frames[self.rn[4]], text="120", value='f1', variable=self.jawaban5,font=("Arial", 20))
        self.opsi3_soal5 = tk.Radiobutton(frames[self.rn[4]], text="1.000", value='f2', variable=self.jawaban5,font=("Arial", 20))
        self.opsi4_soal5 = tk.Radiobutton(frames[self.rn[4]], text="1.485", value='f3', variable=self.jawaban5,font=("Arial", 20))
        
        for i in range(1,6):
            eval('self.soal'+str(i)).pack(anchor="nw", padx=30, pady=8)
            eval('self.opsi1_soal'+str(i)).pack(anchor="nw",padx=60,pady=10)
            eval('self.opsi2_soal'+str(i)).pack(anchor="nw",padx=60,pady=10)
            eval('self.opsi3_soal'+str(i)).pack(anchor="nw",padx=60,pady=10)
            eval('self.opsi4_soal'+str(i)).pack(anchor="nw",padx=60,pady=10)

        for i, frame in enumerate(frames):
            powered_label = tk.Label(frame, text="powered by: Kelompok5", font=("Courier New", 16), anchor="sw")
            powered_label.pack(anchor="se", padx=30, pady=60)


class ExamView:
    def login():
        pass
    def mulai_ujian(self, user):
        self.current_slide = 1
        self.user= user
        self.submit_button = tk.Button(button_frame, text="submit", command=self.kalkulasi,font=("Arial", 10))
        self.submit_button.pack_forget()
        self.next_button = tk.Button(button_frame, text="Next", command=lambda: self.show_slide(self.current_slide + 1),font=("Arial", 10))
        self.next_button.pack(side="right", padx=25, pady=10)
        self.previous_button = tk.Button(button_frame, text="Previous", command=lambda: self.show_slide(self.current_slide - 1),font=("Arial", 10))
        self.previous_button.pack_forget()
        buttons = [
            ("soal 1", 1),
            ("soal 2", 2),
            ("soal 3", 3),
            ("soal 4", 4),
            ("soal 5", 5)
        ]
        for text, slide_number in buttons:
            btn = tk.Button(navigation_frame, text=text, command=lambda sn=slide_number: self.show_slide(sn), font=("Arial", 10))
            btn.pack(side="left", padx=10, pady=10)
        # window.after(5000, window.destroy)
        window.mainloop()
        self.jawaban = [self.user.jawaban1.get(), self.user.jawaban2.get(), self.user.jawaban3.get(), self.user.jawaban4.get(), self.user.jawaban5.get()]

    def kalkulasi(self):
        response = askquestion("Reminder", "Apakah Anda yakin?")
        if response == "yes":
            total = 0
            for i in self.jawaban:
                try:
                    total += int(i)
                except:
                    pass
            window.destroy()
            print(total)
        else:
            pass

    def show_slide(self,slide_number):
        frames[self.current_slide - 1].pack_forget()
        frames[slide_number - 1].pack(fill='both', expand=True)
        self.current_slide = slide_number
        self.update_buttons()

    def update_buttons(self):
        self.next_button.pack(side="right", padx=25, pady=10)
        self.previous_button.pack(side="left", padx=25, pady=10)
        if self.current_slide == 1:
            self.previous_button.pack_forget()
        elif self.current_slide == 5:
            self.next_button.pack_forget()
            self.submit_button.pack()
        elif self.current_slide != 5:
            self.submit_button.pack_forget()

class ExamController:
    def __init__(self, view, model):
        self.model = model
        self.view = view
        self.view.mulai_ujian(self.model)

model = ExamModel()
view = ExamView()
controller = ExamController(view, model)
