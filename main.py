from core.crawler import Crawler


def main() -> None:
    x = Crawler("https://pokeapi.co/api/v2/pokemon")
    x.start()
    print("DONE")


if __name__ == "__main__":
    main()