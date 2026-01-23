import random
import time

Konto = 1000
GeldGesetzt = 0

Deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube (10)", "Dame (10)", "König (10)", "Ass (1 oder 11)"] #Alle Karten aus dem Deck

print("Willkommen zu BlackJack! 🃏")
print("")

def Game_function():

    print(f"Dein Kontostand liegt bei {Konto} Euro 💵")
    try:
        GeldGesetzt = int(input("Wie viel setzt du für die Runde? "))
        print("")
        
    except ValueError: 
        print("") 
        print("Gib eine Gültige Zahl ein du Trottel!")
        print("")
        return None

    if GeldGesetzt > Konto:
        print("Du hast nicht genug Geld little Bro 🥀") #Geld hat er aber nicht genug um die Zahl die er geschrieben hat zu zahlen
        return None
    else:
        if GeldGesetzt == 0: #Geprüft ob es sich um mehr als 0 Euro handelt
            print("Du musst Geld setzen.")
            return None
        
        #Ab hier gehts normal weiter
        print("")
        print(f"Du gehst mit {GeldGesetzt} Euro in die Runde!")
        print("")
        DeineKarte = random.choice(Deck)



    return None #Eigentlich kommt man hier nicht hin deswegen raus aus der Funktion


#Ab hier gehts weiter für die "None"


#Du gehst immer wieder in eine Runde außer du hast kein Geld
while True:
    if Konto <= 0:
        print("Du hast kein Geld mehr übrig! 📉❌💵")
        exit(1)
    else:
        Game_function()