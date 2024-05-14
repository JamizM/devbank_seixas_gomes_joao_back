from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum
import re #importado para a verificação de senha


class User:
    name: str
    agencia: int
    conta: str
    admin_permission: bool = False
    email: str
    senha: str

    
    def __init__(self, name: str=None, agencia: int = None, conta: str=None, admin_permission: bool=None, email:str=None, senha:str=None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name
        
        validation_agencia = self.validate_agencia(agencia)
        if validation_agencia[0] is False:
            raise ParamNotValidated("agencia", validation_agencia[1])
        self.agencia = agencia

        validation_conta = self.validate_conta(conta)
        if validation_conta[0] is False:
            raise ParamNotValidated("conta", validation_conta[1])
        self.conta = conta
        
        validation_admin_permission = self.validate_admin_permission(admin_permission)
        if validation_admin_permission[0] is False:
            raise ParamNotValidated("admin_permission", validation_admin_permission[1])
        self.admin_permission = admin_permission

        validation_email = self.validate_email(email)
        if validation_email[0] is False:
            raise ParamNotValidated("admin_permission", validation_email[1])
        self.email= email

        validation_password = self.validate_password(senha)
        if not validation_password[0]:
            raise ParamNotValidated("senha", validation_password[1])
        self.senha = senha
        
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
    def validate_agencia(agencia: int) -> Tuple[bool, str]:
        if agencia is None:
            return (False, "Uma agência é necesária")
        if type(agencia) != int:
            return (False, "A agência precisa ser um inteiro")
        return (True, "")
    
    @staticmethod
    def validate_conta(conta: str) -> Tuple[bool, str]:
        if conta is None:
            return (False, "É necessária uma conta")
        if "-" not in conta:
            return(False, "Toda conta precisa de um '-' ")
        return (True, "")
    
    @staticmethod
    def validate_admin_permission(admin_permission: bool) -> Tuple[bool, str]:
        if admin_permission is None:
            return (False, "Admin permission é necessária")
        if type(admin_permission) != bool:
            return (False, "Admin permission precisa ser um booleano")
        return (True, "")
        
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        if email is None:
            return (False, "É necessário um email")

        if type(email) != str:
            return (False, "Email precisa ser uma string")
        
        if "@" not in email:
            return(False, "Email inválido")

        return (True, "")
    
    @staticmethod
    def validate_senha(senha: str) -> Tuple[bool, str]:
        if senha is None:
            return (False, "Senha é necessária")
        if len(senha) < 8:
            return(False, "Senha deve ter ao mínimo 8 caracteres")
        if not re.search("[a-z]", senha) or not re.search("[A-Z]", senha) or not re.search("[0-9]", senha):
            return (False, "Senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um número")
        return (True, "")
        

    
        
    def to_dict(self):
        return {
            "name": self.name,
            "agencia": self.agencia,
            "conta": self.conta,
            "admin_permission": self.admin_permission,
            "email": self.email,
            "senha": self.senha
        }
    
    def __eq__(self,other):
        return self.name == other.name and self.agencia == other.agencia and self.conta == other.conta and self.admin_permission == other.admin_permission and self.email == other.email and self.senha == other.senha
    
    def __repr__(self):
        return f"Item(name={self.name}, agencia={self.agencia}, conta={self.conta}, admin_permission={self.admin_permission}, email = {self.email}, senha={self.senha})"