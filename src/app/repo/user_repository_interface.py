from abc import ABC, abstractmethod
from typing import Optional

from ..entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> Optional[list[tuple[int, User]]]:
        '''
        Returns the User with the given user_id.
        If the User does not exist, returns None
        '''
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        '''
        Returns the User with the given user_id.
        If the User does not exist, returns None
        '''
        pass

    @abstractmethod
    def get_user_id(self, nome: str, agencia: str, conta: str) -> Optional[int]:
        '''
        Returns the user_id with the given User: name, agencia, conta.
        If the User does not exist, returns None
        '''

    @abstractmethod
    def create_user(self, user_id: int, user: User) -> Optional[User]:
        '''
        Creates a new User in the database
        '''
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> Optional[User]:
        '''
        Deletes the User with the given user_id.
        If the User does not exist, returns None
        '''
        pass

    @abstractmethod
    def update_user(self, user_id: int,
                    name: str = None,
                    agencia: int = None,
                    conta: str = None,
                    current_balance: float = None,
                    admin_permission: bool = None) -> Optional[User]:
        '''
        Updates the User with the given user_id.
        If the User does not exist, returns None
        '''
        pass
