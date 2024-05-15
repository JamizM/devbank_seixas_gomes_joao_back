import pytest
from src.app.entities.User import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_User:
    def test_user(self):
        user = User("test", 1, "1234-5", 0.0, True)
        assert user.name == "test"
        assert user.agencia == 1
        assert user.conta == "1234-5"
        assert user.current_balance == 0.0
        assert user.admin_permission == True

    #Tratar erros esperados