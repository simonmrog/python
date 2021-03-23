import aiohttp
import asyncio


class HTTPClient:
    session = None

    def __init__(self):
        pass

    def start(self):
        self.session = aiohttp.ClientSession()

    def stop(self):
        self.session.close()

    async def get(self, *, url):
        try:
            async with self.session.get(url) as response:
                result = await response.json()
                return result
        except Exception as e:
            print(f"[ERROR]{e}")
            return None


http_client = HTTPClient()
