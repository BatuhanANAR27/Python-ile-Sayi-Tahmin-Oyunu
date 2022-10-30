import random as r
sayi=r.randint(1,100)
tahmin_sayisi=0
print('-'*33)
print("""1 ile 100 arasında bir sayı tuttum bil bakalım kaç""")
tahmin=int(input("sayı girişi yapınız="))
while True:
    tahmin_sayisi= tahmin_sayisi+1
    if tahmin>sayi:
        tahmin=int(input('Lütfen daha küçük bir sayi deneyiniz='))
    elif tahmin<sayi:
        tahmin = int(input('Lütfen daha büyük bir sayi deneyiniz='))
    else:
        break
print('-'*33)
print('{} sayısının {} denemede buldunuz '.format(sayi,tahmin_sayisi))
