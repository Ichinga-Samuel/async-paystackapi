
class Plan:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """
        name: plan's name.
        description: description of the plan.
        amount: amount for the plan in kobo
        interval: plan's interval
        send_invoices: boolean
        send_sms:
        hosted_page:
        hosted_page_url: url of hosted page
        hosted_page_summary: summary of the hosted page
        currency: plans currency
        :param kwargs: The above arguments as keyword args to form the body of the post request
        :return: Json data from paystack API.
        """
        endpoint = 'plan'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """
        perPage: Specify how many records you want to retrieve per page.
        page: Specify exactly what page you want to retrieve.
        :param kwargs: Keyword args to form the query params
        :return:
        """
        endpoint = 'plan'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def get(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f'plan/{code}'
        return await self.req.get(endpoint=endpoint)

    async def update(self, *, code, **kwargs):
        """

        :param code:
        :param kwargs:
        :return:
        """
        endpoint = f'plan/{code}'
        return await self.req.put(endpoint=endpoint, json=kwargs)
