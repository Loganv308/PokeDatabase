from extract.ExtractData import *
from utils import * 
import json
from load.Pokemon import *

async def main():
    # Raw JSON data directory
    rawJSONDirPath = "src\\data\\raw\\json\\"
    textFilePath = "src\\data\\docs\\"

    # Creates JSON into Dataframe. 
    dataframe = await createJsonDf()

    if utils.has_Files(rawJSONDirPath):
        print("Directory has Data, moving on...")
    else:
        # Starts parsing the dataframe for all URLs
        urls = await parseJson(dataframe)
        
        # Then, traverses API 10 requests (to reduce traffic) at a time, creating a new file for each containing the data for that specific pokemon.
        await startAPITraverse(urls)
    
    # Read JSON files here.
    for file in os.listdir(rawJSONDirPath):
        
        fullFilePath = os.path.join(rawJSONDirPath, file)
        
        pokemonJSONData = open(fullFilePath)
        
        data = json.load(pokemonJSONData)
        
        id = data['id']
        name = data['name']
        height = data['height']
        weight = data['weight']
        hpBase = data['stats'][0]['base_stat']
        attackBase = data['stats'][1]['base_stat']
        defenseBase = data['stats'][2]['base_stat']
        specAttackBase = data['stats'][3]['base_stat']
        specDefenseBase = data['stats'][4]['base_stat']
        speedBase = data['stats'][5]['base_stat']
        pokeType = data['types'][0]["type"]["name"]

        pokemon = Pokemon(id, name, height, weight, hpBase, attackBase, defenseBase, specAttackBase, specDefenseBase, speedBase, pokeType)
        
        print(pokemon)
        
        # print(id, name, height, weight, hpBase, attackBase, defenseBase, specAttackBase, specDefenseBase, speedBase, pokeType)
        
        # statText = pokemon.to_document()
        
        # statTextPath = textFilePath + f"{pokemon.name}.txt"
        
        # # TODO: Add in Move data to each of the files as well. Utilize the Move.py class.

        # # TODO: Put into a Chroma DB and Vectorize. Analyze using ChatGPT or another AI API

        # with open(statTextPath, "w") as w:
        #     w.write(statText)
        #     print(statTextPath + " created!")


if __name__ == "__main__":
    asyncio.run(main())    
