
class Transfer:

    def __init__(self, req):
        self.req = req

    async def initiate(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'transfer'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def finalize(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'transfer/finalize_transfer'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def initiate_bulk_transfer(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'transfer/bulk'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        endpoint = 'transfer'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f"transfer/{code}"
        return await self.req.get(endpoint=endpoint)

    async def verify(self, *, ref):
        """

        :param ref:
        :return:
        """
        endpoint = f"transfer/verify/{ref}"
        return await self.req.get(endpoint=endpoint)
