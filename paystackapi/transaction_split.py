
class TransactionSplit:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'split'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "split"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f"split/{code}"
        return await self.req.get(endpoint=endpoint)

    async def update(self, *, code, **kwargs):
        """

        :param code:
        :param kwargs:
        :return:
        """
        endpoint = f"split/{code}"
        return await self.req.put(endpoint=endpoint, json=kwargs)

    async def add(self, *, code, **kwargs):
        """

        :param code:
        :param kwargs:
        :return:
        """
        endpoint = f"split/{code}/subaccount/add"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def remove(self, *, code, **kwargs):
        """

        :param code:
        :param kwargs:
        :return:
        """
        endpoint = f"split/{code}/subaccount/remove"
        return await self.req.post(endpoint=endpoint, json=kwargs)
