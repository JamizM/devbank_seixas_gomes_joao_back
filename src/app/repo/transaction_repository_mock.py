from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.Transaction import Transaction
from .transaction_repository_interface import TransactionRepository


class TransactionRepositoryMock(TransactionRepository):
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {
            1: Transaction(type=TransactionTypeEnum.DEPOSIT, value=1000, current_balance=1000, timestamp=1234567890), 
            2: Transaction(type=TransactionTypeEnum.WITHDRAW, value=500, current_balance=500, timestamp=0987654321),
        }

    def get_all_transactions(self, type: TransactionTypeEnum) -> Optional[Transaction]:
        return self.transactions.get(type, None)

    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions[transaction] = transaction
        return transaction

    def update_user(self, name:str=None, agencia:int=None, conta:str=None, current_balance: float=None) -> Transaction:
        user = self.users.get(name, None)
        if user is None:
            return None

        if name is not None:
            user.name = name
        if agencia is not None:
            user.agencia = agencia
        if conta is not None:
            user.conta = conta
        if current_balance is not None:
            user.current_balance = current_balance
        self.users[name] = user

        return user