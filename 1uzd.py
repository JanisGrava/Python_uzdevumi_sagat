"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) ar kadiem cipariem tiek strādāts? arābu, pavisam ir 21
2) Romiešu cipariem... I, V, X, D, C, Cipari veido skaitli xxi
3) Kas ir klase? Klase sastāv no konstruktora vai destruktora un metodēm(iekšējās funkcijas)
4)Kādas datu strukturas zinam
        list(saraksts) a=""- tukšs saraksts
        arry(masivs) a=[]
        dict(vārdnīca) {} dict()
5) kas ir vārdnīca? atslēga, vērtība 
"""

class AAA:






    #definēju konstruktoru
    def __init__(self):
        self.roma_sk={
         1: 'I',
         4: 'IV',
         5: 'V',
         9: 'IX',
         10: 'X',
           10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'

        }
        #tā ir metode tas ir funkcija kura veikts pārveidošanu
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result
    #izveidojam objektu
kk=AAA()
skaitlis=21
#izsaucam klases ieksejo funkciju(metoda)
roman_sks=kk.uz_roman(skaitlis)
print(f"{skaitlis} romiešu ciparos ir{roman_sks}")