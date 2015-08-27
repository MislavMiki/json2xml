# -*- coding: utf-8 -*-
import winsound
import os, sys
import codecs

def citajdatum (novidatum):
    dani=int(novidatum[0])
    mjesec=int(novidatum[1])
    godine=int(novidatum[2])
    popis=[]

    ldani = ["", "prvi", "drugi", u"treći", u"četvrti", "peti", u"šesti", "sedmi", "osmi", "deveti", "deseti", "jedanajesti", "dvanajesti", "trinajesti",
             u"četrnajesti", "petnajesti", u"šesnajesti", "sedamnajesti", "osamnajesti", "devetnajesti"]
    ldand = ["","", "dvadeseti", "trideseti"]
    lmjesec= ["",u"siječnja", u"veljače", u"ožujka", "travnja", "svibnja", "lipnja", "srpnja", "kolovoza", "rujna", "listopada", "studeni", "prosinca"]
    lgodine=u"dvije tisuće"
    lgodined=["", "", "", "", "", "", "", "", "", "", "", "", "dvanajeste", "trinajeste", u"četrnajeste", "petnajeste", u"šesnajeste", "sedamnajeste", "osamnajeste", "devetnajeste", "dvadesete"]
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

def embrola(nekalista):
    rjecnik={
    " ":"_ 50",
    "a":"a 61",
    "b":"b 65",
    "c":"ts 113",
    "X":"tS 90",
    "Y":"tS' 98",
    "d":"d 54",
    "D":"dZ 56",
    "Q":"dZ' 61",
    "e":"e 53",
    "f":"f 86",
    "g":"g 56",
    "h":"x 68",
    "i":"i 49",
    "j":"j 53",
    "k":"k 81",
    "l":"l 35",
    "L":"L 59",
    "m":"m 56",
    "n":"n 45",
    "N":"J 60",
    "o":"o 54",
    "p":"p 85",
    "r":"r 25",
    "s":"s 91",
    "S":"S 99",
    "t":"t 76",
    "u":"u 50",
    "v":"v 40",
    "z":"z 68",
    "Z":"Z 74"}
    string=' '.join(n for n in nekalista)
    novistring=string.lower().replace('lj', 'L').replace(u'ž','Z').replace(u'š','S').replace('nj','N').replace(u'đ','Q').replace(u'č','X').replace(u'dž', 'D').replace(u'ć','Y')
    print novistring
    skroznovi='_ 50\n'
    for el in novistring:
        skroznovi+=rjecnik[el]
        skroznovi+='\n'
        
    skroznovi+='_ 50'
    return skroznovi

if __name__ == "__main__":
    dan=input('Molim unesite dan u mjesecu \n')
    mjesec=input('Molim unesite mjesec \n')
    godina=input('Molim unesite godinu \n')
    datum=[]
    datum.append(dan)
    datum.append(mjesec)
    datum.append(godina)
    lista=[]
    lista.append("Datum valjanost proizvoda")
    potrebno=citajdatum(datum) 
    lista.extend(potrebno)
    podaci=embrola(lista)
    dat=codecs.open('mojprogram.pho' ,'w', 'utf-8')
    dat.write(podaci)
    dat.close()
    os.system('mbrola.exe cr1 mojprogram.pho mojprogram.wav')
    print 'Traženi datum je:', potrebno
    winsound.PlaySound('C:\Users\Mislav\Desktop\New folder\programi\mojprogram.wav', winsound.SND_FILENAME)
