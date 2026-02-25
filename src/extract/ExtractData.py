import pandas as pd
import requests
import asyncio
import aiohttp
import json
import os

API_URL = "https://pokeapi.co/api/v2/pokemon?limit=10000&offset=0"
FILEPATH = "src\\data\\pokemon_data.json"
RAWDIRPATH = "src\\data\\raw\\json\\"

def getAPIData():
    response = requests.get(API_URL)

    return response

def getFileSize(filePath: str) -> int:

    fileSize = os.path.getsize(filePath)

    return fileSize

async def fetchAndSave(session, semaphore, name, url):
    async with semaphore:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()

            file_path = os.path.join("src/data/raw/json", f"{name}.json")
            if(os.path.isfile(file_path)):
                print(f"{name}.json is already created...")
            else:
                with open(file_path, "w") as f:
                    json.dump(data, f, indent=4)
                
                print(f"Saved: {name}")

async def main(url_list):
    semaphore = asyncio.Semaphore(10)

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetchAndSave(session, semaphore, name, url)
            for name, url in url_list
        ]

        await asyncio.gather(*tasks)

def createJsonDf() -> pd.DataFrame:
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

        except FileNotFoundError as e:
            print("File not found..." + str(e))

        return pokemonDf
    else:
        # Prints any errors that may occur
        print("Error: " + str(apiData.status_code))

def parseJson(dataFrame: pd.DataFrame) -> list:
    urls = []

    for _, row in dataFrame.iterrows():
        name = row["name"]
        url = row["url"]

        urls.append((name, url))

    return urls

if __name__ == "__main__":
    dataframe = createJsonDf()

    urls = parseJson(dataframe)

    results = asyncio.run(main(urls))