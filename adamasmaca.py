import random
import turtle
import time
import tkinter
adam = turtle.Turtle()
adam.speed(0) 

def adam_cizme(sayi):
    if sayi == 5:
        adam.penup()
        adam.goto(-50, 120)
        adam.pendown()
        adam.circle(50)
        
    elif sayi == 4:
        adam.left(90)
        adam.penup()
        adam.forward(50)
        adam.right(90) 
        adam.forward(50)
        adam.pendown()
        adam.forward(150)
        
    elif sayi == 3:
        adam.left(45)
        adam.forward(80)

    elif sayi == 2:
        adam.left(180)
        adam.penup()
        adam.forward(80)
        adam.left(90)
        adam.pendown()
        adam.forward(80)

    elif sayi == 1:
        adam.left(180)
        adam.forward(80)
        adam.left(45)
        adam.forward(100)
        adam.right(50)
        adam.forward(80)

    elif sayi == 0:
        adam.left(180)
        adam.forward(80)
        adam.right(80)
        adam.forward(80)
        time.sleep(1)

def oyun():
    adam.penup()
    adam.goto(0, 250)
    adam.right(90)
    adam.pendown()
    adam.forward(80)
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
                        adam.clear() 
                        adam.reset()
                        adam.speed(0)
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
                adam.clear() 
                adam.reset()
                adam.speed(0)
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
