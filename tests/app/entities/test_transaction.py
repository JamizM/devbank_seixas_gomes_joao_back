import pytest
from src.app.entities.Transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum


class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100, 100, 1234567.890)
        assert transaction.type == TransactionTypeEnum.DEPOSIT
        assert transaction.value == 100
        assert transaction.current_balance == 100
        assert transaction.timestamp == 1234567.890


        #tatrar os erros esperados