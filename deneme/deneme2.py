sayi = int(input("sayı giriniz:"))
fibonacci = [1, 1]

if sayi > 19:
    for i in range(2, sayi + 1):
        sonEleman = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(sonEleman)
    print(fibonacci)
else:
    print("Lütfen daha büyük bir sayı gir")