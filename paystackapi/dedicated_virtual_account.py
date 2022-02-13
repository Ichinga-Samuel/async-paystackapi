
class DedicatedVirtualAccount:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'dedicated_account'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'dedicated_account'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, _id):
        """

        :param _id:
        :return:
        """
        endpoint = f"dedicated_account/{_id}"
        return await self.req.get(endpoint=endpoint)

    async def deactivate(self, *, _id):
        """

        :param _id:
        :return:
        """
        endpoint = f"dedicated_account/{_id}"
        return await self.req.delete(endpoint=endpoint)

    async def split(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'dedicated_account/split'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def remove_split(self, *, account_number):
        """

        :param account_number:
        :return:
        """
        endpoint = 'dedicated_account/split'
        return await self.req.delete(endpoint=endpoint, json={"account_number": account_number})

    async def providers(self):
        """

        :return:
        """
        endpoint = "dedicated_account/available_providers"
        return await self.req.get(endpoint=endpoint)
