import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import time


class Database:
    def login(self):
        laman_login = tk.Tk()
        laman_login.title("Laman Login")
        laman_login.attributes('-fullscreen',True)
        laman_login.configure(background='white')

        data=[('alan','123'),('nazril','456')]
        sudah_ujian=[]
        NIK = tk.StringVar()
        PASSWORD = tk.StringVar()

        def tombol_click():
            user_nik = nik_entry.get().lower()
            user_pass = password_entry.get().lower()
            if (user_nik,user_pass) in data:
                    konfirmasi=messagebox.askquestion("Success", "mulai ujian")
                    if konfirmasi=='yes':
                        sudah_ujian.append(user_nik)
                        laman_login.destroy()
                    else:
                        pass
            else:
                messagebox.showerror("Input Error", "username atau password salah, coba masukkan yang benar")
                nik_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
               
        input_frame = ttk.Frame(laman_login)
        input_frame.pack(padx=10,pady=10,fill="x")

        keterangan_frame = ttk.Frame(laman_login)
        keterangan_frame.pack(side='bottom',padx=10,pady=10,fill="x")

        judul = ttk.Label(input_frame,text="SELAMAT DATANG PESERTA UTBK",font=("Helvetica", 16))
        judul.pack(anchor='center', pady=20)

        nik_label = ttk.Label(input_frame,text="NIK:",font=("Helvetica", 12))
        nik_label.pack(padx=10,expand=True)
        nik_entry = ttk.Entry(input_frame,textvariable=NIK,font=("Helvetica", 12))
        nik_entry.pack(padx=10,expand=True)

        password_label = ttk.Label(input_frame,text="Password:",font=("Helvetica", 12))
        password_label.pack(padx=10,expand=True)
        password_entry = ttk.Entry(input_frame,textvariable=PASSWORD,font=("Helvetica", 12))
        password_entry.pack(padx=10,expand=True)

        tombol_login = ttk.Button(input_frame,text="Login!",command=tombol_click)
        tombol_login.pack(side='bottom',padx=10,pady=10)

        teks = ttk.Label(keterangan_frame,text=f'''\tImplementasi sederhana Gambaran\n
            Aplikasi Ujian SNBT berbasis GUI dan MVC\n\n        
            \t\tKelompok 5:\n        
            \t\t    Alan\n        
            \t\t    Nazril\n        
            \t\t    Kayla\n        
            \t\t    Marsa''',font=("Helvetica", 14))
        teks.pack(anchor='center',pady=20)

        laman_login.mainloop()
        


class ExamModel:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x200")
        self.window.title("UTBK")
        self.window.attributes("-fullscreen", True)

        self.laman_ujian=tk.Frame(self.window)
        self.laman_ujian.pack(padx=5, pady=5, fill="both", expand=True)

        self.laman_mtk=tk.Frame(self.laman_ujian)
        self.laman_mtk.pack(padx=5, pady=5, fill="both", expand=True)

        self.laman_bi=tk.Frame(self.laman_ujian)
        self.laman_bi.pack(padx=5, pady=5, fill="both", expand=True)

        #MATEMATIKA
        self.frames1 = [tk.Frame(self.laman_mtk) for _ in range(5)]
        for frame in self.frames1:
            frame.pack_forget()
        self.frames1[0].pack(fill='both', expand=True)

        for i, frame in enumerate(self.frames1):
            judul = tk.Label(frame, text='PENALARAN MATEMATIKA', font=("Arial", 27))
            judul.pack(padx=20, pady=5, fill='x')
            judul.configure(bg='dark grey')
            label = tk.Label(frame, text=f"soal {i+1}", font=("Arial", 27))
            label.pack(padx=20, pady=5, anchor="nw")
        self.data = ['12345alan', '56789nazril']
        self.rn = random.sample(range(0, 5), 5)

        # Jawaban
        self.jawaban_mtk=[tk.StringVar(value="none") for _ in range(5)]
        self.mtk=[
            # soal 1
            (ttk.Label(self.frames1[self.rn[0]], text="Himpunan Penyelesaian dari x²-2x-8=0 adalah:", font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[0]], text="(-2,4)", value='20', variable=self.jawaban_mtk[0], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[0]], text="(4,8)", value='f1', variable=self.jawaban_mtk[0], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[0]], text="(3,6)", value='f2', variable=self.jawaban_mtk[0], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[0]], text="(21,-8)", value='f3', variable=self.jawaban_mtk[0], font=("Arial", 20))),

            # soal 2
            (ttk.Label(self.frames1[self.rn[1]], text="Hasil dari 4 log 8 + 4 log 32 adalah:", font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[1]], text="5", value='f1', variable=self.jawaban_mtk[1], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[1]], text="4", value='20', variable=self.jawaban_mtk[1], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[1]], text="7", value='f2', variable=self.jawaban_mtk[1], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[1]], text="3", value='f3', variable=self.jawaban_mtk[1], font=("Arial", 20))),

            # soal 3
            (ttk.Label(self.frames1[self.rn[2]], text="Hasil dari 5!:", font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[2]], text="6", value='f1', variable=self.jawaban_mtk[2], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[2]], text="63", value='f2', variable=self.jawaban_mtk[2], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[2]], text="120", value='20', variable=self.jawaban_mtk[2], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[2]], text="9", value='f3', variable=self.jawaban_mtk[2], font=("Arial", 20))),

            # soal 4
            (ttk.Label(self.frames1[self.rn[3]], text="Hasil dari 7,5 x 2/3 adalah:", font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[3]], text="8", value='f1', variable=self.jawaban_mtk[3], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[3]], text="2", value='f2', variable=self.jawaban_mtk[3], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[3]], text="7", value='f3', variable=self.jawaban_mtk[3], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[3]], text="5", value='20', variable=self.jawaban_mtk[3], font=("Arial", 20))),

            # soal 5
            (ttk.Label(self.frames1[self.rn[4]], text="Hasil dari √841 x √1225 adalah:", font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[4]], text="1.015", value='20', variable=self.jawaban_mtk[4], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[4]], text="120", value='f1', variable=self.jawaban_mtk[4], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[4]], text="1.000", value='f2', variable=self.jawaban_mtk[4], font=("Arial", 20)),
            tk.Radiobutton(self.frames1[self.rn[4]], text="1.485", value='f3', variable=self.jawaban_mtk[4], font=("Arial", 20))) ]
        
        #BAHASA INDONESIA
        self.frames2 = [tk.Frame(self.laman_bi) for _ in range(8)]
        for frame in self.frames2:
            frame.pack_forget()
        self.frames2[0].pack(fill='both', expand=True)

        for i, frame in enumerate(self.frames2):
            judul = tk.Label(frame, text='BAHASA INDONESIA', font=("Arial", 27))
            judul.pack(padx=20, pady=5, fill='x')
            judul.configure(bg='dark grey')
            label = tk.Label(frame, text=f"soal {i+1}", font=("Arial", 27))
            label.pack(padx=20, pady=5, anchor="nw")
        self.data = ['12345alan', '56789nazril']
        self.rn1 = random.sample(range(0, 8), 8)

        # jawaban
        self.jawaban_bi=[tk.StringVar(value="none") for _ in range(8)]
        self.bi=[
            # soal 1
            (ttk.Label(self.frames2[self.rn1[0]], text="Kata “atau” merupakan konjungsi?:", font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[0]], text="Tujuan", value='f1', variable=self.jawaban_bi[0], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[0]], text="Pilihan", value='12.5', variable=self.jawaban_bi[0], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[0]], text="Temporal", value='f2', variable=self.jawaban_bi[0], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[0]], text="Kesimpulan", value='f3', variable=self.jawaban_bi[0], font=("Arial", 20))),

            # soal 2
            (ttk.Label(self.frames2[self.rn1[1]], text="Ceramah bertujuan untuk memberikan?", font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[1]], text="Nasihat baik", value='12.5', variable=self.jawaban_bi[1], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[1]], text="Kebencian", value='f1', variable=self.jawaban_bi[1], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[1]], text="Kemurkaan", value='f2', variable=self.jawaban_bi[1], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[1]], text="Keburukan", value='f3', variable=self.jawaban_bi[1], font=("Arial", 20))),

            # soal 3
            (ttk.Label(self.frames2[self.rn1[2]], text="Bahasa yang digunakan dalam teks ceramah adalah?", font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[2]], text="Efektif", value='12.5', variable=self.jawaban_bi[2], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[2]], text="Ambigu", value='f1', variable=self.jawaban_bi[2], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[2]], text="Rancu", value='f2', variable=self.jawaban_bi[2], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[2]], text="Bahasa gaul", value='f3', variable=self.jawaban_bi[2], font=("Arial", 20))),

            # soal 4
            (ttk.Label(self.frames2[self.rn1[3]], text="Nilai yang menjelaskan baik dan buruk seseorang dalam cerita adalah nilai?", font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[3]], text="Agama", value='f1', variable=self.jawaban_bi[3], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[3]], text="Sosial", value='f2', variable=self.jawaban_bi[3], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[3]], text="Budaya", value='f3', variable=self.jawaban_bi[3], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[3]], text="Moral", value='12.5', variable=self.jawaban_bi[3], font=("Arial", 20))),

            # soal 5
            (ttk.Label(self.frames2[self.rn1[4]], text="Lawan kata dari tetiran adalah?", font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[4]], text="Luar", value='f1', variable=self.jawaban_bi[4], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[4]], text="Asli", value='12.5', variable=self.jawaban_bi[4], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[4]], text="Palsu", value='f2', variable=self.jawaban_bi[4], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[4]], text="Lapar", value='f3', variable=self.jawaban_bi[4], font=("Arial", 20))),

            # soal 6
            (ttk.Label(self.frames2[self.rn1[5]], text="Berikut yang termasuk ciri-ciri cerpen adalah?", font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[5]], text="Jalan ceritanya pendek", value='f1', variable=self.jawaban_bi[5], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[5]], text="Memiliki jumlah 10.000 kata", value='f2', variable=self.jawaban_bi[5], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[5]], text="Berasal dari kehidupan sehari-hari", value='f3', variable=self.jawaban_bi[5], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[5]], text="Tidak ada permasalahan dalam cerita", value='12.5', variable=self.jawaban_bi[5], font=("Arial", 20))),

            # soal 7
            (ttk.Label(self.frames2[self.rn1[6]], text="Sebuah gagasan pokok yang mendasari dari jalan cerita sebuah cerpen disebut?", font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[6]], text="Tema", value='12.5', variable=self.jawaban_bi[6], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[6]], text="Alur", value='f1', variable=self.jawaban_bi[6], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[6]], text="Setting", value='f2', variable=self.jawaban_bi[6], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[6]], text="Tokoh", value='f3', variable=self.jawaban_bi[6], font=("Arial", 20))),

            # soal 8
            (ttk.Label(self.frames2[self.rn1[7]], text="Sebuah gagasan pokok yang mendasari dari jalan cerita sebuah cerpen disebut?", font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[7]], text="Tema", value='12.5', variable=self.jawaban_bi[7], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[7]], text="Alur", value='f1', variable=self.jawaban_bi[7], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[7]], text="Setting", value='f2', variable=self.jawaban_bi[7], font=("Arial", 20)),
            tk.Radiobutton(self.frames2[self.rn1[7]], text="Tokoh", value='f3', variable=self.jawaban_bi[7], font=("Arial", 20))) ]
        # --------------------------------------------------------------------------------------------------------------------------------
        for a,b,c,d,e in self.mtk:
            a.pack(anchor="nw", padx=30, pady=8)
            b.pack(anchor="nw", padx=60, pady=10)
            c.pack(anchor="nw", padx=60, pady=10)
            d.pack(anchor="nw", padx=60, pady=10)
            e.pack(anchor="nw", padx=60, pady=10)

        for a,b,c,d,e in self.bi:
            a.pack(anchor="nw", padx=30, pady=8)
            b.pack(anchor="nw", padx=60, pady=10)
            c.pack(anchor="nw", padx=60, pady=10)
            d.pack(anchor="nw", padx=60, pady=10)
            e.pack(anchor="nw", padx=60, pady=10)

        for frame in self.frames1:
            powered_label = tk.Label(frame, text="powered by: Kelompok5", font=("Courier New", 16), anchor="sw")
            powered_label.pack(anchor="se", padx=30, pady=60)

        for frame in self.frames2:
            powered_label = tk.Label(frame, text="powered by: Kelompok5", font=("Courier New", 16), anchor="sw")
            powered_label.pack(anchor="se", padx=30, pady=60)


class ExamView:
    def __init__(self):
        self.jawaban_mtk = []
        self.jawaban_bi = []
        self.total = 0
        self.sisa_waktu = 60

    def mulai_ujian(self, user):
        self.user= user
        self.mtk(self.user)
    
    def mtk(self,user):
        self.user=user
        self.user.laman_bi.pack_forget()
        button_frame = tk.Frame(self.user.laman_mtk)
        button_frame.pack(side="bottom", fill="x")
        navigation_frame = tk.Frame(self.user.laman_mtk)
        navigation_frame.pack(side="bottom", fill="x")

        self.submit_button = tk.Button(button_frame, text="submit", command=self.kalkulasi1, font=("Arial", 10))
        self.next_button = tk.Button(button_frame, text="Next", command=lambda: self.show_slide1(self.current_slide + 1), font=("Arial", 10))
        self.previous_button = tk.Button(button_frame, text="Previous", command=lambda: self.show_slide1(self.current_slide - 1), font=("Arial", 10))
        self.submit_button.pack(side="right", padx=25, pady=10)
        self.current_slide = 1
        self.user = user
        self.next_button.pack(side="right", padx=25, pady=10)
        self.previous_button.pack_forget()
        buttons = [("soal 1", 1),("soal 2", 2),("soal 3", 3),("soal 4", 4),("soal 5", 5)]
        for text, slide_number in buttons:
            btn = tk.Button(navigation_frame, text=text, command=lambda sn=slide_number: self.show_slide1(sn), font=("Arial", 10))
            btn.pack(side="left", padx=10, pady=10)

        self.waktu1 = tk.Label(navigation_frame,font=("Arial", 12), anchor='s')
        self.waktu1.pack(side='right',padx=20, pady=5)
        self.timer1= self.user.laman_mtk.after(1000, self.update_timer1)
        self.user.window.mainloop()
        self.jawaban_mtk = [var.get() for var in self.user.jawaban_mtk]

    def update_timer1(self):
        if self.sisa_waktu > 0:
            self.sisa_waktu -= 1
            menit, detik = divmod(self.sisa_waktu, 60)
            self.waktu1.config(text=f"Sisa waktu:{menit:02}:{detik:02}")
            self.user.laman_mtk.after(1000, self.update_timer1)
        else:
            self.user.laman_mtk.pack_forget()
            self.b_indo(self.user)

    def kalkulasi1(self):
        respon = messagebox.askquestion("Reminder", "Masuk ke sesi selanjutnya?")
        if respon == "yes":
            time.sleep(2)
            self.sisa_waktu=0
        else:
            pass

    def show_slide1(self, slide_number):
        self.user.frames1[self.current_slide - 1].pack_forget()
        self.user.frames1[slide_number - 1].pack(fill='both', expand=True)
        self.current_slide = slide_number
        self.update_buttons1()

    def update_buttons1(self):
        self.next_button.pack(side="right", padx=25, pady=10)
        self.previous_button.pack(side="left", padx=25, pady=10)
        if self.current_slide == 1:
            self.previous_button.pack_forget()
        elif self.current_slide == 5:
            self.next_button.pack_forget()
        else:
            self.next_button.pack(side="right", padx=25, pady=10)
            self.previous_button.pack(side="left", padx=25, pady=10)


    def b_indo(self,user):
        self.sisa_waktu = 60
        self.user=user
        self.user.laman_bi.pack(padx=5, pady=5, fill="both", expand=True)
        button_frame = tk.Frame(self.user.laman_bi)
        button_frame.pack(side="bottom", fill="x")
        navigation_frame = tk.Frame(self.user.laman_bi)
        navigation_frame.pack(side="bottom", fill="x")

        self.submit_button = tk.Button(button_frame, text="submit", command=self.kalkulasi2, font=("Arial", 10))
        self.next_button = tk.Button(button_frame, text="Next", command=lambda: self.show_slide2(self.current_slide + 1), font=("Arial", 10))
        self.previous_button = tk.Button(button_frame, text="Previous", command=lambda: self.show_slide2(self.current_slide - 1), font=("Arial", 10))
        self.submit_button.pack(side="right", padx=25, pady=10)
        self.current_slide = 1
        self.user = user
        self.next_button.pack(side="right", padx=25, pady=10)
        self.previous_button.pack_forget()
        buttons = [("soal 1", 1),("soal 2", 2),("soal 3", 3),("soal 4", 4),("soal 5", 5),("soal 6", 6),("soal 7",7),("soal 8", 8)]
        for text, slide_number in buttons:
            btn = tk.Button(navigation_frame, text=text, command=lambda sn=slide_number: self.show_slide2(sn), font=("Arial", 10))
            btn.pack(side="left", padx=10, pady=10)

        self.waktu2 = tk.Label(navigation_frame,font=("Arial", 12), anchor='s')
        self.waktu2.pack(side='right',padx=20, pady=5)
        self.timer2=self.user.laman_bi.after(1000, self.update_timer2)
        self.user.window.mainloop()
        self.jawaban_bi = [var.get() for var in self.user.jawaban_bi]

    def update_timer2(self):
        if self.sisa_waktu > 0:
            self.sisa_waktu -= 1
            menit, detik = divmod(self.sisa_waktu, 60)
            self.waktu2.config(text=f"Sisa waktu:{menit:02}:{detik:02}")
            self.user.laman_bi.after(1000, self.update_timer2)
        else:
            self.user.laman_bi.pack_forget()
            self.user.window.destroy()

    def kalkulasi2(self):
        respon = messagebox.askquestion("Reminder", "Akhiri Ujian?")
        if respon == "yes":
            time.sleep(2)
            self.sisa_waktu=0
        else:
            pass

    def show_slide2(self, slide_number):
        self.user.frames2[self.current_slide - 1].pack_forget()
        self.user.frames2[slide_number - 1].pack(fill='both', expand=True)
        self.current_slide = slide_number
        self.update_buttons2()

    def update_buttons2(self):
        self.next_button.pack(side="right", padx=25, pady=10)
        self.previous_button.pack(side="left", padx=25, pady=10)
        if self.current_slide == 1:
            self.previous_button.pack_forget()
        elif self.current_slide == 8:
            self.next_button.pack_forget()
        else:
            self.next_button.pack(side="right", padx=25, pady=10)
            self.previous_button.pack(side="left", padx=25, pady=10)


class Diagram():
    def __init__(self,hasil):
        self.hasil= hasil          
        def chart(axes, sizes, labels, colors, title):
            axes.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            axes.set_title(title)

        for i in self.hasil.jawaban_mtk:
            try:
                self.hasil.total += int(i)
            except:
                pass

        for i in self.hasil.jawaban_bi:
            try:
                self.hasil.total += float(i)
            except:
                pass
        self.hasil.total/=2
        persebaran_mtk = [0, 0, 0]

        for i in self.hasil.jawaban_mtk:
            if i == '20':
                persebaran_mtk[0] += 1
            elif i == 'none':
                persebaran_mtk[2] += 1
            else:
                persebaran_mtk[1] += 1

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        
        for i in self.hasil.jawaban_bi:
            try:
                self.hasil.total += int(i)
            except:
                pass

        persebaran_bi = [0, 0, 0]

        for i in self.hasil.jawaban_bi:
            if i == '12.5':
                persebaran_bi[0] += 1
            elif i == 'none':
                persebaran_bi[2] += 1
            else:
                persebaran_bi[1] += 1

        kategori = ['Benar', 'Salah', 'Tidak Dijawab']
        warna = ['green', 'red', 'gray']
        chart(ax1, persebaran_mtk, kategori, warna, 'Persebaran Jawaban matematika')
        chart(ax2, persebaran_bi, kategori, warna, 'Persebaran Jawaban bahasa indonesia')

        hasil = tk.Tk()
        hasil.title("Diagram Jawaban")
        hasil.configure(bg='white')
        hasil.attributes("-fullscreen", True)

        pemberitahuan = ''
        latar_belakang = ''
        if self.hasil.total >= 70:
            pemberitahuan = 'SELAMAT ANDA BERHASIL DALAM TES INI'
            latar_belakang = 'blue'
        else:
            pemberitahuan = 'MAAF ANDA BELUM BERHASIL DALAM TES INI'
            latar_belakang = 'red'

        label1 = tk.Label(hasil, text=pemberitahuan, font=("Arial", 27))
        label1.configure(bg=latar_belakang)
        label1.pack(padx=20, pady=5)
        label2 = tk.Label(hasil, text=f"Nilai anda: {self.hasil.total}%\nKKM: 70%", font=("Arial", 24))
        label2.pack(padx=20, pady=5)

        canvas = FigureCanvasTkAgg(fig, master=hasil)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor='center')

        frame_penutup = tk.Frame(hasil)
        frame_penutup.pack(side="bottom", fill="x")

        penutup = tk.Label(frame_penutup, text=f'info selanjutnya akan diumumkan kemendikbud.id', font=("Arial", 20), anchor='s')
        penutup.pack(padx=20, pady=5)

        finish_button = tk.Button(frame_penutup, text="OK", command=hasil.destroy, font=("Arial", 10))
        finish_button.pack(side="right", padx=25, pady=10)

        hasil.mainloop()


class ExamController:
    def __init__(self, view, model):
        self.model = model
        self.view = view
        self.view.mulai_ujian(self.model)


login= Database()
login.login()
model1 = ExamModel()
view1 = ExamView()
controller1 = ExamController(view1, model1)
diagram= Diagram(view1)
