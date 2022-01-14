def position():
    """
    - frågar om en väska position för byte
    - vid felaktig val (ogiltig position) skrivs "felaktig val"
    - vid annat svar skrivs "Ej ett position"
    """
    verktygets_position = f"\nVilken position har verktyget som du vill byta? första [0] eller andra [1] eller tredje [2] eller fjärde [3] eller femte [4] → "
    while True:
        try:
            svar = int(input(verktygets_position))
        except ValueError:
            print("Ej en position")
            continue
        else:
            if 0 <= svar <= 5:
                return svar
            else:
                print("\nFelaktig val\n")
