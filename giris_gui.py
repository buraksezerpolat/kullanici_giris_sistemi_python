import tkinter as tk
from tkinter import messagebox
from dogrula import kullanici_kayit, kullanici_giris

def sifre_goster_gizle(entry, var):
    if var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

def giris_yap():
    kullanici_adi = entry_kullanici.get()
    sifre = entry_sifre.get()

    if not kullanici_adi or not sifre:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun.")
        return
    
    if kullanici_giris(kullanici_adi, sifre, etkilesim=False):
        messagebox.showinfo("Başrılı", f"Hoş geldin, {kullanici_adi}!")
    else:
        messagebox.showwarning("Hata", "Kullanıcı adı veya şifre yanlış")

def kayit_ol():
    def kaydi_gerceklestir():
        yeni_kullanici = entry_yeni_kullanici.get()
        yeni_sifre = entry_yeni_sifre.get()

        if not yeni_kullanici or not yeni_sifre:
            messagebox.showwarning("Uyarı", "Tüm alanları doldurun.")
            return
        
        if kullanici_kayit(yeni_kullanici, yeni_sifre, etkilesim=False):
            messagebox.showinfo("Başarılı", "Kayıt Başarılı")
            pencere_kayit.destroy()
        else:
            messagebox.showerror("Hata", "Kayıt başarısız. Kullanıcı zaten var olabilir")
    
    pencere_kayit = tk.Toplevel(pencere)
    pencere_kayit.title("Kayıt Ol")
    pencere_kayit.geometry("800x600")
    tk.Label(pencere_kayit, text="Yeni Kullanıcı Adı",font=("Helvetica",12),bg="#f0f0f0").pack(pady=5)
    entry_yeni_kullanici = tk.Entry(pencere_kayit, font=("Helvetica", 12))
    entry_yeni_kullanici.pack(pady=5)

    tk.Label(pencere_kayit, text="Yeni Şifre: ", font=("Helvetica", 12)).pack(pady=5)
    entry_yeni_sifre = tk.Entry(pencere_kayit,show="*", font=("Helvetice", 12))
    entry_yeni_sifre.pack(pady=5)

    tk.Button(pencere_kayit, text="Kayıt Ol", command=kaydi_gerceklestir, font=("Helvetica", 12), bg="#2859b4", fg="#f0f0f0").pack(pady=10)
    var_yeni_sifre = tk.BooleanVar()
    check_yeni_sifre = tk.Checkbutton(
        pencere_kayit,text="Şifre Göster",
        variable=var_yeni_sifre,
        command=lambda: sifre_goster_gizle(entry_yeni_sifre, var_yeni_sifre))
    check_yeni_sifre.pack()

#Ana giriş penceresi
pencere = tk.Tk()
pencere.title("Giriş Sistemi")
pencere.geometry("800x600")

tk.Label(pencere, text="Kullanıcı Adı", font=("Helvetica", 12)).pack(pady=5)
entry_kullanici = tk.Entry(pencere, font=("Helvetica", 12))
entry_kullanici.pack(pady=5)

tk.Label(pencere, text="Şifre", font=("Helvetica", 12)).pack(pady=5)
entry_sifre = tk.Entry(pencere, show="*", font=("Helvetica", 12))
entry_sifre.pack(pady=5)
var_sifre = tk.BooleanVar()
check_sifre = tk.Checkbutton(
    pencere, 
    text="Şifreyi Göster",
    variable=var_sifre,
    command=lambda: sifre_goster_gizle(entry_sifre, var_sifre))
check_sifre.pack()

tk.Button(pencere, text="Giriş Yap", command=giris_yap, font=("Helvetica", 12), fg="#f0f0f0", bg="#2859b4").pack(pady=10)
tk.Button(pencere, text="Kayıt Ol", command=kayit_ol, font=("Helvetica", 12), fg="#f0f0f0", bg="#79a3f1").pack(pady=5)
pencere.mainloop()