import random
import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as kutucuk

root = tk.Tk()
harfgir = tk.Entry(root)
harfgir.pack()
harfac = tk.Button(root, text="Dene", command=lambda: dene())
harfac.pack()
adamalan = tk.Canvas(root, bg="white", height=500, width=500)
adamalan.pack()
def dene():
    dnx(harfgir.get())
    harfgir.delete(0, tk.END)
def oyun():
    adamciz(0)
    global bilinenler
    global yanlislar
    global dogrular
    global olusankelime
    global x
    global can
    global kelime
    bilinenler = []
    yanlislar = []
    dogrular = []
    olusankelime = ""
    x = ""
    can = 0
    kelime = random.choice(liste)
    print(len(kelime) * "_")
def dnx(gelenharf):
            global bilinenler
            global yanlislar
            global dogrular
            global olusankelime
            global x
            global can
            global kelime
            
            if len(gelenharf) == 1:
                if gelenharf in Harfler:
                    if gelenharf in bilinenler:
                        print("Bunu daha önce yazmıştın")
                    else:
                        bilinenler.append(gelenharf)
                        if gelenharf in kelime:
                            print("Doğru bildin")
                            dogrular.append(gelenharf)
                        else:
                            print("Yanlış bildin")
                            yanlislar.append(gelenharf)
                            can += 1
                            adamciz(can)
                            if can == 6:
                                print("Oyun bitti")
                                print("Kaybettin")
                                print("Doğru cevap " + kelime + " olacaktı")
                                print("Doğru bildiklerin: "  + ", ".join(dogrular))
                                print("Yanlış bildiklerin: " + ", ".join(yanlislar))
                                kararver(False)
                                oyun()
                            print(str(6-can) + " canın kaldı")
                else:
                    print("Lütfen harf gir")
            else:
                print("Lütfen 1 harf girin")
            olusankelime = ""
            for harf in kelime:
                if harf in bilinenler:
                        x = harf
                else:
                        x = "_"
                    
                olusankelime += x
            print(olusankelime)
            if olusankelime == kelime:
                print("Kazandın")
                print("Doğru bildiklerin: "  + ", ".join(dogrular))
                print("Yanlış bildiklerin: " + ", ".join(yanlislar))
                kararver(True)
                oyun()
def kararver(kdurum):
    karar = kutucuk.askquestion('Devam edilsin mi?', 'Devam edilsin mi?')
    if karar == 'yes':
        print("Yeni oyun başlatılıyor...")
    else:
        exit()
def adamciz(adamdurum):
    if adamdurum == 6:
        print("sol bacak")
    elif adamdurum == 5:
        print("sağ bacak")
    elif adamdurum == 4:
        print("sol kol")
    elif adamdurum == 3:
        print("sağ kol")
    elif adamdurum == 2:
        print("gövde")
    elif adamdurum == 1:
        print("kafa")
    elif adamdurum == 0:
        print("ip ve askı")
liste = ["hürriyet", "maksat", "yoksun",
        "sansür", "isyan", "makul",
        "esas", "muamele", "beyan",
        "zapt", "müracaat", "demokratik",
        "bağdaşmak", "prensip", "haysiyet",
        "istismar", "yahut", "ihlal",
        "güvence", "müdafaa", "fıkra",
        "ıslah", "müessese", "meşru",
        "iddia", "merci", "kanaat",
        "nüfuz", "usul", "cevaz", "rücu",
        "isnat", "müsadere", "müeyyide"]

Harfler = "abcçdefgğhıijklmnoöprsştuüvyz"

oyun()
root.mainloop()