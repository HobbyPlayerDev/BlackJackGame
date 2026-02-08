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
        print("Du hast nicht genug Geld für diese Aktion! 💵") #Geld hat er aber nicht genug um die Zahl die er geschrieben hat zu zahlen
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
        print(f"Du hast eine {Karte1} und eine {Karte2} gezogen. Insgesammt hast du jetzt: {DeinErgebnis}")
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
                print(f"Du hast eine {NeueKarte} gezogen. Insgesammt hast du jetzt: {DeinErgebnis}")
                #Überprüfen ob man über 21 ist.
                if DeinErgebnis > 21:
                    print("Du bist über 21 gekommen. Du hast Verloren!")
                    Konto -= GeldGesetzt #Geld wird genommen
                    return None
                else:
                    #Der Spieler hat eine Karte genommen. Der Spieler ist unter 22.
                    WeiterZiehen = input("Möchtest du noch eine Karte ziehen? ").strip().lower()
                    NochEineKarte()
            elif WeiterZiehen in ["nein", "ne", "n"]:
                print("")
                print(f"Du bleibst bei {DeinErgebnis}")
                print("")
                #Dealer Funktion ab hier
                Karte3 = random.choice(Deck)
                Karte4 = random.choice(Deck)
                DealerErgebnis = Karte3 + Karte4
                print(f"Der Dealer hat eine {Karte3} und {Karte4} gezogen. Der Dealer hat jetzt Insgesammt: {DealerErgebnis}")
                while DealerErgebnis < DeinErgebnis or DealerErgebnis == 17 and DealerErgebnis == DeinErgebnis:
                    time.sleep(3) #Mehr Zeit zum Lesen sonst wird es zuviel
                    print("") #Mehr Überischt
                    print("Der Dealer hat sich entschieden eine weitere Karte zu ziehen 🤔.")
                    print("")
                    time.sleep(4) #Mehr Zeit zum Lesen sonst wird es zuviel
                    NeueKarteDealer = random.choice(Deck)
                    DealerErgebnis += NeueKarteDealer
                    if DealerErgebnis > 21:
                        print(f"Der Dealer hat eine {NeueKarteDealer} gezogen 🎲. Insgesammt hat der Dealer jetzt: {DealerErgebnis} 🔹 Der Dealer Verliert da er überzogen hat. Du Gewinnst {GeldGesetzt} Euro 💵 🎉")
                        print("")
                        Konto += GeldGesetzt #Das Geld kriegt man hinzugefügt (Am Anfang wurde das Geld nicht genommen)
                        return None
                    else:
                        print(f"Der Dealer hat eine {NeueKarteDealer} 🃏 gezogen. Der Dealer hat jetzt Insgesammt: {DealerErgebnis}")
                    if DealerErgebnis == DeinErgebnis:
                        print(f"Der Dealer bleibt bei {DealerErgebnis}. Ihr habt somit beide gleich viel. Es steht Unentschieden, keiner Gewinnt!")
                        print("")
                        return None #Beide hatten gleich viel somit wird keinem etwas abgezogen
                if DealerErgebnis > DeinErgebnis:
                    print(f"Der Dealer bleibt bei {DealerErgebnis}. Der Dealer gewinnt! 💥 Da sein Blatt höher ist als deins.") #Der Dealer gewinnt da er eine höhere Hand hatte
                    print("")
                    Konto -= GeldGesetzt
                    return None
                elif DealerErgebnis == DeinErgebnis:
                    print(f"Der Dealer bleibt bei {DealerErgebnis}. Ihr habt somit beide gleich viel. Es steht Unentschieden, keiner Gewinnt!")
                    print("")
                    return None #Beide hatten gleich viel somit wird keinem etwas abgezogen
                else:
                    print("Fehler Code: 2! dieser Weg ist nicht möglich jedoch ist ein Fehler aufgetreten der sie hierherbringt!") #Kann eigentlich nicht passieren!
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