# Dirst scripting Interpreter

A python Dirst scripting interpreter

De Dirst taal is een een programeertaal waarvan de code bestaat namen van folders en bestanden. In deze interpreter is het script gedeelte geïmplementeerd.

Deze python Dirst scripting interpreter is gebaseerd op de [Dirst programming language](https://esolangs.org/wiki/Dirst) and ondersteund een deel van alle functies van de taal met een toevoeging om functies uit te voeren.
Ook ondersteund deze interpreter alleen het script gedeelte van de taal en helaas niet het folder gedeelte van de taal.

In this project is has also added functions calls in the project(an way to declare functions and run them, with an argument and return value)

## installatie

clone deze repository
installeer python 3.11 (https://www.python.org/downloads/) (oudere versies werken niet wegens het gebruiken van de self keyword in type notatie)
installeer de requirements met ```pip install -r requirements.txt```

## gebruik

het gebruik van deze interpreter is als volgt:
- als er console input gevraagd is:
    "python Dirst_cli.py -f [pad naar dirst script vanuitgaand van de hudige workspace] -i [console input]"
- als er geen console input gevraagd is:
    "python Dirst_cli.py -f [pad naar dirst script vanuitgaand van de hudige workspace]"
een voorbeeld aanroep van de greeter programma:
```python Dirst_cli.py -f UnitTests/TestCode/greeter.txt -i "Pim"```

## Requirements

## === ADDED LANGUAGE OPERATORS ===

### waarom?

Om aan de eisen van de atp opdracht te voldoen heb ik 1 operator veranderd en 2 toegevoegd.

### added operators

Veranderd aan de taal is dat de instructie: fnc normaal alleen 1 keer de sub items uitvoert, nu de mogelijkheid heeft om aangeroepen te worden met een argument, dit argument wordt dan gebruikt om de sub items uit te voeren(meer naar een functie), nu is de syntax van de fnc als volgt:
```- fnc_[functienaam]_[functieargument naam in functie]``` - gebruikt om een functie te defineren, dit is een folder
```- run_[functienaam]_[functieargument]_[functie return variable].LNK``` - gebruikt om een functie aan te roepen, de functie return variable is de variable waar de return van de functie in wordt opgeslagen
```-rtn_[functieargument].LNK``` - gebruikt om een functie te returnen(momenteel alleen support voor return type int)
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
Ik heb er goed op gelet dat de code in functionele stijl is geschreven, zo zijn er geen globale variablen gebruikt en zijn er geen loops gebruikt, maar alleen recursie.
wel was het lastig met het rekening houden met hoe erg functioneel de code zou moeten zijn omdat bijvoorbeeld deze code de dirst code leest uit een file en io is strict genoemen een side effect en niet toegestaan. Ook was het lastig om te vinden of het overschrijven van een variable een side effect is of niet, hierop heb ik in de code nu wel rekening mee gehouden en aangepast.


Voor alle mogelijkheden van de Dirst taal, zie documentatie van de taal(https://esolangs.org/wiki/Dirst) en de voorbeelden in de [/UnitTests/TestCode] folder.
Niet alle mogelijkheden van de taal zijn geïmplementeerd. Zie kop "niet geïmplementeerd" onderaan in deze readme.

Loops Voorbeeld: [/UnitTests/TestCode/sommig.txt] - [6-9] - lpc keyword is: "Loop through directory subitems while the specified integer value is not zero"

functies Voorbeeld: [/UnitTests/TestCode/evenOdd.txt] - [20] - fnc keyword is aangepast zie hierboven

Bevat:

Classes met inheritance: bijvoorbeeld [/Parser/tokens.py] - alle tokens zijn classes met inheritance van de hoofd token classe(met als tussenstap de dirst-subset classes zoals Dat en csv) en [/Parser/parser.py] - alle statements zijn classes met inheritance van de hoofd SimpleStatement classe

Object-printing voor elke class: [ja]

Decorator: functiedefinitie op [Tools/tools.py] - [23](functie: function_debug_printing), toegepast op [Runner/runner.py] - [420, 411, 392, 50] - [Parser/parser.py]
de decorator functie is aan te zetten door de variable: "DEBUG_PRINTING" op regel 4 van de tools.py op true te zetten, dan word er bij elke functie ervoor en erna de status van de functie argumenten is. Dit is handig voor het debuggen van de code.

Type-annotatie: Haskell-stijl in comments: [ja]; Python-stijl in functiedefinities: [ja]

Minstens drie toepassingen van hogere-orde functies:

1. [/Lexer/lexer.py] - [800] - map
2. [/Tools/tools.py] - [9] - filter
3. [/Parser/parser.py] - [61] - map

Interpreter-functionaliteit Must-have:

Functies: [meer per file(kan niet cross )] - zie [/UnitTests/TestCode/evenOdd.txt] - gebruik makend van de aangepaste fnc keyword(de toevoeging aan de taal)

Functie-parameters kunnen aan de interpreter meegegeven worden door de run instructie zie hierboven(zie kopje gebruik)

Functies kunnen andere functies aanroepen: zie voorbeeld [/UnitTests/TestCode/evenOdd.txt]

Functie resultaat wordt op de volgende manier weergegeven: door te printen naar de console

Interpreter-functionaliteit (should/could-have):

door diederik is deze taal goedgekeurd op voorwaarde dat er een functie aanroep mogelijkheid is, dit is toegevoegd zie hierboven, voor een voorbeeld van een aanroep van de toevoeging zie file: - [/UnitTests/TestCode/evenOdd.txt]

## voorbeeld code taal

zie website van de taal: https://esolangs.org/wiki/Dirst#Sample_Programs en [/UnitTests/TestCode] folder waar ook voorbeelden van de dirst website staan

## Testen

de testen zijn te vinden in de [/UnitTests] folder, deze testen zijn geschreven in python en gebruiken de unittest library van python.(bij het gebruik van vscode kan op het kopje testing geklikt worden om alle testen makkeijk te runnen)
bij niet het gebruik van vscode zie de documentatie van de unittest library van python voor het runnen van de testen.(https://docs.python.org/3/library/unittest.html)
de testen zijn geschreven om de functionaliteit van de lexer, parser en runner te testen

de testen die zijn geschreven zijn nuttig voor de kwaliteit van de code omdat bijvoorbeeld bij de lexer word er uitbundig getest of de lexer de juiste tokens terug geeft voor de juiste input, dit is belangrijk omdat de parser en runner afhankelijk zijn van de lexer en als de lexer niet goed werkt dan werken de parser en runner ook niet goed, dit maakt dat als er fouten in de implementatie van de lexer zitten deze fouten snel gevonden worden en opgelost kunnen worden. Ook zijn er testen om te controleren hoe de lexer reageert met foute input, zoals een extra spatie of tab of een onbekend bestand of een file zonder geldige bestand extensie. Door deze dingen te testen kan er gecontroleerd worden of de lexer de fouten eruit haald en kan continu getest worden of veranderingen in de code geen fouten veroorzaken.

## niet geïmplementeerd

Niet alle statements van deze taal zijn geïmplementeerd, zie voor alle statements die geimplementeerd en niet zijn [/Parser/parser.py] bij de functie: parseCodeBlock (regel: ~544), bij een geen implementatie van een statement wordt de class NotImplemented gebruikt.

Ook is er tijdens het ontwikkelen er voor gekozen om de consoleinput vooraf aan het runnen van de functie mee te geven. Dit is omdat het een side effect is en niet functioneel geprogrameerd kan.

## video

[![Dirst interpreter video]({https://img.youtube.com/vi/XQOu8LEz-X4/0.jpg})](https://youtu.be/XQOu8LEz-X4)
