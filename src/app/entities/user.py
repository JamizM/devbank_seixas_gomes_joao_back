from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum
import re #importado para a verificação de senha


class User:
    name: str
    agencia: str
    conta: str
    current_balance: float
    admin_permission: bool = False
    
    def __init__(self, name: str=None, agencia: str = None, conta: str=None, current_balance:float=None, admin_permission: bool=None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("nome", validation_name[1])
        self.name = name
        
        validation_agencia = self.validate_agencia(agencia)
        if validation_agencia[0] is False:
            raise ParamNotValidated("agencia", validation_agencia[1])
        self.agencia = agencia

        validation_conta = self.validate_conta(conta)
        if validation_conta[0] is False:
            raise ParamNotValidated("conta", validation_conta[1])
        self.conta = conta

        valodation_current_balance = self.validate_current_balance(current_balance)
        if valodation_current_balance[0] is False:
            raise ParamNotValidated("Saldo", valodation_current_balance[1])
        self.current_balance = current_balance
        
        validation_admin_permission = self.validate_admin_permission(admin_permission)
        if validation_admin_permission[0] is False:
            raise ParamNotValidated("admin_permission", validation_admin_permission[1])
        self.admin_permission = admin_permission

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Nome é necessário")
        if type(name) != str:
            return (False, "Nome precisa ser uma string")
        if len(name) < 3:
            return (False, "Nome precisa ter pelo menos 3 caracteres")
        return (True, "")
        
    @staticmethod
    def validate_agencia(agencia: str) -> Tuple[bool, str]:
        if agencia is None:
            return (False, "Uma agência é necesária")
        if type(agencia) != str:
            return (False, "A agência precisa ser uma string")
        if len(agencia) != 4:
            return (False, "A agência precisa conter apenas 4 digitos")

        try:
            int(agencia)
        except ValueError:
            return (False, "A agencia precisa conter 4 digitos no formato (xxxx), com x indo de 0 a 9")

        return (True, "")
    
    @staticmethod
    def validate_conta(conta: str) -> Tuple[bool, str]:
        if conta is None:
            return (False, "É necessária uma conta")
        if type(conta) != str:
            return (False, "A conta precisa ser uma string")
        else:
            if "-" not in conta:
                return (False, "Toda conta precisa de um '-' ")
        return (True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Saldo é necessário")
        if type(current_balance) != float:
            return (False, "Saldo precisa ser um float")
        if current_balance < 0:
            return (False, "Saldo precisa ser um número positivo")
        return (True, "")
    
    @staticmethod
    def validate_admin_permission(admin_permission: bool) -> Tuple[bool, str]:
        if admin_permission is None:
            return (False, "Permissão de administrador é necessária")
        if type(admin_permission) != bool:
            return (False, "Permissão de administrador precisa ser um booleano")
        return (True, "")
            
    def to_dict(self):
        return {
            "name": self.name,
            "agencia": self.agencia,
            "conta": self.conta,
            "current_balance": self.current_balance,
            "admin_permission": self.admin_permission
        }
    
    def __eq__(self,other):
        return self.name == other.name and self.agencia == other.agencia and self.conta == other.conta
    
    def __repr__(self):
        return f"Item(name={self.name}, agencia={self.agencia}, conta={self.conta})"