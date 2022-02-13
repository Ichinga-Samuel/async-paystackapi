import asyncio
import platform

from aiohttp import request, ClientSession

from paystackapi import API_BASE_URL


class BasicAPIPayment:

    def __init__(self, *, secret_key):
        auth = f"Bearer {secret_key}"
        self.headers = {"Content-type": "application/json"}
        self.headers = {"Authorization": auth, "Content-type": "application/json"}

    def update_header(self, header):
        self.headers.update(header)

    async def _request(self, method, url, **kwargs):
        headers = kwargs.get('headers', {})
        kwargs['headers'] = {**self.headers, **headers}
        url = f"{API_BASE_URL}{url}"
        async with request(method, url, **kwargs) as resp:
            res = await resp.json()
        return res

    async def post(self, *, endpoint, **kwargs):
        return await self._request("POST", endpoint, **kwargs)

    async def get(self, *, endpoint, **kwargs):
        return await self._request("GET", endpoint, **kwargs)

    async def delete(self, *, endpoint, **kwargs):
        return await self._request("DELETE", endpoint, **kwargs)

    async def put(self, *, endpoint, **kwargs):
        return await self._request("PUT", endpoint, **kwargs)


class SessionPayment:

    def __init__(self, *, secret_key):
        auth = f"Bearer {secret_key}"
        self.headers = {"Authorization": auth, "Content-type": "application/json"}
        self.session = ClientSession(headers={**self.headers})

    async def _request(self, method, url, **kwargs):
        url = f"{API_BASE_URL}{url}"
        if headers := kwargs.get('headers', None):
            kwargs['headers'] = {**self.headers, **headers}
        resp = await method(url, **kwargs)
        return await resp.json()

    async def post(self, *, endpoint, **kwargs):
        return await self._request(self.session.post, endpoint, **kwargs)

    async def get(self, *, endpoint, **kwargs):
        return await self._request(self.session.get, endpoint, **kwargs)

    async def delete(self, *, endpoint, **kwargs):
        return await self._request(self.session.delete, endpoint, **kwargs)

    async def put(self, *, endpoint, **kwargs):
        return await self._request(self.session.put, endpoint, **kwargs)


if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
