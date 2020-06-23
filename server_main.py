import asyncio
import websockets
import time
import sys


def append_to_file(arr):
    file = open("log.txt", "a")
    file.write(time.strftime("%H:%M:%S", time.localtime()) + "\n")
    for i in arr:
        file.write(i)
    file.close()
    print("Successfully saved to file")


async def websocket_handler(websocket, path):
    processes = await websocket.recv()
    append_to_file(processes)

    # await websocket.send("Success")
    # print("Success")

ipv4 = sys.argv[1]
port = 8800
start_server = websockets.serve(websocket_handler, ipv4, port)
print("Socket open on port: " + str(port))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
