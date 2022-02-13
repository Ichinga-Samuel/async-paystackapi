from .base import SessionPayment, BasicAPIPayment
from .transaction import Transaction
from .misc import Misc
from .page import Page
from .controlpanel import CPanel
from .charge import Charge
from .bulkcharge import BulkCharge
from .customer import Customer
from .dedicated_virtual_account import DedicatedVirtualAccount
from .disputes import Dispute
from .subaccount import SubAccount
from .plan import Plan
from .settlement import Settlement
from .transfer import Transfer
from .refund import Refund
from .transaction_split import TransactionSplit
from .invoice import Invoice
from .verification import Verification
from .transfer_control import TransferControl
from .products import Product
from .transfer_recipient import TransferRecipient
from .subscription import Subscription
from paystackapi import SECRET_KEY


class Paystack:

    def __init__(self, secret_key=None, session=True):
        secret_key = secret_key or SECRET_KEY
        self.req = SessionPayment(secret_key=secret_key) if session else BasicAPIPayment(secret_key=secret_key)
        self.plan = Plan(self.req)
        self.bulkcharge = BulkCharge(self.req)
        self.charge = Charge(self.req)
        self.cpanel = CPanel(self.req)
        self.customer = Customer(self.req)
        self.disputes = Dispute(self.req)
        self.dva = DedicatedVirtualAccount(self.req)
        self.invoice = Invoice(self.req)
        self.misc = Misc(self.req)
        self.page = Page(self.req)
        self.plan = Plan(self.req)
        self.product = Product(self.req)
        self.refund = Refund(self.req)
        self.settlement = Settlement(self.req)
        self.subaccount = SubAccount(self.req)
        self.subscription = Subscription(self.req)
        self.transaction = Transaction(self.req)
        self.transactionSplit = TransactionSplit(self.req)
        self.transferControl = TransferControl(self.req)
        self.transfer = Transfer(self.req)
        self.transferRecipient = TransferRecipient(self.req)
        self.verification = Verification(self.req)
        self.session = session

    async def close(self):
        if self.session:
            await self.req.session.close()
        else:
            pass
