import wmi
import time
import platform

import asyncio
import websockets

# Initializing the wmi constructor
f = wmi.WMI()

server_address = "ws://localhost:8800";
current_processes = []


def gather_process_names():

    if platform.system() == "Windows":
        for process in f.Win32_Process():
            # print(process.Name)
            current_processes.append(process.Name + " \n ")


def send_list(out, target):
    async def send():
        async with websockets.connect(target) as websocket:
            await websocket.send(out)

            # ret = await websocket.recv()
            # print(ret)

    asyncio.get_event_loop().run_until_complete(send())


while True:
    gather_process_names()
    send_list(current_processes, server_address)
    print('Information sent')
    del current_processes
    time.sleep(5)

