import random
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as kutucuk
import pygame
pygame.init()
olumsuz = pygame.mixer.Sound('yanlis.mp3')
cokolumsuz = pygame.mixer.Sound('kaybettin.mp3')
cokolumlu = pygame.mixer.Sound('kazandin.mp3')
olumlu = pygame.mixer.Sound('dogru.mp3')
yanlisharf = pygame.mixer.Sound('yanlisharf.mp3')
root = tk.Tk()
root.title("Adam Asmaca - Anayasa Sürümü AD-AS")
harfyeri = tk.Label(root, font=("Arial", 26))
harfyeri.pack()
adamalan = tk.Canvas(root, bg="lightgreen", height=500, width=500)
adamalan.pack()
inf = tk.Label(root)
inf.pack()
cani = tk.Label(root)
cani.pack()
def oyun():
    adamciz(0)
    global bilinenler
    global olusankelime
    global x
    global can
    global cany
    global kelime
    global kelimeNo
    global kelimeAnlam
    global kelsy
    global kelsay
    global ekbilgi
    bilinenler = []
    olusankelime = ""
    x = ""
    can = 0
    cany = 6
    kelimeNo = random.randint(0,33)
    kelime = liste[kelimeNo]
    kelimeAnlam = listeAnlam[kelimeNo]
    kelsy = str(len(kelime)) + " harfli bir kelime"
    kelsay = len(kelime) * " _ "
    harfyeri.config(text=kelsay)
    harfyeri.config(fg="black")
    inf.config(text="")
    cani.config(text = kelsy)
def dnx(event):
            global bilinenler
            global olusankelime
            global x
            global can
            global cany
            global kelime
            global kelsay
            global ekbilgi
            gelenharf = event.char
            if gelenharf in Harfler:
                if gelenharf in bilinenler:
                        harfyeri.config(fg="orange")
                        inf.config(text="Aynı harfe bastınız")
                        yanlisharf.play()
                else:
                    bilinenler.append(gelenharf)
                    if gelenharf in kelime:
                        harfyeri.config(fg="green")
                        inf.config(text="Doğru")
                        olumlu.play()
                    else:
                        harfyeri.config(fg="red")
                        inf.config(text="Yanlış")
                        can += 1
                        adamciz(can)
                        olumsuz.play()
                        if can == 6:
                            harfyeri.config(fg="black")
                            inf.config(text="Kaybettin")
                            ekbilgi = "Oyun bitti, kaybettin. Doğru cevap " + kelime + " olacaktı. Anlamı: " + kelimeAnlam + ". Devam edilsin mi?'"
                            kararver(False, ekler=ekbilgi)
                            oyun()
                        cany = str(int(6-can))
                        cani.config(text = kelsy)
            else:
                harfyeri.config(fg="red")
                inf.config(text="Lütfen alfabede bulunan bir harfi giriniz")
                olumsuz.play()
            olusankelime = ""
            for harf in kelime:
                if harf in bilinenler:
                        x = harf
                else:
                        x = " _ "
                olusankelime += x
            harfyeri.config(text=olusankelime)
            if olusankelime == kelime:
                kararver(True)
                oyun()
def kararver(kdurum, **kwargs):
    if kdurum == True:
        cokolumlu.play()
        karar = kutucuk.askquestion('Devam edilsin mi?', 'Kazandın! Anlamı: ' + kelimeAnlam + '. Devam edilsin mi?')
        if karar == 'yes':
            inf.config(text="Yeni oyun başlatılıyor...")
        else:
            exit()
    else:
        ekinfo = kwargs.get('ekler', None)
        cokolumsuz.play()
        karary = kutucuk.askquestion('Devam edilsin mi?', ekinfo)
        if karary == 'yes':
            inf.config(text="Yeni oyun başlatılıyor...")
        else:
            exit()
def adamciz(adamdurum):
    if adamdurum == 6:
        adamalan.create_line(325, 205, 295, 235, width=5)   # sağ bacak
    elif adamdurum == 5:
        adamalan.create_line(325, 205, 355, 235, width=5)   # sol bacak
    elif adamdurum == 4:
        adamalan.create_line(325, 145, 295, 175, width=5)  # sağ kol
    elif adamdurum == 3:
        adamalan.create_line(325, 145, 355, 175, width=5)    # sol kol
    elif adamdurum == 2:
        adamalan.create_line(325, 135, 325, 205, width=5)   # vücut
    elif adamdurum == 1:
        adamalan.create_oval(305, 98, 345, 138, width=5)  # kafa
    elif adamdurum == 0:
        adamalan.delete("all")
        adamalan.create_line(165, 398, 315, 398, width=5, fill='darkblue')  # taban
        adamalan.create_line(250, 398, 250, 78, width=5, fill='darkblue')  # dikme
        adamalan.create_line(250, 78, 325, 78, width=5, fill='darkblue')  # üst yan çizgi
        adamalan.create_line(325, 78, 325, 98, width=5, fill='darkblue')  # ip    
sozluk = {
    "hürriyet": "özgürlük",
    "maksat": "amaç",
    "yoksun": "belli bir şeyin yokluğunu çeken",
    "sansür": "Bazı fikir ve haberlerin devlet tarafından kısıtlanması veya engellenmesidir",
    "isyan": "ayaklanma, başkaldırma",
    "makul": "mantığa uygun olan",
    "esas": "bir şeyin özü",
    "muamele": "tutum, yol",
    "beyan": "açıklamak, ortaya koymak",
    "zapt": "zorla alma, ele geçirme",
    "müracaat": "başvuru",
    "demokratik": "demokrasiye uygun olan",
    "bağdaşmak": "birbiriyle uyuşmak",
    "prensip": "ilke",
    "haysiyet": "onur, saygınlık",
    "istismar": "bir kişinin iyi niyetini kötüye kullanmak",
    "yahut": "ya da",
    "ihlal": "zarar verme, bozma",
    "güvence": "alınan bu sorumluluğa güven sağlamak üzere ortaya konulan şey",
    "müdafaa": "savunma",
    "fıkra": "gazetelerde bir olayı yorumlayan köşe yazısı",
    "ıslah": "düzeltme, iyileştirme",
    "müessese": "kurum, kuruluş",
    "meşru": "doğru, haklı, yasal olan",
    "iddia": "taşımadığı bir niteliği, kendinde var olmayan bir yeteneği varmış gibi gösterme çabası",
    "merci": "bir işin çözümü için başvurulan makam",
    "kanaat": "elindekiyle yetinme",
    "nüfuz": "başkalarına söz geçirme",
    "usul": "asıllar, kök",
    "cevaz": "izin verme",
    "rücu": "geri dönme, cayma",
    "isnat": "kara çalma, suç yükleme",
    "müsadere": "işlenen bir suç ile ilgili belirli bazı eşya veya kazançların mülkiyetinin devlete aktarılması",
    "müeyyide": "bir kişinin  hukuk kurallarına uygun davranmadığı durumlarda devletin zor kullanarak o kişinin kurallara uygun davranmasını sağlaması"
}
liste = list(sozluk.keys())
listeAnlam = list(sozluk.values())
Harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
oyun()
root.bind('<Key>', dnx)
root.mainloop()
