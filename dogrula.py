import bcrypt
from veritabani_baglanti import baglanti_olustur

def kullanici_kayit(username=None, password=None, etkilesim=None):
    if etkilesim:
        username = input("Kullanıcı Adı: ")
        password = input("Şifre: ")

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    conn = baglanti_olustur()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed))
        conn.commit()
        if etkilesim:
            print("Kayıt başarılı")
        return True
    except Exception as e:
        if etkilesim:
            print("Kayıt başarısız", e)
        return False
    finally:
        cursor.close()
        conn.close()

def kullanici_giris(username=None, password=None, etkilesim=False):
    if etkilesim:
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")

    conn = baglanti_olustur()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        if etkilesim:
            print("Giriş Başarılı")
        return True
    else:
        if etkilesim:
            print("Hatalı kullanıcı adı veya şifre")
        return False
    
