from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum

class Transaction:
    type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type: TransactionTypeEnum=None, value: float=None, current_balance: float=None, timestamp: float=None):

        validation_type = self.validate_type(type)
        if validation_type[0] is False:
            raise ParamNotValidated("tipo", validation_type[1])
        self.type = type

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("valor", validation_value[1])
        self.value = value

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("saldo", validation_current_balance[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("tempo", validation_timestamp[1])
        self.timestamp = timestamp

    #validações de campos 
    @staticmethod
    def validate_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
        if type is None:
            return (False, "Tipo é obrigatório")
        if type(transaction_type) != TransactionTypeEnum:
            return (False, "Tipo inválido")
        return (True, "")
    
    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return (False, "Valor é obrigatório")
        if type(value) != float:
            return (False, "Valor deve ser um float")
        if value < 0:
            return (False, "Uma transação deve conter um valor positivo")
        return (True, "") 
    

    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Saldo é obrigatório")
        if type(current_balance) != float:
            return (False, "Saldo deve ser um float, Ex: 1000.0")
        if current_balance < 0:
            return (False, "Saldo deve ser um número positivo")
        return (True, "")
    
    @staticmethod 
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "Tempo é obrigatório")
        if type(timestamp) != float:
            return (False, "Tempo deve ser um float")
        if timestamp < 0:
            return (False, "Tempo deve ser um número positivo")
        return (True, "")

    def to_dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp,
        }
    
    def __eq__(self,other):
        return self.type == other.type and self.value == other.value and self.current_balance == other.current_balance and self.timestamp == other.timestamp

    def __repr__(self):
        return f"Transaction(type={self.type}, value={self.value}, current_balance={self.current_balance}, timestamp={self.timestamp})"