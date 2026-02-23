import pandas as pd
import numpy
import json
import requests

API_URL = "https://pokeapi.co/api/v2/pokemon?limit=10000&offset=0"

def getAPIData():
    response = requests.get(API_URL)

    return response

if __name__ == "__main__":
    apiData = getAPIData()

    # If response code equals 200...
    if(apiData.status_code == 200):

        # Takes the response in as JSON.
        pokemonData = apiData.json()

        # Creates the .json locally, defined as 'f'.
        with open("src\data\pokemon_data.json", 'w') as f:
            if(f):
                print("File already exists, moving on...")
            else:
                # Adding in the "indent" and "ensure_ascii" gives a pretty print to the dumped JSON.
                json.dump(pokemonData, f, ensure_ascii=False, indent=4)

        pokemon_df = pd.json_normalize(pokemonData)

        print(pokemon_df)
    else:
        # Prints any errors that may occur
        print("Error: " + str(apiData.status_code))
