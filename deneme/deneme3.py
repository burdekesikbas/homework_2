sayi1=int(input("sayı giriniz:"))
sayi2=int(input("sayı giriniz:"))
ebob=0

if sayi1>sayi2:
    for i in range(1,sayi2+1):
   
        if sayi1%i==0 and sayi2%i==0:
            ebob=i
elif sayi1==sayi2:
    ebob=sayi1
else:
    for i in range(1,sayi1+1):
        if sayi1%i==0 and sayi2%i==0:
            ebob=i
print("ebob:",ebob)

ekok=(sayi1*sayi2)/ebob
print("ekok", ekok)
          
        
    
    
    
