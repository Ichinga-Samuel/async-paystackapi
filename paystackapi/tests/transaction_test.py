import pytest


@pytest.mark.usefixtures('setup')
class TestTransaction:

    async def test_initialize(self, mock):
        transaction = self.pay.transaction
        mock.post(f"{self.API}transaction/initialize", body='{"status": true, "contributors": true}', status=201, )
        resp = await transaction.initialize(amount=12000, email='akaichinga@gmail.com')
        assert resp['status'] == True

    async def test_get(self, mock):
        mock.get(f"{self.API}transaction/4013", body='{"status": true, "contributors": true}', status=201,)
        transaction = self.pay.transaction
        resp = await transaction.get(id=4013)
        assert resp['status'] == True
