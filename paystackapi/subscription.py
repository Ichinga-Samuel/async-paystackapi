
class Subscription:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'subscription'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'subscription'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f'subscription/{code}'
        return await self.req.get(endpoint=endpoint)

    async def enable(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'subscription/enable'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def disable(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'subscription/disable'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def generate_link(self, *, code):
        """
        Generate a link for updating the card on a subscription
        :param code:
        :return:
        """
        endpoint = f'subscription/{code}/manage/link'
        return await self.req.get(endpoint=endpoint)

    async def send_link(self, *, code):
        """
        Email a customer a link for updating the card on their subscription
        :param code:
        :return:
        """
        endpoint = f'subscription/{code}/manage/email'
        return await self.req.get(endpoint=endpoint)
