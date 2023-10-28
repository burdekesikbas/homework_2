sayi=int(input("sayı giriniz:"))
bolen=[]
asalBolen=[]

def bolenBul(sayi,bolen):
    for i in range(2,sayi+1):
        if sayi%i==0:
            bolen.append(i)


def asalBul(bolen,asalBolen):
    for i in bolen:
        asalSayi=True

        for x in range(2,i):
            if i%x==0:
                asalSayi=False
                break
    
        if asalSayi:
            asalBolen.append(i)
    


bolenBul(sayi, bolen)
asalBul(bolen, asalBolen)

print("Bolenler:", bolen)
print("Asal Bolenler:", asalBolen)


