import random as rand
import time
from Player import Player
from Items import Items
from position import position
from ta_potion import ta_potion


def main():
    player = Player(input("\nSkriv din karaktärs namn här → "),
                    [50], 100, ["Kniv"], 1)

    kista_1 = Items("Svärd", rand.randint(30, 90))
    kista_2 = Items("Lazer", rand.randint(35, 100))
    kista_3 = Items("Gevär", rand.randint(40, 110))
    kista_4 = Items("Hammare", rand.randint(10, 50))
    kistor = [kista_1, kista_2, kista_3, kista_4]

    antal_potions = 3
    print(f"\nHej {player.name}! Välkomen till denna spännande äventyr.")

    while True:

        svar = input(
            "\nVad vill du göra: titta i inventory [I], titta på statusen [S], gå igenom dörren framför dig [F], gå igenom dörren till höger [H] eller gå igenom dörren till vänster [V], eller ta en potion [P] → ")
        if svar.lower() == "s":
            print(
                f"\nDin status just nu ser ut så här → \n \t* HP: {player.hp} \n \t* Styrka: {sum(player.strength)} \n \t* Nivå: {player.level} \n \t* Antal potions: {antal_potions}\n")

        elif svar.lower() == "i":
            if len(player.inventory) == 1:
                print(
                    f"\nDin väska innehåller följande verktyg: \n \t* {player.inventory[0], player.strength[0]}")
            elif len(player.inventory) == 2:
                print(
                    f"\nDin väska innehåller följande verktyg: \n \t* {player.inventory[0], player.strength[0]} \n \t* {player.inventory[1], player.strength[1]}")
            elif len(player.inventory) == 3:
                print(
                    f"\nDin väska innehåller följande verktyg: \n \t* {player.inventory[0], player.strength[0]} \n \t* {player.inventory[1], player.strength[1]} \n \t* {player.inventory[2], player.strength[2]}")
            elif len(player.inventory) == 4:
                print(
                    f"\nDin väska innehåller följande verktyg: \n \t* {player.inventory[0], player.strength[0]} \n \t* {player.inventory[1], player.strength[1]} \n \t* {player.inventory[2], player.strength[2]} \n \t* {player.inventory[3], player.strength[3]}")
            else:
                print(
                    f"\nDin väska innehåller följande verktyg: \n \t* {player.inventory[0], player.strength[0]} \n \t* {player.inventory[1], player.strength[1]} \n \t* {player.inventory[2], player.strength[2]} \n \t* {player.inventory[3], player.strength[3]} \n \t* {player.inventory[4], player.strength[4]} ")

        elif svar.lower() == "p":
            player.hp, antal_potions = ta_potion(player.hp, antal_potions)

        elif svar.lower() == "f" or svar.lower() == "v" or svar.lower() == "h":
            bakom_dorren = rand.randint(1, 3)
            if bakom_dorren == 1:
                if player.level < 3:
                    monster_styrka = rand.randint(30, 250)
                elif player.level < 5:
                    monster_styrka = rand.randint(50, 350)
                else:
                    monster_styrka = rand.randint(100, 420)
                monster_skada = rand.randint(1, 5)
                if monster_styrka > sum(player.strength):
                    if player.hp - monster_skada > 0:
                        print(
                            f"\nDet fanns ett monster bakom dörren och du hade inte till räckligt styrka för att översegra den. Din hp gick ner till {player.hp - 1}")
                        player.new_hp(player.hp-monster_skada)
                    else:
                        print(
                            "Monstern har besegrad dig och gjort att din hp gick ner till 0. Du har förlurat spelet.\n")
                        time.sleep(1.5)
                        spela_igen = input(
                            "Vill du spela igen: ja [j] annars ange vilken knapp som helst → ")
                        if spela_igen.lower() == "j":
                            main()
                        else:
                            break

                elif monster_styrka < sum(player.strength):
                    print(
                        f"\nDu har mött en monster med lägre styrka än dig. Du har besegrat monstern, du gick upp till nivå: {player.level + 1}")
                    player.new_level(player.level + 1)
                    if player.level == 6:
                        extra_potion = rand.randint(1, 2)
                        antal_potions = antal_potions + extra_potion
                        print(f"\nDu har fått {extra_potion} extra potion")
                    if player.level == 10:
                        print(
                            f"Grattis {player.name}! Du har nått nivå 10 vilket betyder att du har vunnit.\n")
                        time.sleep(1.5)
                        spela_igen = input(
                            "Vill du spela igen ja [j] annars ange vilken knapp som helst → ")
                        if spela_igen.lower() == "j":
                            main()
                        else:
                            break

                else:
                    print(
                        "\nDu träffade en monster med samma styrka som dig. Inget hände.")

            elif bakom_dorren == 2:
                namn_pa_verktyg = rand.choice(kistor).name
                styrka = rand.choice(kistor).strength_bonus
                print(
                    f"\nBakomen denna dörr finns en kista med verktyg som du kan använda i vidare strider. Den kista innehåller ett verktyg med namnet: {namn_pa_verktyg} och styrkan: {styrka}")

                if len(player.strength) == 5:
                    print("\nDin inventory är full du kan inte lägga till verktyget.\n")

                    while True:
                        byta = input(
                            f"Vill du byta en av dina verktyg mot den? ja [J] eller nej [N]. Dina verktyg har följande styrka: {player.strength} → ")
                        if byta.lower() == "j":
                            verktygets_position = position()
                            player.strength.pop(verktygets_position)
                            player.inventory.pop(verktygets_position)
                            player.strength.append(styrka)
                            player.inventory.append(namn_pa_verktyg)
                            print(
                                "\nDu har nu bytt ett av dina verktyg mot ett nytt.")
                            break
                        elif byta.lower() == "n":
                            break
                        else:
                            print("\nFelaktig val\n")

                else:
                    player.inventory.append(namn_pa_verktyg)
                    player.strength.append(styrka)

            else:
                if player.level < 3:
                    forlorade_hp = rand.randint(2, 12)
                elif player.level < 5:
                    forlorade_hp = rand.randint(4, 14)
                elif player.level < 8:
                    forlorade_hp = rand.randint(5, 16)
                else:
                    forlorade_hp = rand.randint(6, 20)
                if player.hp - forlorade_hp > 0:
                    print(
                        f"\nDu har hamnat i en fälla som gjort att du har förlurat {forlorade_hp} hp du har nu {player.hp-forlorade_hp} hp kvar.")
                    player.new_hp(player.hp-forlorade_hp)
                else:
                    print(
                        "\nDu stöt på en fälla som gjort att din HP gick ner till 0. Du har förlurat spelet.\n")
                    time.sleep(1.5)
                    spela_igen = input(
                        "Vill du spela igen ja [j] annars ange vilken knapp som helst → ")
                    if spela_igen.lower() == "j":
                        main()
                    else:
                        break

        else:
            print("\nFelaktig val")


main()
