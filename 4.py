"""
ассинхронная функция грузит инфу со 100-а ссылок  (github) и засекает время 
"""
import asyncio
import aiohttp
import time

async def download_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status == 200:
                data = await response.read()
            else:
                  print("Ошибка")

async def main():

    start = time.time()

    tasks = []
    for url in urls: 

        task = asyncio.create_task(download_data(url))
        tasks.append(task)

    await asyncio.gather(*tasks)

    end = time.time()
    itog_time =  end - start 
    print(f"процесс занял {itog_time} секунд.")

if __name__ == "__main__":
    urls = [  
        "https://github.com/Don-Rumata-Estorsky/25.3.python",
        "https://github.com/Don-Rumata-Estorsky/25.3.python",
        "https://github.com/Don-Rumata-Estorsky/25.3.python"
    ]  # грузил 100, комп завис, вот вам 3

    asyncio.run(main())
