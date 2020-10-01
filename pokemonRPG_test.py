import pokemonRPG.py

def test_show():
    testlines = '''
Welcome to Pokemon!
========
Commands:
  go [direction]
  talk [item]
========
You're objective is to beat the
Vermillion Gym Leader!
========
Defeat Wild Pokemon, get items, level up!
'''
    assert showInstructions() == testlines
