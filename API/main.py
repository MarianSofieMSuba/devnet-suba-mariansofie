import requests
import random

# -------
# UI for the game using the terminal colors, that also includes majority of the game for decoration purposes
# -------

def pokemon_ui(): # 3

    print("\033[1;93mPokemon Guessing Minigame\033[0m\n\n\033[1;96mHow well can you guess each pokemon based on their:\n> Height\n> Weight\n> Type\n> Ability\n\nYou only have 3 guesses to win, Good luck!\033[0m\n\n\033[0;32m[1] START\033[0m\n\033[0;31m[2] EXIT\033[0m")

# -------
# This will check for the status code by using request.get to get the pokemon api of their height, weight, types and abilities
# their specific data using a quary will be specified inside a dictionary of poke_data
# -------


def poke_info(poke_stats): # 4

    checker = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{poke_stats}" # way simpler than doing each individual pokemon name from my old case match format
                          )

    if checker.status_code == 200:

        print("\033[1;92mAPI connection successful!\nStatus code:\033[0m", checker.status_code,"\n\n----")
        info = checker.json()

        height = info["height"]
        weight = info["weight"]

        # Uncertain whether I'll do two or three more but for simplicity case I'll do one
        pokemon_type = info["types"][0]["type"]["name"]
        ability = info["abilities"][0]["ability"]["name"] 

        poke_data = {
            "name": poke_stats,
            "height": height,
            "weight": weight,
            "type": pokemon_type,
            "ability": ability
        }

        return poke_data

    else:
        print("\033[1;91mThe API connection failed!\nStatus code:\033[0m", checker.status_code,"\n\n----")
        return None

# -------
# actual gameplay of the game, poke_list was added here so it could actually randomize the pokemons
# then added an for loop with an if statement just in case it returned a 400 from poke_info which means it failed to retrieve the API and will not start the game
# inside the nested for loop the to prevent further more errors for the answer input, added a strip() to remove empty spaces then added a lower() to keep all letters in lowercase
# added capitalize() to turn the name into an uppercase letter soley for UI sake
# added a for loop counter to count the retries of the user, they are limited to 3 for each pokemon
# -------


def the_guessing_game(): # 5

    poke_list = [
        "pikachu",
        "charmander",
        "butterfree",
        "beedrill",
        "eevee"
                ]
    
    random.shuffle(poke_list)

    for pokemon in poke_list:
        poke_data = poke_info(pokemon)

        if poke_data is None:
            print("\033[1;91mUnable to start the game due to an API issue.\n\033[0m\n----")
            return
        
        print("\n\033[1;93mWHO IS THAT POKEMON?\033[0m\n")

        print("\033[1;96mThis pokemon is", poke_data["height"], "tall, it weighs around", poke_data["weight"], "\033[0m")
        print("\033[1;96mIt is a", poke_data["type"], "type and one of its abilities is", poke_data["ability"],"\033[0m")

        for guess in range(3):

            print(f"\n\033[0;35mTries {guess + 1}/3\033[0m")
            answer = input("> ").strip().lower()


            if answer == poke_data["name"]:

                print("\n\033[0;33mDing! ding! ding!\033[0m\n")
                break

            else:

                print("\n\033[0;31mNope, not correct! Try again.\033[0m\n")

        else:

            print("\n\033[1;91mThe Pokemon was:", poke_data["name"].capitalize(),"\nYou Lose!\n\n\033[0m")
            return

    print("\n\033[1;93mYou guessed all the 5 Pokemons!\nYou Win!\n\n\033[0m\n-----------")

# -------
# It prints the UI and uses a while loop to keep the game running
# as long as the user wants to exit the game
# However it will cause an error if the input is a string
# -------

def main_start(): # 2
    while True:

        pokemon_ui()

        game_of_choice = int(input("\n>"))

        if game_of_choice == 1:
            the_guessing_game()

        elif game_of_choice == 2:
            print("\033[1;91mExiting...\033[0m")
            break

        else:
            print("\033[1;91mThere are only two options, pick either [1] Start or [2] Exit\033[0m\n\n----")

# -------
# The entire game runs here
# vvvvvvv

main_start() # 1

