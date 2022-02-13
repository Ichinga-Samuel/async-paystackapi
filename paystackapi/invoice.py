
class Invoice:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'paymentrequest'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "paymentrequest"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def view(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f"paymentrequest/{code}"
        return await self.req.get(endpoint=endpoint)

    async def verify(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f"paymentrequest/verify/{code}"
        return await self.req.get(endpoint=endpoint)

    async def send_notification(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f"paymentrequest/notify/{code}"
        return await self.req.post(endpoint=endpoint)

    async def dashboard_metrics(self):
        """
        Get invoice metrics for dashboard
        :return:
        """
        endpoint = 'paymentrequest/totals'
        return await self.req.get(endpoint=endpoint)

    async def finalize_draft(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f"paymentrequest/finalize/{code}"
        return await self.req.post(endpoint=endpoint)

    async def update(self, *, code, **kwargs):
        """

        :param code:
        :param kwargs:
        :return:
        """
        endpoint = f"paymentrequest/{code}"
        return await self.req.put(endpoint=endpoint, json=kwargs)

    async def archive(self, *, code):
        """

        :param code:
        :param kwargs:
        :return:
        """
        endpoint = f"paymentrequest/archive/{code}"
        return await self.req.post(endpoint=endpoint)
