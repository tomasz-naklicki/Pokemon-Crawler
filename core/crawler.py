import requests
import asyncio
import httpx
from typing import TypedDict, Literal


# PokemonFields = Literal["name", "url"]
# Pokemon = TypedDict[str, str]


class Crawler:
    def __init__(self, url: str):
        self.url = url
        self.pokemon_data = {}
        self.queue = asyncio.Queue()
        self.client = httpx.AsyncClient()
        self.worker_limit = 2

    async def start(self):
        data = requests.get(self.url).json()
        self.populate_queue(int(data["count"]))
        workers = [asyncio.create_task(self.worker()) for _ in range(self.worker_limit)]
        await self.queue.join()

        for worker in workers:
            worker.cancel()

    def populate_queue(self, count: int) -> None:
        for i in range(1, count + 1):
            self.queue.put_nowait(f"{self.url}/{i}")

    async def worker(self):
        while True:
            try:
                await self.extract()
            except asyncio.CancelledError:
                return           
                
    async def extract(self):
        """
        TO DO: 
        - convert payload to json
        - extract data 
        - save data
        
        """
        url = await self.queue.get()
        payload = await self.client.get(url)
        async for x in payload.aiter_text():
            print(x)