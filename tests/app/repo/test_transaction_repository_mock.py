import pytest
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock


class Test_TransactionRepositoryMock:

    def test_get_all_transactions(self):
        repo = TransactionRepositoryMock()
        assert all([expected_transaction == transaction for expected_transaction, transaction in
                    zip(repo.transactions.values(), repo.get_all_transactions())])

    def test_get_transaction(self):
        repo = TransactionRepositoryMock()
        assert repo.get_transaction(transaction_id=1) == repo.transactions.get(1)

    def test_get_transaction_id(self):
        repo = TransactionRepositoryMock()
        transaction = repo.transactions.get(1)
        assert repo.get_transaction_id(transaction.type,
                                       transaction.value,
                                       transaction.timestamp) == 1

    def test_get_transaction_not_found(self):
        repo = TransactionRepositoryMock()
        user = repo.get_transaction(transaction_id=888)
        assert user is None

    def test_create_transaction(self):
        repo = TransactionRepositoryMock()
        len_before = len(repo.transactions)
        transaction = Transaction(type=TransactionTypeEnum.WITHDRAW,
                                  value=12000.99,
                                  current_balance=999.1,
                                  timestamp=12321.2)
        repo.create_transaction(transaction=transaction, transaction_id=1)
        len_after = len(repo.transactions)
        assert len_after == len_before + 1
        assert repo.transactions.get(3) == transaction

    def test_delete_transaction(self):
        repo = TransactionRepositoryMock()
        transaction_expected_to_be_deleted = repo.transactions.get(2)
        len_before = len(repo.transactions)

        transaction = repo.delete_transaction(transaction_id=2)
        len_after = len(repo.transactions)
        assert len_after == len_before - 1
        assert transaction == transaction_expected_to_be_deleted

    def test_delete_transaction_not_found(self):
        repo = TransactionRepositoryMock()
        user = repo.delete_transaction(transaction_id=1000)
        assert user is None

    def test_update_transaction(self):
        repo = TransactionRepositoryMock()
        transaction = Transaction(type=TransactionTypeEnum.WITHDRAW, value=1322.2, current_balance=123.0, timestamp=0.2)
        transaction_updated = repo.update_transaction(transaction_id=1,
                                                      transaction_type=transaction.type,
                                                      value=transaction.value,
                                                      current_balance=transaction.current_balance,
                                                      timestamp=transaction.timestamp)

        assert transaction_updated == transaction
        assert repo.transactions.get(1) == transaction
