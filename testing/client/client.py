import asyncio
import websockets

async def listen():
    uri = "ws://localhost:56277/ws"
    async with websockets.connect(uri) as websocket:
        # Stuur 1 keer bericht
        await websocket.send("Hallo FastAPI websocket!")

        print("Bericht verzonden, wacht op reactie...")

        while True:
            try:
                letter = await asyncio.wait_for(websocket.recv(), timeout=2)
                print(f"Ontvangen letter: {letter}")
            except asyncio.TimeoutError:
                print("Geen data meer ontvangen, connection close assumed.")
                break

asyncio.run(listen())
