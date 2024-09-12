"""
Farklı Sayıların Toplamı
Bir liste içindeki farklı (tekrarlanmayan) sayıların toplamını hesaplayan bir fonksiyon yazın

"""

import random
import time


def sayilari_sec_ve_topla(liste):


    sayi1 , sayi2 = random.sample(liste,2)

    print("Sayılar seçiliyor bekleyiniz ....")
    time.sleep(2)

    print("ilk sayı : {}".format(sayi1))
    print(("İkinci Sayı : {}").format(sayi2))

    time.sleep(1)

    print("Sayılar birbirleri ile toplanıyor ...")

    time.sleep(2)

    print("Sayıların toplamı : {}".format(sayi1 + sayi2))


liste_sayilari = input("Lütfen aralarına boşluk koyarak sayıları giriniz :")

liste = list(map(int,liste_sayilari.split()))


sayilari_sec_ve_topla(liste)


