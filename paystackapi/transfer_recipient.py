
class TransferRecipient:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "transferrecipient"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def bulk_create(self, *, batch):
        """

        :param batch:
        :return:
        """
        endpoint = 'transferrecipient/bulk'
        return await self.req.post(endpoint=endpoint, json=dict(batch=batch))

    async def list(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'transferrecipient'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f'transferrecipient/{code}'
        return await self.req.get(endpoint=endpoint)

    async def update(self, *, code, **kwargs):
        """

        :param code:
        :return:
        """
        endpoint = f'transferrecipient/{code}'
        return await self.req.put(endpoint=endpoint, json=kwargs)

    async def delete(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f'transferrecipient/{code}'
        return await self.req.delete(endpoint=endpoint)
