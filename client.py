import aiohttp
import asyncio
import ssl


async def main():
    sslcontext = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile='example.crt')
    async with aiohttp.ClientSession() as session:
        async with session.get("https://127.0.0.1:8443/JOHNYY", ssl=sslcontext) as response:
            html = await response.read()
            print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())