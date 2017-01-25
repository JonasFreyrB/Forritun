#Jónas Freyr Bjarnason
#25.01.2017
#Forritun

#Liður 1

#Byð notanda um tölu 1
tala1=int(input("Sláðu inn tölu 1 "))
#Byð notanda um tölu 2
tala2=int(input("Sláðu inn tölu 2 "))
#Birti tölu 1 og 2 lagðar saman
print("Tölurnar lagðar saman ",tala1+tala2)
#Birti tölu 1 og 2 margfaldaðar saman
print("Tölurnar margfaldaðar saman ",tala1*tala2)

#Liður 2

#Byð notanda um fornafn
fornafn=input("Sláðu inn fornafnið þitt ")
#Byð notanda um eftirnafn
eftirnafn=input("Sláðu inn eftirnafnið þitt ")
#Birti skilaboð ásamt bæði nöfnin lögð saman
print("Halló",fornafn,eftirnafn)

#Liður 3

#Byð notanda um texta
text=input("Sláðu inn texta ")
#Bý til teljara fyrir lágstafi
tellagstafi=0
#Bý til teljara fyrir hágstafi
telhastafi=0
#Bý til teljara fyrir lágstafi á eftir hástafi
tellagstafieftir=0

#Bý til for lykkju sem keyrir í gegnum textann
for x in range(len(text)):
    #Ef stafurinn í texta er bókstafur og er í hástaf
    if (text[x].isalpha() and text[x].isupper()):
        #Bæti 1 við teljara fyrir hágstafi
        telhastafi=telhastafi+1
        #Ef næsti stafur er lágstafur
        if (text[x +1].islower()):
            #Bæti 1 við teljara fyrir lágstafi á eftir hástafi
            tellagstafieftir=tellagstafieftir+1
    #Ef stafurinn í texta er bókstafur og er í lágstaf
    elif(text[x].isalpha() and text[x].islower()):
        #Bæti 1 við teljara fyrir lágstafi
        tellagstafi=tellagstafi+1
#Birti fjölda hástafi
print("Það komu",telhastafi,"hástafir")
#Birti fjölda lágstafi
print("Það komu",tellagstafi,"lágstafir")
#Birti fjölda lágstafi á eftir hástafi
print("Það komu",tellagstafieftir,"lágstafir koma strax á eftir hástaf")
            
