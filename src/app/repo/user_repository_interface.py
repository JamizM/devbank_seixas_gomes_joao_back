from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.User import User


class IUserRepository(ABC):

    @abstractmethod
    def get_User(self, name: str) -> Optional[User]:
        '''
        Returns the User with the given name.
        If the User does not exist, returns None
        '''
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        '''
        Creates a new User in the database
        '''
        pass

    @abstractmethod
    def delete_User(self, name: str) -> User:
        '''
        Deletes the User with the given name.
        If the User does not exist, returns None
        '''

    @abstractmethod
    def update_User(self, name:str=None, agencia:int=None, conta:str=None, current_balance:float=None, admin_permission:bool=None) -> User:
        '''
        Updates the User with the given name.
        If the User does not exist, returns None
        '''
        pass