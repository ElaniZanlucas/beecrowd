# Animal
# Seleção

# -*- coding: utf-8 -*-

div1 = input()
div2 = input()
div3 = input()

if(div1 == "vertebrado"):
    if(div2 == "ave"):
        if(div3 == "carnivoro"):
            print("aguia")
        elif(div3 == "onivoro"):
            print("pomba")        
    elif(div2 == "mamifero"):
        if(div3 == "herbivoro"):
            print("vaca")
        elif(div3 == "onivoro"):
            print("homem")
elif(div1 == "invertebrado"):
    if(div2 == "inseto"):
        if(div3 == "hematofago"):
            print("pulga")
        elif(div3 == "herbivoro"):
            print("lagarta")        
    elif(div2 == "anelideo"):
        if(div3 == "hematofago"):
            print("sanguessuga")
        elif(div3 == "onivoro"):
            print("minhoca")
            



