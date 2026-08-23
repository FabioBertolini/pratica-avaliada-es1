import hashlib
from typing import List, Optional


class Usuario:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)

    def _hash_senha(self, senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios: List[Usuario] = []

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        for usuario in self.usuarios:
            if usuario.email == email:
                raise ValueError("Email já cadastrado")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        for usuario in self.usuarios:
            if usuario.email == email and usuario.validar_senha(senha):
                return usuario
        return None

    def listar_todos(self) -> List[Usuario]:
        return self.usuarios
