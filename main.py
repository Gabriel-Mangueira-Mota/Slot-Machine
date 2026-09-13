import random
import time

niquel = ["🍓", "🍇", "🥭", "💣", "🔄"]

strawberry = "🍓🍓🍓"
grape = "🍇🍇🍇"
mango = "🥭🥭🥭"
bomb = "💣💣💣"
retry = "🔄🔄🔄"


# BANCO

while True:

    bank_input = input("\nSelect the initial value of your bank: ")

    if bank_input.upper() == "VIP":
        vip = True
        value = int(input("VIP mode! Select the value of your bank: "))
        break

    else:
        vip = False

        try:
            value = int(bank_input)

            if value <= 0:
                print("The bank value must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a number.")


bank = value


# VIDA DO JOGADOR

while True:

    if bank <= 0:
        print("\n💀 YOU BROKE!")
        print("Your bank is empty.")
        break

    house = 0

    print("\n==============================")
    print("          THE BANK")
    print("==============================")
    print(f"Bank: {bank}")
    print("==============================")

    print("\n1 - Deposit money in the house")
    print("2 - Leave")

    option = input("\nSelect an option: ")

    if option == "2":
        print("\nReturning to the bank...")
        print(f"🏦 Final bank value: {bank}")
        break

    elif option != "1":
        print("Invalid option.")
        continue


    # DEPOSITO NA CASA

    while True:

        try:
            deposit = int(input("\nHow much do you want to put in the house? "))

            if deposit <= 0:
                print("The value must be greater than 0.")

            elif deposit > bank:
                print("Insufficient funds.")

            else:
                bank = bank - deposit
                house = house + deposit

                print(f"\n🏦 Bank: {bank}")
                print(f"🎰 House: {house}")

                break

        except ValueError:
            print("Please enter a number.")


    # EXPLICACAO

    print("\nGame rules:\n")

    time.sleep(1)
    print("🍓🍓🍓 = value x 2")
    time.sleep(1)

    print("🍇🍇🍇 = value x 5")
    time.sleep(1)

    print("🥭🥭🥭 = value x 10")
    time.sleep(1)

    print("💣💣💣 = Game Over")
    time.sleep(1)

    print("🔄🔄🔄 = Retry")
    time.sleep(1)

    print("🍓🍇🥭 Random = Game Over")

    print("\nChances:")

    if vip:
        print("🍓 Strawberry = VIP chance")
        print("🍇 Grape = VIP chance")
        print("🥭 Mango = VIP chance")
        print("💣 Bomb = reduced chance")
        print("🔄 Retry = normal chance")
    else:
        print("🍓 Strawberry = 25%")
        print("🍇 Grape = 15%")
        print("🥭 Mango = 10%")
        print("💣 Bomb = 25%")
        print("🔄 Retry = 25%")


    # APOSTA

    while house > 0:

        try:
            game_value = int(input("\nSelect the value you want to bet: "))

            if game_value <= 0:
                print("The bet must be greater than 0.")
                continue

            if game_value > house:
                print("Insufficient funds in the house.")
                continue

            break

        except ValueError:
            print("Please enter a number.")


        # GIROS

    while True:

        try:
            spins = int(input("\nHow many spins do you want? "))

            if spins <= 0:
                print("The number of spins must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a number.")


    # GIROS AUTOMATICOS

    for spin in range(spins):

        if house <= 0:
            print("\n💸 The house has no more credits.")
            break

        if game_value > house:
            game_value = house

        print("\n==============================")
        print(f"           SPIN {spin + 1}")
        print("==============================")

        print("🎰 Spinning...")

        time.sleep(0.5)

        # PRIMEIRA PARTE DO GIRO

        for i in range(5):

            roll_one = random.choice(niquel)
            roll_two = random.choice(niquel)
            roll_tree = random.choice(niquel)

            print(f"\r  {roll_one}   {roll_two}   {roll_tree}", end="")

            time.sleep(0.3)

        print()

        # SEGUNDA PARTE DO GIRO

        for i in range(5):

            roll_one = random.choice(niquel)
            roll_two = random.choice(niquel)
            roll_tree = random.choice(niquel)

            print(f"\r  {roll_one}   {roll_two}   {roll_tree}", end="")

            time.sleep(0.3)

        print()

        # RESULTADO FINAL

        if vip:

            # VIP aumenta as chances dos resultados bons

            vip_niquel = [
                "🍓", "🍓", "🍓",
                "🍇", "🍇",
                "🥭",
                "💣",
                "🔄"
            ]

            roll_one = random.choice(vip_niquel)
            roll_two = random.choice(vip_niquel)
            roll_tree = random.choice(vip_niquel)

        else:

            roll_one = random.choice(niquel)
            roll_two = random.choice(niquel)
            roll_tree = random.choice(niquel)


        game_result = roll_one + roll_two + roll_tree

        print(f"\n[ {roll_one} ] [ {roll_two} ] [ {roll_tree} ]")


        # RESULTADOS

        if game_result == strawberry:

            prize = game_value * 2

            house = house - game_value
            house = house + prize

            print("\n🎉 Congratulations!")
            print(f"🍓 Strawberry! You won {prize}!")

        elif game_result == grape:

            prize = game_value * 5

            house = house - game_value
            house = house + prize

            print("\n🥳 CONGRATULATIONS!")
            print(f"🍇 Grape! You won {prize}!")

        elif game_result == mango:

            prize = game_value * 10

            house = house - game_value
            house = house + prize

            print("\n🚀 BIG WIN!")
            print(f"🥭 Mango! You won {prize}!")

        elif game_result == bomb:

            house = house - game_value

            print("\n💣 BOOM!")
            print("You lost your bet.")

        elif game_result == retry:

            print("\n🔄 FREE RETRY!")
            print("You can try again for free.")

        else:

            house = house - game_value

            print("\n💔 You lost your bet.")


        print(f"\n🏦 Bank: {bank}")
        print(f"🎰 House: {house}")

        time.sleep(1)


    # FIM DOS GIROS

    print("\n==============================")
    print("       END OF SPINS")
    print("==============================")

    print(f"🏦 Bank: {bank}")
    print(f"🎰 House: {house}")

    print("\n1 - Transfer house to bank")
    print("2 - Continue with the house")
    print("3 - Leave")

    option = input("\nSelect an option: ")


    if option == "1":

        bank = bank + house
        house = 0

        print("\n💰 Money transferred!")
        print(f"🏦 New bank value: {bank}")

    elif option == "2":

        print("\nYou continue with the money in the house.")

        if house <= 0:
            print("The house is empty.")
            print("Returning to the bank.")

    elif option == "3":

        bank = bank + house
        house = 0

        print("\nReturning to the bank...")
        print(f"🏦 Final bank value: {bank}")

        break