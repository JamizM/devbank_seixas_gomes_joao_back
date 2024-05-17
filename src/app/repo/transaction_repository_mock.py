from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.Transaction import Transaction
from .transaction_repository_interface import ITransactionRepository


class TransactionRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {
            1: Transaction(type=TransactionTypeEnum.DEPOSIT, value=1000.0, current_balance=1000.0, timestamp=1234567890),
            2: Transaction(type=TransactionTypeEnum.WITHDRAW, value=500.0, current_balance=500.0, timestamp=987654321),
        }

    def get_all_transactions(self, transaction_id: int) -> Optional[Transaction]:
        return self.transactions.get(transaction_id, None)

    def create_transaction(self, transaction_id: int, transaction: Transaction) -> Optional[Transaction]:
        if not self.transactions.get(transaction_id, None):
            return transaction
        return

    def update_transaction(self, transaction_id: int,
                           transaction_type: TransactionTypeEnum = None,
                           value: float = None,
                           current_balance: float = None,
                           timestamp: float = None) -> Optional[Transaction]:

        transaction = self.transactions.get(transaction_id, None)

        if transaction:

            if transaction_type:
                transaction.type = transaction_type
            if value:
                transaction.value = value
            if current_balance:
                transaction.current_balance = current_balance
            if timestamp:
                transaction.timestamp = timestamp

            self.transactions[transaction_id] = transaction

        return transaction






