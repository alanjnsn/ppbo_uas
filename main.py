import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import time


class Database:
    sudah_ujian=[]
    data=[('alan','123'),('nazril','456')]

    def login(self):
        self.laman_login = tk.Tk()
        self.laman_login.geometry('1166x718')
        self.laman_login.resizable(0, 0)
        self.laman_login.state('zoomed')
        self.laman_login.title('Login Page') # DONE

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.laman_login, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.laman_login, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.nik_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.nik_label.place(x=550, y=300)

        self.nik_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.nik_entry.place(x=580, y=335, width=270)

        self.nik_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.nik_line.place(x=550, y=359)
        # ===== Username icon =========
        self.nik_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.nik_icon)
        self.nik_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.nik_icon_label.image = photo
        self.nik_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login_button = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.tombol_click)
        self.login_button.place(x=20, y=10)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

        self.laman_login.mainloop()

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def tombol_click(self):
            user_nik = self.nik_entry.get().lower()
            user_pass = self.password_entry.get().lower()
            if (user_nik,user_pass) in self.data:
                if user_nik in self.__class__.sudah_ujian:
                    messagebox.showinfo("Input Error", "Sesi anda sudah habis")
                    self.nik_entry.delete(0, tk.END)
                    self.password_entry.delete(0, tk.END)
                else:
                    konfirmasi=messagebox.askquestion("Success", "mulai ujian")
                    if konfirmasi=='yes':
                        self.sudah_ujian.append(user_nik)
                        self.laman_login.quit()
                        self.laman_login.destroy()
                    else:
                        pass
            else:
                messagebox.showerror("Input Error", "username atau password salah, coba masukkan yang benar")
                self.nik_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)

    
    def nilai_ujian(self,ujian):
        self.ujian= ujian          
        self.hasil = tk.Tk()
        self.hasil.title("Diagram Jawaban")
        self.hasil.configure(bg='white')
        self.hasil.attributes("-fullscreen", True)
        
        def chart(axes, sizes, labels, colors, title):
            axes.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            axes.set_title(title)

        for i in self.ujian.jawaban_mtk:
            try:
                self.ujian.total += int(i)
            except:
                pass

        for i in self.ujian.jawaban_bi:
            try:
                self.ujian.total += float(i)
            except:
                pass
        self.ujian.total/=2

        self.persebaran_mtk = [0, 0, 0]

        for i in self.ujian.jawaban_mtk:
            if i == '20':
                self.persebaran_mtk[0] += 1
            elif i == 'none':
                self.persebaran_mtk[2] += 1
            else:
                self.persebaran_mtk[1] += 1


        self.persebaran_bi = [0, 0, 0]

        for i in self.ujian.jawaban_bi:
            if i == '12.5':
                self.persebaran_bi[0] += 1
            elif i == 'none':
                self.persebaran_bi[2] += 1
            else:
                self.persebaran_bi[1] += 1

        fig,(ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

        kategori = ['Benar', 'Salah', 'Tidak Dijawab']
        warna = ['green', 'red', 'gray']
        chart(ax1, self.persebaran_mtk, kategori, warna, 'Persebaran Jawaban matematika')
        chart(ax2, self.persebaran_bi, kategori, warna, 'Persebaran Jawaban bahasa indonesia')


        pemberitahuan = ''
        latar_belakang = ''
        if self.ujian.total >= 70:
            pemberitahuan = 'SELAMAT ANDA BERHASIL DALAM TES INI'
            latar_belakang = 'blue'
        else:
            pemberitahuan = 'MAAF ANDA BELUM BERHASIL DALAM TES INI'
            latar_belakang = 'red'

        label1 = tk.Label(self.hasil, text=pemberitahuan, font=("Arial", 27))
        label1.configure(bg=latar_belakang)
        label1.pack(padx=20, pady=5)
        label2 = tk.Label(self.hasil, text=f"Nilai anda: {self.ujian.total}%\nKKM: 70%", font=("Arial", 24))
        label2.pack(padx=20, pady=5)

        self.canvas = FigureCanvasTkAgg(fig, master=self.hasil)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(anchor='center')
        self.frame_penutup = tk.Frame(self.hasil)
        self.frame_penutup.pack(side="bottom", fill="x")

        self.penutup = tk.Label(self.frame_penutup, text=f'info selanjutnya akan diumumkan kemendikbud.id', font=("Arial", 20), anchor='s')
        self.penutup.pack(padx=20, pady=5)

        self.finish_button = tk.Button(self.frame_penutup, text="OK", command=lambda:[self.hasil.quit(),self.hasil.destroy()], font=("Arial", 10))
        self.finish_button.pack(side="right", padx=25, pady=10)
        self.hasil.update_idletasks()
        
        self.hasil.mainloop()


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
        self.user.window.quit()

    def update_timer2(self):
        if self.sisa_waktu > 0:
            self.sisa_waktu -= 1
            menit, detik = divmod(self.sisa_waktu, 60)
            self.waktu2.config(text=f"Sisa waktu:{menit:02}:{detik:02}")
            self.user.laman_bi.after(1000, self.update_timer2)
        else:
            self.user.laman_bi.pack_forget()
            self.user.window.quit()
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
    


class ExamController:
    def __init__(self, view, model):
        self.model = model
        self.view = view
        self.view.mulai_ujian(self.model)



database= Database()

# sesi 1
database.login()
model1 = ExamModel()
view1 = ExamView()
controller1 = ExamController(view1, model1)
database.nilai_ujian(controller1.view)
# sesi 2
database.login()
model2 = ExamModel()
view2 = ExamView()
controller2 = ExamController(view2, model2)
database.nilai_ujian(view2)
