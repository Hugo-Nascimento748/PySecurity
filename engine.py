from cryptography.fernet import Fernet
import os

def carregar_chave():
    if not os.path.exists("chave.key"):
        chave = Fernet.generate_key()
        with open("chave.key", "wb") as arquivo_chave:
            arquivo_chave.write(chave)
    return open("chave.key", "rb").read()

def criptografar_senha(senha_pura):
    chave = carregar_chave()
    f = Fernet(chave)
    return f.encrypt(senha_pura.encode())

def descriptografar_senha(senha_travada):
    chave = carregar_chave()
    f = Fernet(chave)
    return f.decrypt(senha_travada).decode()

def salvar_senha(servico, senha_pura):
    senha_travada = criptografar_senha(senha_pura)
    with open("senhas.txt", "a") as arquivo:
        
        arquivo.write(f"{servico.strip()}:{senha_travada.decode()}\n")

def listar_senhas():
    if not os.path.exists("senhas.txt"):
        return []
    lista_final = []
    with open("senhas.txt", "r") as arquivo:
        for linha in arquivo:
            if ":" in linha: 
                servico, senha_travada = linha.strip().split(":")
                senha_aberta = descriptografar_senha(senha_travada.encode())
                lista_final.append((servico, senha_aberta))
    return lista_final

def deletar_senha(servico_para_apagar):
    if not os.path.exists("senhas.txt"):
        return
    linhas_que_ficam = []
    with open("senhas.txt", "r") as arquivo:
        for linha in arquivo:
            if ":" in linha: 
                servico, senha_travada = linha.strip().split(":")
                
                if servico.strip().lower() != servico_para_apagar.strip().lower():
                    linhas_que_ficam.append(linha)
    
    with open("senhas.txt", "w") as arquivo:
        arquivo.writelines(linhas_que_ficam)