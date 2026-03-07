from extract.ExtractData import *
from utils import * 
import json

async def main():
    
    # Raw JSON data directory
    rawJSONDirPath = "src\\data\\raw\\json\\"
    
    # Creates JSON into Dataframe. 
    dataframe = await createJsonDf()

    if utils.has_Files(rawJSONDirPath):
        print("Directory has Data, moving on...")
    else:
        # Starts parsing the dataframe for all URLs
        urls = await parseJson(dataframe)
        
        # Then, traverses API 10 requests (to reduce traffic) at a time, creating a new file for each containing the data for that specific pokemon.
        await startAPITraverse(urls)
    
    print(rawJSONDirPath)
    
    # Read JSON files here.
    for file in os.listdir(rawJSONDirPath):
        
        fullFilePath = os.path.join(rawJSONDirPath, file)
        
        pokemonJSONData = open(fullFilePath)
        data = json.load(pokemonJSONData)
        
        id = data['id']
        name = data['name']
        height = data['height']
        weight = data['weight']
        #hpBase = data["stats"]["stat"]["hp"]
        
        print(id, name, height, weight)
        

if __name__ == "__main__":
    asyncio.run(main())    
