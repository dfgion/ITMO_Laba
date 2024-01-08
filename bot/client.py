import asyncio


async def run_client(msg: bytes) -> None:
    print("Client also has been run")
    try:
        reader, writer = await asyncio.open_connection("127.0.0.1", 9999)
    except:
        # Данное исключение никогда не будет вызвано. Оно сделана для понимания того, что подключение идёт к существующей сессии запроса кода и если хост  закрыт для подключения, значит запроса кода не было. В данной реализации хост всегда открыт, так как клиент и сервер это один компьютер и взаимодействие происходит в локальной сети, а так же оно 100% открывается, так как хэндлер кода активируется после написания сообщения в бота, а не при запросе кода в приложении
        raise Exception('the server is closed')
    writer.write(msg)
    await writer.drain()

    while True:
        data = await reader.read(128)
        print(data)
        if not data:
            print("no data")
            writer.close()
            await writer.wait_closed()
