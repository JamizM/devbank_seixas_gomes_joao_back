from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.transaction import Transaction


class ITransactionRepository(ABC):
    @abstractmethod
    def get_all_transactions(self) -> Optional[List[Transaction]]:
        '''
        Returns all the transactions in the database
        '''
        pass
    
    @abstractmethod
    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        '''
        Returns the transaction with the given id.
        If the transaction does not exist, returns None
        '''
        pass

    def get_transaction_id(self, type: TransactionTypeEnum, value: float, timestamp: int) -> Optional[Transaction]:
        '''
        Returns the transaction_id with the given Transaction: type, value and timestamp.
        If the transaction does not exist, returns None
        '''
        pass

    @abstractmethod
    def create_transaction(self, transaction_id: int, transaction: Transaction) -> Optional[Transaction]:
        '''
        Creates a new transaction in the database
        '''
        pass
    
    @abstractmethod
    def delete_transaction(self, transaction_id: int) -> Optional[Transaction]:
        '''
        Deletes the transaction with the given id.
        If the transaction does not exist, returns None
        '''
        pass

    @abstractmethod
    def update_transaction(self, transaction_id: int,
                           transaction_type: TransactionTypeEnum = None,
                           value: float = None,
                           current_balance: float = None,
                           timestamp: float = None) -> Transaction:
        '''
        Updates the transaction with the given id.
        If the transaction does not exist, returns None
        '''
        pass
    
    