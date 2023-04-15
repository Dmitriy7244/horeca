import asyncio


async def main():
    print('Пересылаю')

    try:
        await asyncio.sleep(10)
    finally:
        print('Удаляю')


loop = asyncio.get_event_loop()

if __name__ == '__main__':
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.close()
