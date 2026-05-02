import os

class UsuarioView2:
    def __init__(self):
        # Cores para deixar o terminal com vida
        self.AZUL = '\033[94m'
        self.VERDE = '\033[92m'
        self.AMARELO = '\033[93m'
        self.RESET = '\033[0m'
        self.NEGRITO = '\033[1m'

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu(self):
        print(f"\n{self.AZUL}{'━' * 30}{self.RESET}")
        print(f"{self.NEGRITO}      SISTEMA DE USUÁRIOS{self.RESET}")
        print(f"{self.AZUL}{'━' * 30}{self.RESET}")
        print(f"{self.VERDE} 1 {self.RESET} ➜ Criar usuário")
        print(f"{self.VERDE} 2 {self.RESET} ➜ Listar usuários")
        print(f"{self.AMARELO} 0 {self.RESET} ➜ Sair")
        print(f"{self.AZUL}{'━' * 30}{self.RESET}")
        print(f"{self.NEGRITO}Escolha uma opção:{self.RESET} ", end="")

    def obter_dados_usuario(self):
        print(f"\n{self.AZUL}┌── Cadastro de Novo Usuário ──┐{self.RESET}")
        nome = input(f" │ Nome: ")
        email = input(f" │ Email: ")
        print(f"{self.AZUL}└──────────────────────────────┘{self.RESET}")
        return nome, email

    def mostrar_usuarios(self, usuarios):
        self.limpar_tela()
        print(f"\n{self.AZUL}┏{'━' * 42}┓{self.RESET}")
        print(f"{self.AZUL}┃{self.RESET} {self.NEGRITO}{'LISTA DE USUÁRIOS':^40} {self.AZUL}┃{self.RESET}")
        print(f"{self.AZUL}┣{'━' * 4}┳{'━' * 18}┳{'━' * 18}┫{self.RESET}")
        print(f"{self.AZUL}┃{self.RESET} ID {self.AZUL}┃{self.RESET} Nome             {self.AZUL}┃{self.RESET} Email            {self.AZUL}┃{self.RESET}")
        print(f"{self.AZUL}┣{'━' * 4}╋{'━' * 18}╋{'━' * 18}┫{self.RESET}")
        
        if not usuarios:
            print(f"{self.AZUL}┃{self.RESET}      Nenhum usuário cadastrado.      {self.AZUL}┃{self.RESET}")
        else:
            for u in usuarios:
                # Ajusta o espaçamento para caber na tabela
                nome = (u.nome[:15] + '..') if len(u.nome) > 16 else u.nome.ljust(16)
                email = (u.email[:15] + '..') if len(u.email) > 16 else u.email.ljust(16)
                print(f"{self.AZUL}┃{self.RESET} {str(u.id).ljust(2)} {self.AZUL}┃{self.RESET} {nome:<16} {self.AZUL}┃{self.RESET} {email:<16} {self.AZUL}┃{self.RESET}")
        
        print(f"{self.AZUL}┗{'━' * 4}┻{'━' * 18}┻{'━' * 18}┛{self.RESET}")

    def mostrar_mensagem(self, mensagem):
        # Destaca mensagens de sucesso ou avisos
        print(f"\n {self.AMARELO}» {mensagem}{self.RESET}")