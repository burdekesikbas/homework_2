eskiMaas = int (input("Lütfen mevcut maaşınızı giriniz:"))
print(eskiMaas)

zamOranı = float(input("Lütfen zam oranını giriniz(%):"))
print(zamOranı)

yeniMaas = str((eskiMaas*(zamOranı/100)) + eskiMaas)
print("Zamlı maaşınız : " + yeniMaas)

                     
                     