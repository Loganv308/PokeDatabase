from extract.ExtractData import *

async def run():
    
    dataframe = await createJsonDf()

    urls = await parseJson(dataframe)
    
    await startAPITraverse(urls)

# For each URL it finds within the "pokemon_data.json", it will iterate and request 10 at a time, then put the pertaining data into the "/raw/json" folder
if __name__ == "__main__":
    asyncio.run(run())    
