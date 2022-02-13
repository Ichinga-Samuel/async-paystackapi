
class Customer:
    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """
        email is required
        :param kwargs:
        :return:
        """
        endpoint = 'customer'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """
        List customers available on your integration
        if you specify a page number also specify a results per page. eg page=1, perPage=10
        :param kwargs: query parameters as keyword arguments
        :return: List of customers as json data from paystack API
        """
        endpoint = 'customer'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def get(self, *, customer_id):
        """
        :param customer_id: email or code of customer
        :return:
        """
        endpoint = f"customer/{customer_id}"
        return await self.req.get(endpoint=endpoint)

    async def update(self, *, customer_id, **kwargs):
        """

        :param customer_id:
        :param kwargs:
        :return:
        """
        endpoint = f'customer/{customer_id}'
        return await self.req.put(endpoint, json=kwargs)

    async def validate(self, *, customer_id, **kwargs):
        """
        validate customer
        :param customer_id:
        :param kwargs:
        :return:
        """
        endpoint = f"customer/{customer_id}/identification"
        return await self.req.post(endpoint, json=kwargs)

    async def risk_action(self, **kwargs):
        """
        blacklist or white list customer
        :param kwargs:
        :return:
        """
        endpoint = "customer/set_risk_action"
        return await self.req.post(endpoint, json=kwargs)

    async def deactivate_authorization(self, **kwargs):
        """
        deactivate authorization of card
        :param kwargs:
        :return:
        """
        endpoint = "customer/deactivate_authorization"
        return await self.req.post(endpoint, json=kwargs)

