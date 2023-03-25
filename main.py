import asyncio
from core.crawler import Crawler


async def main() -> None:
    x = Crawler("https://pokeapi.co/api/v2/pokemon")
    await x.start()
    print("DONE")


if __name__ == "__main__":
    asyncio.run(main())
