sayi = input("Lütfen bir sayı giriniz : ")

ters = sayi[::-1]

if sayi == ters:
    print("Girdiğiniz sayı palindrom sayıdır.")
else:
    print("Girdiğiniz sayı palindrom sayı değildir.")