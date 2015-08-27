# -*- coding: cp1250 -*-
import time
import winsound

def citajdatum (novidatum):
    dani=int(novidatum[0])
    mjesec=int(novidatum[1])
    godine=int(novidatum[2])
    popis=[]

    ldani = ["", "prvi", "drugi", "treći", "cetvrti", "peti", "šesti", "sedmi", "osmi", "deveti", "deseti", "jedanajesti", "dvanajesti", "trinajesti",
             "četrnajesti", "petnajesti", "šesnajesti", "sedamnajesti", "osamnajesti", "devetnajesti"]
    ldand = ["","", "dvadeseti", "trideseti"]
    lmjesec= ["","siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja", "kolovoza", "rujna", "listopada", "studenog", "prosinca"]
    lgodine="dvije tisuće"
    lgodined=["", "", "", "", "", "", "", "", "", "", "", "", "dvanajeste", "trinajeste", "četrnajeste", "petnajeste", "šesnajeste", "sedamnajeste", "osamnajeste", "devetnajeste", "dvadesete"]
    if dani>=20:
        popis.append(ldand[int(dani/10)])
        d=dani%10
        if d != 0:
            popis.append(ldani[d])
    if dani in range (1, 20):
        popis.append(ldani[dani])
    popis.append(lmjesec[mjesec])

    popis.append(lgodine)
    if godine>=2012:
        popis.append(lgodined[int(godine%2000)])
    return popis


def meni():
    while True:
        try:
            a=int(raw_input("Upisite datum isteka valjanosti proizvoda! \n"))
            return a
        except ValueError:
            print("Ne valja... :( Probajte opet.\n")

if __name__ == "__main__":
    dan=input('Molim unesite dan u mjesecu \n')
    mjesec=input('Molim unesite mjesec \n')
    godina=input('Molim unesite godinu \n')
    datum=[]
    datum.append(dan)
    datum.append(mjesec)
    datum.append(godina)
    lista=[]
    lista.append("uvod")
    potrebno=citajdatum(datum) 
    lista.extend(potrebno)
    print 'Traženi datum je:', potrebno
    for i in lista:
        winsound.PlaySound("C:\\Documents and Settings\\Guest\\My Documents\\faks\\ursg\\programi\\"+i+".wav", winsound.SND_FILENAME)
        

   
