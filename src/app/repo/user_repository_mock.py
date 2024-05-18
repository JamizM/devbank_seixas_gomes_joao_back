from abc import ABC
from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.user import User
from .user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository, ABC):
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User(name="Vitor Soller", agencia="0000", conta="00000-0", current_balance=1000.0, admin_permission=False),
            321: User(name="Jao do Bao", agencia="0001", conta="10000-0", current_balance=1001.1, admin_permission=True),
        }

    def get_all_users(self) -> Optional[List[User]]:
        return [user for user in self.users.values()]

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id, None)

    def get_user_id(self, name: str, agencia: str, conta: str) -> Optional[int]:

        for id in self.users.keys():

            if [self.users[id].name, self.users[id].agencia, self.users[id].conta] == [name, agencia, conta]:

                return id

        return None

    def create_user(self, user_id: int, user: User) -> Optional[User]:
        if self.users.get(user_id, None):
            raise ValueError(f"User {user_id} has already been created")
        self.users[user_id] = user
        return user

    def delete_user(self, user_id: int) -> Optional[User]:
        return self.users.pop(user_id, None)

    def update_user(self, user_id: int,
                    name: str = None,
                    agencia: str = None,
                    conta: str = None,
                    current_balance: float = None,
                    admin_permission: bool = None) -> Optional[User]:

        user = self.users.get(user_id, None)

        if user:

            if name:
                user.name = name
            if agencia:
                user.agencia = agencia
            if conta:
                user.conta = conta
            if current_balance:
                user.current_balance = current_balance
            self.users[user_id] = user

        return user
