
class Transaction:

    def __init__(self, req):
        self.req = req

    async def initialize(self, **kwargs):
        """
        Initialize transaction. Email and amount are required fields
        :param kwargs: body of request as keyword arguments
        :return: json data from paystack API
        """
        endpoint = 'transaction/initialize'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def verify(self, *, reference):
        """

        :param reference:
        :return: json data from paystack API
        """
        endpoint = f'transaction/verify/{reference}'
        return await self.req.get(endpoint=endpoint)

    async def list(self, **kwargs):
        """
        if you specify a page number also specify a results per page. eg page=1, perPage=10
        :param kwargs: query parameters as keyword arguments
        :return: List of transactions as json data from paystack API
        """
        endpoint = 'transaction'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def get(self, *, id):
        """
        :param id: id of a single transaction
        :return: json data from paystack API
        """
        endpoint = f'transaction/{id}'
        return await self.req.get(endpoint=endpoint)

    async def charge(self, **kwargs):
        """
        :param kwargs: body of request as keyword arguments
        :return: json data from paystack API
        """
        endpoint = "transaction/charge_authorization"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def check(self, **kwargs):
        """
        All mastercard and visa authorizations can be checked with this endpoint to know if they have funds for the payment you seek.
        :param kwargs: body of request as keyword arguments
        :return: json data from paystack API
        """
        endpoint = "transaction/check_authorization"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def timeline(self, *, ref):
        """
        :param ref: id or reference of transaction
        :return: json data from paystack API
        """
        endpoint = f"transaction/timeline/{ref}"
        return await self.req.get(endpoint=endpoint)

    async def totals(self, **kwargs):
        """
        If you specify a page number also specify a results per page. eg page=1, perPage=10
        You can specify from and to as query parameters
        :param kwargs:
        :return: json data from paystack API
        """
        endpoint = "transaction/totals"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def export(self, **kwargs):
        """
        If you specify a page number also specify a results per page. eg page=1, perPage=10
        :param kwargs:
        :return:
        """
        endpoint = "transaction/export"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def partial_debit(self, **kwargs):
        """
        Retrieve part of a payment from a customer
        authorization_code, currency, amount, email are required fields
        :param kwargs: keyword arguments form body of requests
        :return:
        """
        endpoint = "transaction/partial_debit"
        return await self.req.post(endpoint=endpoint, json=kwargs)