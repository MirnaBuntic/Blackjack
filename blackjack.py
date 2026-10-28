import random

#En funktion för en ny kortlek
def nyKortlek(): 

    #Dictonary med kortets nr och värde.
    värden = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

    symboler = ["spades", "hearts", "diamonds", "clubs"]

    kortlek = []

    #Skapa ett kort för varje kombination av namn och symbol och la till i kortlek listan
    for namn, värde in värden.items():
        for symbol in symboler:
            kort = {
                "namn" : namn,
                "symbol" : symbol,
                "värde" : värde
            }
            kortlek.append(kort)


    random.shuffle(kortlek)
    return kortlek

#Funktion för att få finare utskrift av korten
def finUtskrift(kortDict): 
    namn = kortDict["namn"]
    symbol = kortDict["symbol"]
    return f"{namn} of {symbol}"
     
#Funktion som delar ut kort
def dealKort(hand, kLek, nr=1): 
    for _ in range(nr):
        #Använde pop() för ta sista kortet
        hand.append(kLek.pop())


#Funktion för att räkna ut det totala värdet av korten i handen
def handVärde(hand):
    total = 0
    antalEss = 0

    #Lägger ihop alla kort
    for kort in hand:
        värde = kort["värde"]
        namn = kort["namn"]

        total += värde
        
        #Räknar ess så att man kan ändra värdet
        if namn == "Ace":
            antalEss += 1


    while total > 21 and antalEss > 0:
        total -= 10
        antalEss -= 1
    
    return total

#Funktion som printar korten i handen
def visaHand(hand):
    for kort in hand:
        print(f" - {finUtskrift(kort)}")


#Funktion för själva spelet
def blackjack():
  
    mynt = 5  
    
    print(f"\nWelcome to Blackjack! You have {mynt} chips.")


    while mynt > 0:
        

        try:
            insats = int(input("\nHow much do you want to bet? (0 to end the game)\n"))
        except ValueError:
            print("\nType in a number.")
            continue


        if insats == 0:
            print("\nYou ended the game.")
            break


        if insats > mynt or insats < 0:
            print("\nInvalid input.")
            continue

        #Ny runda
        kortlek = nyKortlek()

        spelarHand = []
        dealerHand = []


        dealKort(spelarHand, kortlek, 2)
        dealKort(dealerHand, kortlek, 2)

        #Visar spelarens hand
        print(f"\nYour cards:")  
        visaHand(spelarHand)
        print(f"Total value: {handVärde(spelarHand)}")

        #Visar det ena kortet ur dealerns hand (index 0)
        print("\nDealer shows:")
        print(f"- {finUtskrift(dealerHand[0])}")

        #Spelarens tur
        while True:

            if handVärde(spelarHand) == 21:
                print("\nBlackjack!")
                break

            #Spelaren får välja om det vill ta hit eller stand
            val = input(f"\nHit (h) or stand (s)?\n ").lower()

            if val == "h":
                
                dealKort(spelarHand, kortlek, 1)

                print("\nYour cards:")
                visaHand(spelarHand)
                print(f"Total value: {handVärde(spelarHand)}")
                
                if handVärde(spelarHand) > 21:
                    print("\nBusted! You went over 21.")
                    break
            

            elif val == "s":
                break

            else:
                print("\nType h or s.")
        
        spelarVärde = handVärde(spelarHand)

        #Om spelaren har mer än 21 ska insats dras bort från mynt
        if spelarVärde > 21:
            
            mynt -= insats
            print(f"\nYou lost {insats} chips.")
            continue

        print("\nDealers turn.")
        print("Dealer cards:")
        visaHand(dealerHand)


        while handVärde(dealerHand) < 17:

            dealKort(dealerHand, kortlek, 1)

            print("\nDealer drew a card")
            print("Dealer cards:")

            visaHand(dealerHand)

            print(f"Total value: {handVärde(dealerHand)}")

        dealerVärde = handVärde(dealerHand)

        #Jämför värderna
        if dealerVärde > 21 or spelarVärde > dealerVärde:
            print("\nYou won!")
            mynt += insats

        elif spelarVärde < dealerVärde:
            print(f"Dealer won with a total value of {dealerVärde}")
            print("\nBetter luck next time!")
            mynt -= insats

        else:
            print("\nPush (it is a draw).")

    print(f"\nThe game is over. You now have {mynt} chips left.")


blackjack()