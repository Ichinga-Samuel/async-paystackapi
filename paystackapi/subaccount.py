
class SubAccount:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'subaccount'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "subaccount"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f"subaccount/{code}"
        return await self.req.get(endpoint=endpoint)

    async def update(self, *, code, **kwargs):
        """

        :param code: 
        :param kwargs:
        :return:
        """
        endpoint = f"subaccount/{code}"
        return await self.req.post(endpoint=endpoint, json=kwargs)
