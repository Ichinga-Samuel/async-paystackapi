# async-paystackapi

Asynchronous Python plugin for [Paystack](https://paystack.com/)
View on [pypi.python.org](https://pypi.python.org/pypi/paystackapi)

## Installation

```shell
pip install asyncpaystackapi
```

## Instantiate Paystack

```python
from paystackapi.paystack import Paystack
paystack_secret_key = "5om3secretK3y"

# All parameters must be passed in as keywords. For both required and optional arguments.
# setting session to true is faster when making multiple requests, this is the default.
# set session to false when you need to make just one request, this is faster for single requests.

paystack = Paystack(secret_key=paystack_secret_key, session=True)

# to use transaction class inside a coroutine
await paystack.transaction.list()

# to use customer class
await paystack.customer.get(customer_id=_id)

# to use plan class
await paystack.plan.get(code=plan_id)

# to use subscription class
await paystack.subscription.list()

# when using session remember to close it.
# await paystack.close()
```

## DOC Reference: <https://developers.paystack.co/v2.0/reference>

### Other methods can be found in the docs folder

#### This library is very similar to [andela-sjames/paystack-python](https://github.com/andela-sjames/paystack-python) for ease of use.
#### apart from the "await" syntax most of the syntax is the same. You can check the documentation in that repo until extensive documentation for this version is made.

### Static Use

To start using the Paystack Python API, you need to start by setting your secret key.

You can set your secret key in your environment by running:

```bash
export PAYSTACK_SECRET_KEY = 'your_secret_key'
```

> Don't forget to get your API key from [Paystack](https://paystack.com/) and assign to the variable `PAYSTACK_SECRET_KEY`

### Available resources

```Python

BulkCharge
Charge
ControlPanel
Customer
DedicatedVirtualAccount
Disputes
Invoice
Misc
Page
Plan
Product
Refund
Settlement
SubAccount
Subscription
Transaction
TransferControl
Transfer
TransferSplit
TransferRecipient
Verification
```

Please reference the **docs** folder for usage,
