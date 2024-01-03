import asyncio

import socketio
from aioconsole import ainput

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print("Connected to server")
    asyncio.create_task(send_messages())


@sio.event
async def message(self, data):
    print(data)


@sio.event
async def disconnect():
    print("Disconnected from server")


async def send_messages():
    while True:
        message = await ainput("Your message: ")
        await sio.send(message)


async def start(host, port):
    await sio.connect(f"http://{host}:{port}")
    await sio.wait()


def run_client(host, port):
    asyncio.run(start(host, port))


# import asyncio

# import socketio
# from aioconsole import ainput

# sio = socketio.AsyncClient()

# @sio.event
# async def connect():
#     print("Connected to server")
#     asyncio.create_task(send_messages())

# @sio.event
# async def message(data):
#     print(data)

# @sio.event
# async def disconnect():
#     print("Disconnected from server")

# async def send_messages():
#     while True:
#         message = await ainput("Your message: ")
#         await sio.send(message)

# async def main():
#     await sio.connect('http://127.0.0.1:6969')
#     await sio.wait()

# if __name__ == '__main__':
#     asyncio.run(main())
