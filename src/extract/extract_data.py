import pandas as pd
import requests
import numpy
import json
import os

API_URL = "https://pokeapi.co/api/v2/pokemon?limit=10000&offset=0"
FILEPATH = "src\data\pokemon_data.json"

def getAPIData():
    response = requests.get(API_URL)

    return response

def getFileSize(filePath: str) -> int:

    fileSize = os.path.getsize(filePath)

    return fileSize


if __name__ == "__main__":
    apiData = getAPIData()

    # If response code equals 200...
    if(apiData.status_code == 200):

        # Takes the response in as JSON.
        pokemonData = apiData.json()

        try:
            jsonFileSize = getFileSize(FILEPATH)

            if(jsonFileSize == 0):
                # Creates the .json locally, defined as 'f'.
                with open(jsonFileSize, 'w') as f:
                    # Adding in the "indent" and "ensure_ascii" gives a pretty print to the dumped JSON.
                    json.dump(pokemonData, f, ensure_ascii=False, indent=4)
            else:
                print("File already exists and contains data, moving on...")

            pokemonDf = pd.json_normalize(pokemonData["results"])
            
            # Takes the index # and puts it at 1 instead of 0. This correlates better with the official PokeAPI
            pokemonDf.index = range(1, len(pokemonDf) + 1)

            print(pokemonDf.head())

        except FileNotFoundError as e:
            print("File not found...")

    else:
        # Prints any errors that may occur
        print("Error: " + str(apiData.status_code))
