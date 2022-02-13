
class Settlement:

    def __init__(self, req):
        self.req = req

    async def fetch(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        endpoint = 'settlement'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch_transactions(self, *, _id, **kwargs):
        """
        :param _id:
        :param kwargs:
        :return:
        """
        endpoint = f'settlement/{_id}/transactions'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)
