# Dirst_Interpreter

A python Dirst interpreter

This python Dirst interpreter is based on the [Dirst programming language](https://esolangs.org/wiki/Dirst)

In this project is has also added functions calls in the project

# Requirements

# === ADDED LANGUAGE OPERATORS ===
veranderd aan de taal is dat de instructie: fnc normaal alleen 1 keer de sub items uitvoert, nu de mogelijkheid heeft om aangeroepen te worden met een argument, dit argument wordt dan gebruikt om de sub items uit te voeren(meer naar een functie), nu is de syntax van de fnc als volgt:
```- fnc_[functienaam]_[functieargument naam in functie]``` - gebruikt om een functie te defineren
```- call_[functienaam]_[functieargument]_[functie return variable].LNK``` - gebruikt om een functie aan te roepen, de functie return variable is de variable waar de return van de functie in wordt opgeslagen
```-rtn_[functieargument].LNK``` - gebruikt om een functie te returnen
door de functie def_ te gebruiken kan je een functie definiëren, de functie call_ kan je gebruiken om een functie aan te roepen
de functie deff en call kan als volgt gebruikt worden:
```- def_[functienaam]_[functieargument type]_[functieargument] ``` - gebruikt om een functie te defineren
```- call_[functienaam]_[functieargument]``` - gebruikt om een functie aan te roepen
```-rtn_[functieargument]``` - gebruikt om een functie te returnen
ondersteunende type is momenteel: int
voorbeeld:
```- def_ print_int_1```
```- call_ print_int_1_1```
```-rtn 1```


# === README CHECKLIST ===
Gekozen taal: [Dirst](https://esolangs.org/wiki/Dirst) moet nog werken aan bewijs

Turing-compleet omdat:

Code is geschreven in functionele stijl.

Taal ondersteunt:

Loops? Voorbeeld: [/Examples/Fib_seq.txt] - [7-12]

Goto-statements? Voorbeeld: [/Examples/even.txt] - [3]

Lambda-calculus? Voorbeeld: [/Examples/even.txt] - [3](denk ik?)

Bevat:

Classes met inheritance: bijvoorbeeld [tokens.py] - [36-40]

Object-printing voor elke class: [ja]

Decorator: functiedefinitie op (nu nog niet aanwezig) [file] - [regel], toegepast op [file] - [regel]

Type-annotatie: Haskell-stijl in comments: [ja]; Python-stijl in functiedefinities: [ja/nee]

Minstens drie toepassingen van hogere-orde functies:

1. [lexer.py] - [477] - map
2. [file] - [regel]
3. [file] - [regel]

Interpreter-functionaliteit Must-have:

Functies: [één per file / meer per file]

Functie-parameters kunnen aan de interpreter meegegeven worden door:

Functies kunnen andere functies aanroepen: zie voorbeeld [file] - [regel]

Functie resultaat wordt op de volgende manier weergegeven:

Interpreter-functionaliteit (should/could-have):

[Gekozen functionaliteit] geïmplementeerd door middel van de volgende functies: a) [functie] in [file] op regel [regel]

[Extra functionaliteit overlegd met docent, goedkeuring: datum e-mail; overeengekomen max. aantal punten: X]
