#Liður 1
tala1=int(input("Sláðu inn tölu 1 "))
tala2=int(input("Sláðu inn tölu 2 "))
print("Tölurnar lagðar saman ",tala1+tala2)
print("Tölurnar margfaldaðar saman ",tala1*tala2)

#Liður 2
fornafn=input("Sláðu inn fornafnið þitt ")
eftirnafn=input("Sláðu inn eftirnafnið þitt ")
print("Halló",fornafn,eftirnafn)

#Liður 3
text=input("Sláðu inn texta ")
tellagstafi=0
telhastafi=0
tellagstafieftir=0

for x in range(len(text)):
    if (text[x].isalpha() and text[x].isupper()):
        telhastafi=telhastafi+1
        if (text[x +1].islower()):
            tellagstafieftir=tellagstafieftir+1
    elif(text[x].isalpha() and text[x].islower()):
        tellagstafi=tellagstafi+1

print("Það komu",telhastafi,"hástafir")
print("Það komu",tellagstafi,"lágstafir")
print("Það komu",tellagstafieftir,"lágstafir koma strax á eftir hástaf")
            
