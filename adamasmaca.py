import random
import turtle
import time
c = turtle.Turtle()
c.speed(0) 

def adam_cizme(sayi):
    if sayi == 5:
        c.penup()
        c.goto(-50, 120) #adamın kafası
        c.pendown()
        c.circle(50)
        
    elif sayi == 4:
        c.left(90)
        c.penup()
        c.forward(50)
        c.right(90)   #adamın gövdesi
        c.forward(50)
        c.pendown()
        c.forward(150)
        
    elif sayi == 3:
        c.left(45)
        c.forward(80) #sağ bacak

    elif sayi == 2:
        c.left(180)
        c.penup()
        c.forward(80) #sol bacak
        c.left(90)
        c.pendown()
        c.forward(80)

    elif sayi == 1:
        c.left(180)
        c.forward(80)
        c.left(45)
        c.forward(100) #sag kol 
        c.right(50)
        c.forward(80)

    elif sayi == 0:
        c.left(180)
        c.forward(80) #sol kol
        c.right(80)
        c.forward(80)

def oyun():
    c.penup()
    c.goto(0, 250)
    c.right(90)    #adamın ipi çiziliyor
    c.pendown()
    c.forward(80)
    bilinenler = []
    olusankelime = ""
    x = ""
    can = 6
    kelime = random.choice(liste)
    print(len(kelime) * "_")
    while True:
            gelenharf = input('Tahminini gir: ')
            if gelenharf in bilinenler:
                print("Bunu daha önce yazmıştın")
            else:
                bilinenler.append(gelenharf)
                if gelenharf in kelime:
                    print("Doğru bildin")
                else:
                    print("Yanlış bildin")
                    can -= 1
                    adam_cizme(can)
                    if can == 0:
                        print("Oyun bitti")
                        print("Doğru cevap " + kelime + " olacaktı")
                        print("Yeni oyun hazırlanıyor..")
                        c.clear() 
                        c.reset()
                        c.speed(0)
                        oyun()
                    print(str(can) + " canın kaldı")

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
                print("Yeni oyun hazırlanıyor..")
                c.clear() 
                c.reset()
                c.speed(0)
                oyun()

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
oyun()
