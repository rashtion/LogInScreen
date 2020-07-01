from Tkinter import *
import time
 
bilgiler = ("demo", "123456")
denemeHakki = 3
zaman = 0
def girisYap():
    global denemeHakki, zaman
     
    if denemeHakki <= 0:
        if time.time()-zaman >= 5:
            denemeHakki = 3
        else:
            sonuc.config(text = u"Lutfen 5 saniye bekleyiniz.")
            return False
     
    kAdi = isim.get()
    parola = sifre.get()
    print kAdi, " - ", parola
    print "Kontrol ediliyor ..."
    if kAdi == bilgiler[0] and parola == bilgiler[1]:
        print "Bilgiler dogru!"
        sonuc.config(text = u"Oturum acma islemi basarili.")
        ekraniTemizle()
    else:
        print "Bilgiler yanlis!"
        denemeHakki -= 1
        if denemeHakki == 0:
            zaman = time.time()
        sonuc.config(text = u"Bilgiler yanlis. Kalan deneme hakki: %d" %denemeHakki)
         
 
def ekraniTemizle():
    karsilama.config(text = u"Hosgeldin, Demo!")
    isimSor.destroy()
    isim.destroy()
    sifreSor.destroy()
    sifre.destroy()
    buton.destroy()
 
 
pencere = Tk()
 
pencere.title(u"canusta.com.tr - Python Dersleri")
pencere.geometry("290x200+100+100")
 
karsilama = Label(pencere)
karsilama.config(text = u"Hosgeldiniz, lutfen giris yapiniz.")
karsilama.pack()
 
isimSor = Label(pencere)
isimSor.config(text = u"Kullanici Adi:")
isimSor.pack()
 
isim = Entry(pencere)
isim.pack()
 
sifreSor = Label(pencere)
sifreSor.config(text= u"Sifreniz:")
sifreSor.pack()
 
sifre = Entry(pencere)
sifre.pack()
 
 
buton = Button(pencere)
buton.config(text = u"Giris yap!", command = girisYap)
buton.pack()
 
sonuc = Label(pencere)
sonuc.config(text = u"Giris yapilmadi.")
sonuc.pack()
 
 
mainloop ()
