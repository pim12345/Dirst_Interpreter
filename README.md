# Dirst scripting Interpreter

A python Dirst scripting interpreter

Deze python Dirst scripting interpreter is gebaseerd op de [Dirst programming language](https://esolangs.org/wiki/Dirst) and ondersteund een deel van alle functies van de taal met een toevoeging om functies uit te voeren.
Ook ondersteund deze interpreter alleen het script gedeelte van de taal en helaas niet het folder gedeelte van de taal.

In this project is has also added functions calls in the project(an way to declare functions and run them, with an argument and return value)

# installatie

clone deze repository
installeer python 3.11 (https://www.python.org/downloads/)(oudere versies werken niet wegens het gebruiken van de self keyword in type notatie)
installeer de requirements met ```pip install -r requirements.txt```

# gebruik

# Requirements

# === ADDED LANGUAGE OPERATORS ===
## waarom?
om aan de eisen van de atp opdracht te voldoen heb ik 1 operator veranderd en 2 toegevoegd.
## added operators
veranderd aan de taal is dat de instructie: fnc normaal alleen 1 keer de sub items uitvoert, nu de mogelijkheid heeft om aangeroepen te worden met een argument, dit argument wordt dan gebruikt om de sub items uit te voeren(meer naar een functie), nu is de syntax van de fnc als volgt:
```- fnc_[functienaam]_[functieargument naam in functie]``` - gebruikt om een functie te defineren, dit is een folder
```- run_[functienaam]_[functieargument]_[functie return variable].LNK``` - gebruikt om een functie aan te roepen, de functie return variable is de variable waar de return van de functie in wordt opgeslagen
```-rtn_[functieargument].LNK``` - gebruikt om een functie te returnen
momenteel is het alleen ondersteund type voor een return type momenteel: int
voorbeeld voor een functie definitie in dirst:
```
    fnc_voorbeeldFunctie_voorbeeldArgument
    #functie code
    rtn_voorbeeldArgument.lnk
```
en een voorbeeld aanroep van die functie is als volgt:
```
    civ_voorbeeldReturnVariable.csv #maak een variable aan om de return van de functie in op te slaan
    civ_voorbeeldArgument.csv #maak een variable aan om aan de functie mee te geven
    run_voorbeeldFunctie_voorbeeldArgument_voorbeeldReturnVariable.lnk
```

# === README CHECKLIST ===
Gekozen taal: [Dirst](https://esolangs.org/wiki/Dirst)

Dirst is Turing-compleet omdat: 
    - de taal ondersteunin heeft voor opslag in een tape, met het lezen van de head, het wijzigen van de head en het verplaatsen naar links of rechts van de head. Waarbij de tape oneindig is.(https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/turing-machine/one.html)
    - if statements ondersteund, loops ondersteund en variablen ondersteund zonder een functioneel limiet(anders dan geheugen limiet van de computer)
    - de taal staat tussen de turing complete talen op de esolangs website(https://esolangs.org/wiki/Dirst)

Code is geschreven in functionele stijl.
ik heb er goed op gelet dat de code in functionele stijl is geschreven, zo zijn er geen globale variablen gebruikt en zijn er geen loops gebruikt, maar alleen recursie.
wel was het lastig met het rekening houden met hoe erg functioneel de code zou moeten zijn omdat bijvoorbeeld deze code de dirst code leest uit een file en io is strict genoemen een side effect en niet toegestaan. Ook was het lastig om te vinden of het overschrijven van een variable een side effect is of niet, hierop heb ik in de code nu wel rekening mee gehouden en aangepast.

voor alle mogelijkheden van de Dirst taal, zie documentatie van de taal(https://esolangs.org/wiki/Dirst) en de voorbeelden in de [/UnitTests/TestCode] folder

Loops Voorbeeld: [/UnitTests/TestCode/sommig.txt] - [6-9] - lpc keyword is: "Loop through directory subitems while the specified integer value is not zero"

functies Voorbeeld: [/UnitTests/TestCode/evenOdd.txt] - [20] - fnc keyword is aangepast zie hierboven

Bevat:

Classes met inheritance: bijvoorbeeld [/Parser/tokens.py] - alle tokens zijn classes met inheritance van de hoofd token classe(met als tussenstap de dirst-subset classes zoals Dat en csv) en [/Parser/parser.py] - alle statements zijn classes met inheritance van de hoofd SimpleStatement classe

Object-printing voor elke class: [ja]

Decorator: functiedefinitie op [Tools/tools.py] - [23](functie: function_debug_printing), toegepast op [Runner/runner.py] - [420, 411, 392, 50] - [Parser/parser.py]

Type-annotatie: Haskell-stijl in comments: [ja]; Python-stijl in functiedefinities: [ja]

Minstens drie toepassingen van hogere-orde functies:

1. [/Lexer/lexer.py] - [800] - map
2. [/Tools/tools.py] - [9] - filter
3. [/Parser/parser.py] - [61] - map

Interpreter-functionaliteit Must-have:

Functies: [meer per file] - zie [/UnitTests/TestCode/evenOdd.txt] - gebruik makend van de aangepaste fnc keyword

Functie-parameters kunnen aan de interpreter meegegeven worden door de run instructie zie hierboven

Functies kunnen andere functies aanroepen: zie voorbeeld [/UnitTests/TestCode/evenOdd.txt]

Functie resultaat wordt op de volgende manier weergegeven: door te printen naar de console gebruik makend van de dsi instructie

Interpreter-functionaliteit (should/could-have):

door diederik is deze taal goedgekeurd op voorwaarde dat er een functie aanroep mogelijkheid is, dit is toegevoegd zie hierboven voor een voorbeeld van een aanroep zie [/UnitTests/TestCode/evenOdd.txt]

# voorbeeld code taal
zie website van de taal: https://esolangs.org/wiki/Dirst#Sample_Programs en [/UnitTests/TestCode] folder waar ook voorbeelden van de dirst website staan

