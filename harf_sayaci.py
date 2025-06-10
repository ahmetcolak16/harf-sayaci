import string

#HARF SAYACI UYGULAMASI

metin = input(str("Lütfen metninizi giriniz:"))
harfler = list(metin.lower())
harf_listesi = list(str("abcçdefgğhıijklmnoöprsştuüvyzqwx"))
sayac = 0

for i in range(len(harf_listesi)):
    sayac = 0
    for k in range(len(metin)):
        if harfler[k] == harf_listesi[i]:
            sayac += 1 
    if sayac != 0:
        print(f"{sayac} tane {harf_listesi[i]} harfi var!")
