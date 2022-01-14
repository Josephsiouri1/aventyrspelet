def ta_potion(hp, antal):
    """
    - tar emot två variablar
    - om antal är större än 0 kör funktionen
    - annars inget förändras med variablerna
    - det kontrollerar om hp inte blir högre än 10
    - om inte större än 100 adderas 10 till hp och 1 minskar från antalet
    - annars inget händer
    """
    if antal > 0:
        if hp + 10 > 100:
            print("\nDin hp är tillräckligt hög.")
            return hp, antal
        else:
            antal = antal - 1
            hp = hp + 10
            print("\nDin hp gick upp med 10.")
            return hp, antal
    else:
        print("\nDu har inga potions kvar!")
        return hp, antal
