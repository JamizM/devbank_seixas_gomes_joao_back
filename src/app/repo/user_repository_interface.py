from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_all_users(self, user_id: int) -> Optional[dict[int, User]]:
        '''
        Returns the User with the given name.
        If the User does not exist, returns None
        '''
        pass

    @abstractmethod

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        '''
        Returns the User with the given name.
        If the User does not exist, returns None
        '''
        pass

    @abstractmethod
    def create_user(self, user_id: int, user: User) -> Optional[User]:
        '''
        Creates a new User in the database
        '''
        pass

    @abstractmethod
    def delete_user(self, user_id: int, user: User) -> Optional[User]:
        '''
        Deletes the User with the given name.
        If the User does not exist, returns None
        '''

    @abstractmethod
    def update_user(self, user_id: int,
                    name: str = None,
                    agencia: int = None,
                    conta: str = None,
                    current_balance: float = None,
                    admin_permission: bool = None) -> Optional[User]:
        '''
        Updates the User with the given name.
        If the User does not exist, returns None
        '''
        pass