# KULLANICI KAYIT/GİRİŞ SİSTEMİ

Bu proje, Python kullanılıarak geliştirilmiş bir kullanıcı kayıt/giriş sistemidir. GUI kısmı 'tkinter' ile oluşturulmuştur.

## Özellikler

- Kullanıcı kayıt ve giriş sistemi
- Şifre güvenliği için bcrypt
- Şifre güvenliği için hash+salt SHA256 algoritması
- '.env' dosyası ile gizli bilgilerin güvenliği
- Şifreyi göster gizle seçeneği
- MySQL ile veritabanı bağlantı

## Gereksinimler

Projeyi çalıştırmadan önce aşağıdaki kütüphaneleri yüklemeniz gerekli.

```bash
pip install -r requirements.txt
```
Ayrıca .env dosyası oluşturmanız gerekldir.

1. .env.example dosyasını kopyalayın.
2. Yeni bir .env dosyası oluşturun
3. Kopyanızı .env dosyasına yapıştırın.
4. İçini veritabanı bilgilerinizle doldurun.

## Projeyi Çalıştırmak

terminale 'python giris_gui.py' yazın.

#### *Bu proje MIT lisansı ile lisanslanmıştır*
