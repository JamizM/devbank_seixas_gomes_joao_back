from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .enums.transaction_type_enum import TransactionTypeEnum

from .entities.transaction import Transaction

app = FastAPI()

user_repo = Environments.get_user_repo()
transaction_repo = Environments.get_transaction_repo()

in_use_id = 1
factor = 2

@app.get("/")
def get_user():

    user = user_repo.get_user(user_id=in_use_id)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    return user.to_dict()

# @app.get("/users/get_all_users")
# def get_all_items():
#     users = user_repo.get_all_users()
#     json = {}
#
#     for user in users:
#         json["user_id: " + str(users[0])]: user.to_dict()
#
#     return json

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#
#     user = user_repo.get_user(user_id)
#
#     if not user:
#         raise HTTPException(status_code=400, detail="User not found")
#
#     return user.to_dict()

@app.post("/deposit")
def deposit(request: dict):

    model = {
        "2": 0,
        "5": 0,
        "10": 0,
        "20": 0,
        "50": 0,
        "100": 0,
        "200": 0
    }

    transaction_value = 0.0

    for key in request:
        print(model.get(key, None))
        if model.get(key, None) is not None:
            transaction_value += int(key) * float(request[key])

    user = user_repo.get_user(user_id=in_use_id)

    if transaction_value >= user.current_balance * factor:
        raise HTTPException(status_code=403, detail="Depósito suspeito")

    user.current_balance += transaction_value

    transaction = Transaction(type=TransactionTypeEnum.DEPOSIT,
                              value=transaction_value,
                              current_balance=user.current_balance,
                              timestamp=1001.0)

    transaction_repo.create_transaction(transaction_id=int((transaction.current_balance*transaction.value)/1000),
                                        transaction=transaction)

    return {
        "current_balance": transaction.current_balance,
        "timestamp": transaction.timestamp
    }



@app.post("/withdraw")
def withdraw(request: dict):

    model = {
        "2": 0,
        "5": 0,
        "10": 0,
        "20": 0,
        "50": 0,
        "100": 0,
        "200": 0
    }

    transaction_value = 0.0

    for key in request:
        if model.get(key, None) is not None:
            transaction_value += int(key) * float(request[key])

    user = user_repo.get_user(user_id=in_use_id)

    if transaction_value > user.current_balance: #caso valor da transacao seja maior que o saldo do usuario
        raise HTTPException(status_code=403, detail="Saldo insuficiente para transação")

    user.current_balance -= transaction_value #atualiza o saldo do usuario caso a transacao seja possivel

    transaction = Transaction(type=TransactionTypeEnum.WITHDRAW,
                              value=transaction_value,
                              current_balance=user.current_balance,
                              timestamp=1001.0)

    transaction_repo.create_transaction(transaction_id=int((transaction.current_balance*transaction.value)/1000),
                                        transaction=transaction) #registrando uma nova transação com um ID específico no repositório de transações.

    return {
        "current_balance": transaction.current_balance,
        "timestamp": transaction.timestamp
    }


handler = Mangum(app, lifespan="off")

