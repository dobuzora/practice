import aiohttp


session = aiohttp.ClientSession()


async def fetch(url):
    async with session.get(url) as resp:
        return resp.status
#         return await resp.status
#     async with session.get(
#         url
#     ) as response:
#         result = await response
#         return result





