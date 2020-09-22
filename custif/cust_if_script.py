poke = ''
pType = ''
gen = ''
appear = ''

while poke == '':
    while pType != 'fire' and pType != 'grass' and pType != 'water' and pType != 'electric':
        print("It\'s dangerous to go alone! What's your favorite basic Pokemon type?")
        pType = input("Valid basic types are 'Fire', 'Grass', 'Water', and 'Electric': ").lower()
    while gen != 'classic' and gen != 'modern' and gen != 'futuristic':
        print("What generation of pokemon do you like?")
        gen = input("Valid generations are 'Classic', 'Modern', or 'Futuristic': ").lower()
    while appear != 'cute' and appear != 'cool' and appear != 'scary':
        print("What kind of pokemon appearence do you like?")
        appear = input("Valid appearences are 'Cute', 'Cool', or 'Scary': ").lower()
    if pType == 'fire':
        if gen == 'classic':
            if appear == 'cute':
                poke = 'Charmander'
            elif appear == 'cool':
                poke = 'Charmeleon'
            else:
                poke = 'Charizard'
        elif gen == 'modern':
            if appear == 'cute':
                poke = 'Cyndaquil'
            elif appear == 'cool':
                poke = 'Quilava'
            else:
                poke = 'Typhlosion'
        else:
            if appear == 'cute':
                poke = 'Tepig'
            elif appear == 'cool':
                poke = 'Pignite'
            else:
                poke = 'Emboar'
    elif pType == 'grass':
        if gen == 'classic':
            if appear == 'cute':
                poke = 'Bulbasaur'
            elif appear == 'cool':
                poke = 'Ivysaur'
            else:
                poke = 'Venusaur'
        elif gen == 'modern':
            if appear == 'cute':
                poke = 'Chikorita'
            elif appear == 'cool':
                poke = 'Bayleef'
            else:
                poke = 'Meganium'
        else:
            if appear == 'cute':
                poke = 'Snivy'
            elif appear == 'cool':
                poke = 'Servine'
            else:
                poke = 'Serperior'
    elif pType == 'water':
        if gen == 'classic':
            if appear == 'cute':
                poke = 'Squirtle'
            elif appear == 'cool':
                poke = 'Wartortle'
            else:
                poke = 'Blastoise'
        elif gen == 'modern':
            if appear == 'cute':
                poke = 'Totodile'
            elif appear == 'cool':
                poke = 'Croconaw'
            else:
                poke = 'Feraligatr'
        else:
            if appear == 'cute':
                poke = 'Oshawott'
            elif appear == 'cool':
                poke = 'Dewott'
            else:
                poke = 'Samurott'
    else:
        if gen == 'classic':
            if appear == 'cute':
                poke = 'Pikachu'
            elif appear == 'cool':
                poke = 'Jolteon'
            else:
                poke = 'Electrobuzz'
        elif gen == 'modern':
            if appear == 'cute':
                poke = 'Pichu'
            elif appear == 'cool':
                poke = 'Ampharos'
            else:
                poke = 'Raikou'
        else:
            if appear == 'cute':
                poke = 'Emolga'
            elif appear == 'cool':
                poke = 'Zeraora'
            else:
                poke = 'Galvantula'
print(f"You choose a {appear} {gen} {pType} type Pokemon! You're Pokemon is a {poke}!")
