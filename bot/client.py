import asyncio


async def run_client(msg: bytes) -> None:
    print("Client also has been run")
    reader, writer = await asyncio.open_connection("127.0.0.1", 9999)
    writer.write(msg)
    await writer.drain()

    while True:
        data = await reader.read(128)
        print(data)
        if not data:
            print("no data")

            writer.close()
            await writer.wait_closed()
