"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from pydockermon.api import API


async def test():
    """Example usage of pydockermon."""
    async with aiohttp.ClientSession() as session:
        host = '192.168.2.11'
        port = '8126'
        data = API(LOOP, session, host, port)
        await data.list_containers()
        print("All containers:", data.all_containers)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test())
