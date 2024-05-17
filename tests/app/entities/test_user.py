import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_User:
    def test_user(self):
        user = User("test", 1, "1234-5", 0.0, True)
        assert user.name == "test"
        assert user.agencia == 1
        assert user.conta == "1234-5"
        assert user.current_balance == 0.0
        assert user.admin_permission == True

###NAME_TESTS###
    def test_user_name_not_none(self):
        with pytest.raises(ParamNotValidated):
            User(name=None, agencia=1, conta="1234-5", current_balance=0.0, admin_permission=True)

    def test_user_name_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name=0, agencia=1, conta="1234-5", current_balance=0.0, admin_permission=True)

    def test_user_name_len(self):
        with pytest.raises(ParamNotValidated):
            User(name="pa", agencia=1, conta="1234-5", current_balance=0.0, admin_permission=True)
###NAME_TESTS###

###AGENCIA_TESTS###
    def test_user_agencia_not_none(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=None, conta='1234-5', current_balance=0.0, admin_permission=True)

    def test_user_agencia_not_int1(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1.0, conta='1234-5', current_balance=0.0, admin_permission=True)
    def test_user_agencia_not_int2(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia='1.0', conta='1234-5', current_balance=0.0, admin_permission=True)
###AGENCIA_TESTS###

###CONTA_TESTS###
    def test_user_conta_not_none(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta=None, current_balance=0.0, admin_permission=True)

    def test_user_conta_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta=1, current_balance=0.0, admin_permission=True)

    def test_user_conta_format(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta='12345', current_balance=0.0, admin_permission=True)
###CONTA_TESTS###

###CBALANCE_TESTS###
    def test_user_cbalance_not_none(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta='1234-5', current_balance=None, admin_permission=True)

    def test_user_cbalance_not_float1(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta='1234-5', current_balance=1, admin_permission=True)
    def test_user_cbalance_not_float2(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta='1234-5', current_balance='1', admin_permission=True)

    def test_user_cbalance_not_negative(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta='1234-5', current_balance=-1, admin_permission=True)
###CBALANCE_TESTS###

###ADMINP_TEST###
    def test_user_admin_not_none(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta='1234-5', current_balance=0.0, admin_permission=None)

    def test_user_admin_not_bool(self):
        with pytest.raises(ParamNotValidated):
            User(name='test', agencia=1, conta='1234-5', current_balance=0.0, admin_permission='True')

    def test_user_to_dict(self):
        test_user = User(name='test', agencia=1, conta='1234-5', current_balance=0.0, admin_permission=True)
        assert test_user.to_dict() == {"name": "test",
                                       "agencia": 1,
                                       "conta": "1234-5",
                                       "current_balance": 0.0,
                                       "admin_permission": True}













