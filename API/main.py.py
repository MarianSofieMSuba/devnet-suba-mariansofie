import requests

pokemon = yeah

match pokemon:
    case 1:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
        info = response.json()

        height = info.get('height')
        weight = info.get('weight')

        print("This has a height of ", height, " and a weight of ", weight )

    case 2:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
        info = response.json()

        height = info.get('height')
        weight = info.get('weight')

        print("This has a height of ", height, " and a weight of ", weight )

    case 3:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
        info = response.json()

        height = info.get('height')
        weight = info.get('weight')

        print("This has a height of ", height, " and a weight of ", weight )

    case 4:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
        info = response.json()

        height = info.get('height')
        weight = info.get('weight')

        print("This has a height of ", height, " and a weight of ", weight )

    case 5:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
        info = response.json()

        height = info.get('height')
        weight = info.get('weight')

        print("This has a height of ", height, " and a weight of ", weight )

