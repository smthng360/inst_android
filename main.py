import asyncio
from src.flow.main import Flow


async def main():
    fl = Flow("_.ringoo._", "your_password")

    await fl.process_and_redirect()

    print(fl._aacjid)


if __name__ == "__main__":
    asyncio.run(main())
