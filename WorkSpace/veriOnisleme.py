import pandas as pd

veriler = pd.read_excel("../Datas/yeraltisulari.xlsx")
depremVerileri = pd.read_excel("../Datas/depremler.xlsx")
depremVerileri2 = pd.read_excel("../Datas/depremler2.xlsx")
radonGaziVerileri = pd.read_excel("../Datas/radon.xlsx")
depremDerinligiVerileri = pd.read_excel("../Datas/derinlikDeprem.xlsx")
metanGaziVerileri= pd.read_excel("../Datas/metan.xlsx")


veriler = veriler.fillna(value=0.1)

#print(veriler)


suDerinligi = []
aylar = ["ocak", "subat", "mart", "nisan", "mayis", "haziran", "temmuz", "agustos", "eylul", "ekim", "kasim", "aralik"]

yillar = []

depremSiddeti = []

radonGazi = []

depremDerinligi = []

metanGazi= []



# tum su derinligi degerleri ay sirasina ve yil sirasina gore listeye eklelendi. ileride dictionary olarak kullanılmak uzere
for i in range(1999, 2017):
    for j in veriler[i]:
        yillar.append(i)
        suDerinligi.append(j)

#print(suDerinligi)


for i in range(1999, 2017):
    for j in depremVerileri2[i]:

        depremSiddeti.append(j)

#print(depremSiddeti)


for i in range(1999, 2017):
    for j in radonGaziVerileri[i]:

        radonGazi.append(j)

#print(depremSiddeti)

#print(radonGazi)

for i in range(1999, 2017):
    for j in depremDerinligiVerileri[i]:

        depremDerinligi.append(j)
#print(depremDerinligi)

for i in range(1999, 2017):
    for j in metanGaziVerileri[i]:

        metanGazi.append(j)




#RICHTER ÖLÇEĞİ
depremSiniflari = []
for i in depremSiddeti:

    if i >=0 and i <5:
        depremSiniflari.append("kucuk")

    elif i >=5 and i <7:

        depremSiniflari.append("orta")

    elif i == 7:

        depremSiniflari.append("ciddi")

    elif i > 7  and i < 10:

        depremSiniflari.append("buyuk")

    elif i >= 10:

        depremSiniflari.append("yikici")


#print(depremSiniflari)
print(len(depremSiniflari), len(depremSiddeti))

aylarSerisi = pd.Series(aylar * len(yillar))
yillarSerisi = pd.Series(yillar)
#print(yillarSerisi)

#print(len(aylar)*len(yillar),len())

structData = {

    "depremSiddeti" : depremSiddeti,
    "depremDerinligi" : depremDerinligi,
    "radonGazi" : radonGazi,
    "yeraltiSuDerinligi" : suDerinligi,
    "ay" : aylar * 18,
    "yil" : yillar,
    "sinif" : depremSiniflari,
    "metanGazi" : metanGazi,

}

birlestirilmisVeriler = pd.DataFrame(structData)
birlestirilmisVeriler.to_csv("../Datas/birlestirilmisVeriler.csv",index=False)

#print(birlestirilmisVeriler)





veriler = pd.read_csv("../Datas/birlestirilmisVeriler.csv")

x = veriler.iloc[:,0:4].values
y = veriler.iloc[:,6:7]

print(y)



















""""

#print(type(depremVerileri.iloc[:,0:1].iloc[0]))
print(type(depremVerileri.iloc[:,0:1].values))
print(depremVerileri.iloc[0,3])
print(type(depremVerileri.iloc[0,3]))
print(str(depremVerileri.iloc[:,0].iloc[3]))


depremTarih = depremVerileri.iloc[:,0:1].values

print(depremTarih[0][0] <= depremTarih[44][0])
print(depremTarih[0][0] , depremTarih[44][0])
print(len(depremTarih))
#def checkDate()


print(depremVerileri2)
depremAylikToplagazım = 0



for i in range(len(depremTarih)):
    for j in depremTarih:


        if depremTarih[i][0] == j[0]:
            
            depremAylikToplam = depremVerileri.iloc[i, 3] + depremAylikToplam

"""