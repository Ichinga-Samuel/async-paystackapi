import pytest
from aioresponses import aioresponses

from paystackapi.paystack import Paystack
from paystackapi import API_BASE_URL


@pytest.fixture
async def setup(request):
    pay = Paystack(session=True)
    request.cls.pay = pay
    request.cls.API = API_BASE_URL
    yield
    await pay.close()


@pytest.fixture
def mock():
    with aioresponses() as mock:
        yield mock
