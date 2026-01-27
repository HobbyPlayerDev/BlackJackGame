import random
import time

Konto = 1000
GeldGesetzt = 0

Deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #Bube, Dame, König werden nur als 10 Verarbeitet und angezeigt und das Ass gibt es nicht


print("Willkommen zu BlackJack! 🃏")
print("")

def Game_function():
    global Konto
    global GeldGesetzt
    global DeinErgebnis
    global Deck
    global WeiterZiehen

    print(f"Dein Kontostand liegt bei {Konto} Euro 💵")
    try:
        GeldGesetzt = int(input("Wie viel setzt du für die Runde? "))
        print("")
        
    except ValueError: 
        print("") 
        print("Gib eine Gültige Zahl ein.")
        print("")
        return None

    if GeldGesetzt > Konto:
        print("Du hast nicht genug Geld little Bro 🥀") #Geld hat er aber nicht genug um die Zahl die er geschrieben hat zu zahlen
        return None
    else:
        if GeldGesetzt <= 0: #Geprüft ob es sich um mehr als 0 Euro handelt
            print("Du musst Geld setzen um zu spielen!")
            return None
        
        #Ab hier gehts normal weiter
        print("")
        print(f"Du gehst mit {GeldGesetzt} Euro in die Runde!")
        
        #Kartenmechanismus (nur für erste Karten des Spielers)
        #Erste und Zweite Karte wird gezogen
        Karte1 = random.choice(Deck)
        Karte2 = random.choice(Deck)
        DeinErgebnis = Karte1 + Karte2
        print(f"Du hast eine {Karte1} und eine {Karte2} gezogen. Insgesammt hast du jetzt {DeinErgebnis}")
        print("")

        #Karten wurden gezogen. Möchte der Spieler weiter?
        WeiterZiehen = input("Möchtest du noch eine Karte ziehen? ").strip().lower() #Characters sind egal #Großbuchstaben sind Egal
        print(f"Du schreibst {WeiterZiehen}")
        #Karte ziehen
        def NochEineKarte():
            global NeueKarte
            global WeiterZiehen
            global DeinErgebnis
            global Konto
            
            if WeiterZiehen in ["ja", "weiter", "j", "hit"]:
                print("Du ziehst eine Weitere Karte 🃏")
                #Hier neue Karte auswürfeln
                NeueKarte = random.choice(Deck)
                DeinErgebnis += NeueKarte
                print("")
                print(f"Du hast eine {NeueKarte} gezogen. Insgesammt hast du jetzt Insgesammt: {DeinErgebnis}")
                #Überprüfen ob man über 21 ist.
                if DeinErgebnis > 21:
                    print("Du bist über 21 gekommen. Du hast Verloren!")
                    Konto -= GeldGesetzt #Geld wird genommen
                    return None
                else:
                    #Man hat eine Karte genommen. Man ist unter 22.
                    WeiterZiehen = input("Möchtest du noch eine Karte ziehen? ").strip().lower()
                    NochEineKarte()
            elif WeiterZiehen in ["nein", "ne", "n"]:
                print("")
                print(f"Du bleibst bei {DeinErgebnis}")
                print("")
                #Dealer hinzufügen hier! ##################
            else:
                #Es wird so oft Nachgefragt bis sich der Spieler für Ja oder Nein entscheidet.
                print("Gib Ja oder Nein an!")
                WeiterZiehen = input("Möchtest du noch eine Karte ziehen? ").strip().lower()
                NochEineKarte()

        NochEineKarte()


#Hier gehts für die weiter die durch sind mit der Runde ("None") Egal ob Verloren gewonnen oder abgebrochen.
#Ab hier gehts wieder zurück in ein neues Game solange man Geld hat.
#Du gehst immer wieder in eine Runde außer du hast kein Geld
while True:
    if Konto <= 0:
        print("Du hast kein Geld mehr übrig! 📉❌💵")
        exit(1)
    else:
        Game_function()