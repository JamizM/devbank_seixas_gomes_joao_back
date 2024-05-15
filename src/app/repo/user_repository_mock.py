from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.User import User
from .user_repository_interface import UserRepository


class UserRepositoryMock(UserRepository):
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User(name="Vitor Soller", agencia="0000", conta="00000-0", current_balance= 1000.0)
        }

    def get_user(self, name: str) -> Optional[User]:
        return self.users.get(name, None)

    def create_user(self, user: User) -> User:
        self.users[user] = user
        return user

    def delete_item(self, name: str) -> Optional[User]:
        user= self.users.pop(name, None)
        return user

    def update_user(self, name:str=None, agencia:str=None, conta:str=None, current_balance: float=None) -> User:
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