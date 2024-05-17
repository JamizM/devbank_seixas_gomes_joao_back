from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.user import User
from .user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User(name="Vitor Soller", agencia="0000", conta="00000-0", current_balance=1000.0)
        }

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id, None)

    def create_user(self, user_id: int, user: User) -> Optional[User]:
        if self.users.get(user_id, None):
            raise ValueError(f"User {user_id} has already been created")
        self.users[user_id] = user
        return user

    def delete_item(self, user_id: int, user: User) -> Optional[User]:
        return self.users.pop(user_id, None)

    def update_user(self, user_id: int,
                    name: str = None,
                    agencia: int = None,
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
