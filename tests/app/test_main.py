import time

import fastapi.exceptions
import pytest

from src.app.main import get_user, deposit, withdraw
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.entities.transaction import Transaction

in_use_id = 1


class Test_Main:

    def test_get(self):
        repo = UserRepositoryMock()
        response = get_user()
        assert response == repo.get_user(in_use_id).to_dict()

    def test_post_deposit(self):

        user_repo = UserRepositoryMock()

        response = deposit(request={"2": 1,
                                    "5": 2,
                                    "10": 0,
                                    "20": 0,
                                    "50": 5,
                                    "100": 0,
                                    "200": 0})

        withdraw(request={"2": 1,
                          "5": 2,
                          "10": 0,
                          "20": 0,
                          "50": 5,
                          "100": 0,
                          "200": 0})

        total_expected_value = 1 * 2 + 2 * 5 + 0 * 10 + 0 * 20 + 5 * 50 + 0 * 100 + 0 * 200 + user_repo.get_user(
            1).current_balance

        assert total_expected_value == response.get("current_balance")

    def test_post_deposit_suspect(self):
        with pytest.raises(fastapi.exceptions.HTTPException) as exc_info:

            response = deposit(request={"2": 1,
                                        "5": 2,
                                        "10": 0,
                                        "20": 0,
                                        "50": 5,
                                        "100": 0,
                                        "200": 300})

            withdraw(request={"2": 1,
                              "5": 2,
                              "10": 0,
                              "20": 0,
                              "50": 5,
                              "100": 0,
                              "200": 300})

        assert exc_info.value.status_code == 403
        assert exc_info.value.detail == "Depósito suspeito"

    def test_post_withdraw(self):
        user_repo = UserRepositoryMock()

        request = withdraw({
            "2": 0,
            "5": 2,
            "10": 2,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 0
        })

        deposit({
            "2": 0,
            "5": 2,
            "10": 2,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 0
        })

        keys = ['2', '5', '10', '20', '50', '100', '200']
        values = [0, 2, 2, 0, 0, 0, 0]

        total_expected_value = user_repo.get_user(user_id=in_use_id).current_balance - sum(int(k) * v for k, v in zip(keys, values))  #esta linha é a soma do valor total a ser sacado com o saldo atual do usuário

        assert total_expected_value == request['current_balance']

    def test_withdraw_insufficient_funds(self):
        with pytest.raises(fastapi.exceptions.HTTPException) as exc_info:
            response = withdraw(request={"2": 1,
                                         "5": 2,
                                         "10": 0,
                                         "20": 0,
                                         "50": 5,
                                         "100": 0,
                                         "200": 300})

            deposit(request={"2": 1,
                             "5": 2,
                             "10": 0,
                             "20": 0,
                             "50": 5,
                             "100": 0,
                             "200": 300})

        assert exc_info.value.status_code == 403
        assert exc_info.value.detail == "Saldo insuficiente para transação"

    def test_get_history(self):
        user_repo = UserRepositoryMock()
        transaction_repo = TransactionRepositoryMock()

        mock_transactions = [
            Transaction(
                type=TransactionTypeEnum.DEPOSIT,
                value=100.0,
                current_balance=1000.0,
                timestamp=1234567890.0,

            ),
            Transaction(
                type=TransactionTypeEnum.WITHDRAW,
                value=50.0,
                current_balance=950.0,
                timestamp=1234567891.0,

            )
        ]
        assert transaction_repo.create_transaction(1, mock_transactions[0])
