import pytest
from src.app.entities.Transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, 100.0, 1234567.890)
        assert transaction.type == TransactionTypeEnum.DEPOSIT
        assert transaction.value == 100.0
        assert transaction.current_balance == 100.0
        assert transaction.timestamp == 1234567.890

###TYPE_TESTS###
    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=None, value=100.0, current_balance=100.0, timestamp=1234567.890)

    def test_transaction_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type="notinenum", value=100.0, current_balance=100.0, timestamp=1234567.890)
###TYPE_TESTS###

###VALUE_TESTS###
    def test_transaction_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=None, current_balance=100.0, timestamp=1234567.890)

    def test_transaction_value_is_not_float1(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=1, current_balance=100.0, timestamp=1234567.890)
    def test_transaction_value_is_not_float2(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value='1.0', current_balance=100.0, timestamp=1234567.890)

    def test_transaction_value_is_not_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=-1.0, current_balance=100.0, timestamp=1234567.890)
###VALUE_TESTS###

###CURRENT_BALANCE_TESTS###
    def test_transaction_cbalance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=None, timestamp=1234567.890)

    def test_transaction_cbalance_is_not_float1(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=1, timestamp=1234567.890)
    def test_transaction_cbalance_is_not_float2(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance='1.0', timestamp=1234567.890)

    def test_transaction_cbalance_is_not_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=-1, timestamp=1234567.890)
###CURRENT_BALANCE_TESTS###

###TIMESTAMP_TESTS###
    def test_transaction_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=100.0, timestamp=None)

    def test_transaction_timestamp_is_not_float1(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=100.0, timestamp=1)
    def test_transaction_timestamp_is_not_float2(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=100.0, timestamp='1')

    def test_transaction_timestamp_is_not_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=100.0, timestamp=-1)
###TIMESTAMP_TESTS###

###TODICT_TESTS###

    def test_transaction_to_dict(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, 100.0, 1234567.890)
        assert transaction.to_dict() == {"type": transaction.type,
                                         "value": transaction.value,
                                         "current_balance": transaction.current_balance,
                                         "timestamp": transaction.timestamp}