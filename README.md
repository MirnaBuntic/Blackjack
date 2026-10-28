# Blackjack – Python 

Blackjack er et konsollbasert kortspill utviklet i Python, der spilleren konkurrerer mot en datastyrt dealer. Målet er å komme så nær 21 poeng som mulig uten å overskride grensen.

Prosjektet er utviklet for å øve på **funksjoner, løkker, betingelser, lister, dictionaries og spilllogikk** i Python.

## Teknologier

- **Python** – Programmeringsspråket som brukes til å utvikle spillet.
- **Random** – Innebygd Python-modul som brukes til å stokke kortstokken.
- **Terminal/konsoll** – Brukes til å spille gjennom tekstbaserte kommandoer.

## Funksjonalitet

Spillet inneholder flere funksjoner som gjenskaper grunnleggende regler fra Blackjack:

- **Kortstokk** – En standard kortstokk med 52 kort opprettes og stokkes før hver runde.
- **Kortutdeling** – Spilleren og dealeren får utdelt to kort hver ved starten av en runde.
- **Hit eller Stand** – Spilleren kan velge å trekke flere kort (`h`) eller beholde hånden sin (`s`).
- **Automatisk dealer** – Dealeren trekker automatisk kort frem til håndens verdi er minst 17.
- **Poengberegning** – Kortverdiene beregnes automatisk, inkludert ess som kan telle som 1 eller 11.
- **Innsatssystem** – Spilleren starter med 5 sjetonger og kan satse et valgfritt antall innenfor sin beholdning.
- **Resultatberegning** – Spillet avgjør om spilleren vinner, taper eller får uavgjort.
- **Flere runder** – Spilleren kan fortsette å spille så lenge det finnes sjetonger igjen, eller avslutte ved å skrive `0` når innsatsen velges.

## Hvordan spillet fungerer

Programmet er delt opp i flere funksjoner med ulike ansvarsområder.

`nyKortlek()` oppretter en kortstokk ved hjelp av dictionaries og lister. Kortene får navn, symbol og verdi før kortstokken stokkes med `random.shuffle()`.

`dealKort()` deler ut kort ved å hente dem fra kortstokken med `.pop()`.

`handVärde()` beregner den totale verdien av kortene på hånden og justerer automatisk verdien til ess dersom summen overstiger 21.

`finUtskrift()` og `visaHand()` brukes til å presentere kortene på en lesbar måte i terminalen.

Hovedfunksjonen `blackjack()` styrer spillets gang, inkludert innsats, spillerens valg, dealerens tur og beregning av resultatet.

Programmet bruker også `try` og `except` for å håndtere ugyldige inndata når spilleren skal velge innsats.

## Hva jeg har lært

Gjennom dette prosjektet har jeg fått praktisk erfaring med flere sentrale konsepter innen Python:

- Oppdeling av kode i funksjoner.
- Bruk av dictionaries og lister for å organisere data.
- Løkker og betingelser for å kontrollere spillflyten.
- Bruk av `random` for tilfeldig kortutdeling.
- Håndtering og validering av brukerinput.
- Utvikling av spilllogikk og automatiserte handlinger.
- Bruk av `try` og `except` for enkel feilhåndtering.

## Videreutvikling

Spillet er en forenklet versjon av Blackjack og kan videreutvikles med flere funksjoner.

Mulige forbedringer inkluderer støtte for splitting og doubling down, en egen utbetaling for naturlig Blackjack og et grafisk brukergrensesnitt.

Prosjektet har først og fremst hatt fokus på å bygge et fungerende kortspill ved hjelp av grunnleggende Python-programmering.
