import asyncio

from app.controls.registration import Code


async def run_server():
    print("In connection")
    server = await asyncio.start_server(Code.connection, "127.0.0.1", 9999)
    await server.start_serving()
    await asyncio.sleep(10)
    server.close()
    await server.wait_closed()
    print("Сессия в 10 секунд была завершена")
