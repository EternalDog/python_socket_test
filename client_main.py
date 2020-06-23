import time
import asyncio
import websockets
import psutil


server_address = "ws://192.168.1.159:8800";
current_processes = []


def gather_process_names():
    current_processes.clear()
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            current_processes.append(proc.name() + " \n ")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


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
    print('Information sent, waiting 5s')
    time.sleep(5)
