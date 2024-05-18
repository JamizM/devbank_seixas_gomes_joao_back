import pytest
from src.app.entities.user import User
from src.app.repo.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:
    def test_get_all_users(self):
        repo = UserRepositoryMock()
        assert all([user_expect == user for user_expect, user in zip(repo.users.values(), repo.get_all_users())])

    def test_get_user(self):
        repo = UserRepositoryMock()
        user = repo.get_user(user_id=1)
        assert user == repo.users.get(1)

    def test_get_user_by_id(self):
        repo = UserRepositoryMock()
        user = repo.get_user(user_id=1)
        user_id = repo.get_user_id(user.name, user.agencia, user.conta)
        assert user == repo.get_user(user_id=user_id)

    def test_get_user_not_found(self):
        repo = UserRepositoryMock()
        user = repo.get_user(user_id=10)
        assert user is None

    def test_create_user(self):
        repo = UserRepositoryMock()
        len_before = len(repo.users)
        user = User(name="Leo", agencia="0200", conta="13227-2", current_balance=0, admin_permission=True)
        repo.create_user(user=user, user_id=777)
        len_after = len(repo.users)
        assert len_after == len_before + 1
        assert repo.users.get(777) == user

    def test_delete_user(self):
        repo = UserRepositoryMock()
        user_expected_to_be_deleted = repo.users.get(321)
        len_before = len(repo.users)

        user = repo.delete_user(user_id=321)
        len_after = len(repo.users)
        assert len_after == len_before - 1
        assert user == user_expected_to_be_deleted

    def test_delete_user_not_found(self):
        repo = UserRepositoryMock()
        user = repo.delete_user(user_id=777)
        assert user is None

    def test_update_user(self):
        repo = UserRepositoryMock()
        user = User(name="Lucao", agencia="0003", conta="07779-5", current_balance=123.0, admin_permission=False)
        user_updated = repo.update_user(user_id=321,
                                        name=user.name,
                                        agencia=user.agencia,
                                        conta=user.conta,
                                        current_balance=user.current_balance,
                                        admin_permission=user.admin_permission)

        assert user_updated == user
        assert repo.users.get(321) == user
