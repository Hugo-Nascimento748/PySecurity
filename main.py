import customtkinter as ctk
from engine import salvar_senha, listar_senhas, deletar_senha

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PySecurity - Gerenciador de Senhas")
        self.geometry("500x600")

        self.label_titulo = ctk.CTkLabel(self, text="MEU COFRE DE SENHAS", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.entry_servico = ctk.CTkEntry(self, placeholder_text="Nome do Serviço (ex: Gmail)")
        self.entry_servico.pack(pady=10, padx=20, fill="x")

        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Sua Senha", show="*")
        self.entry_senha.pack(pady=10, padx=20, fill="x")

        self.botao_salvar = ctk.CTkButton(self, text="Salvar Senha", command=self.acao_salvar)
        self.botao_salvar.pack(pady=10)

        self.botao_excluir = ctk.CTkButton(self, text="Excluir por Nome", 
                                          fg_color="#cc3333", hover_color="#991111",
                                          command=self.acao_excluir)
        self.botao_excluir.pack(pady=5)

        self.textbox_lista = ctk.CTkTextbox(self, width=450, height=200, state="disabled")
        self.textbox_lista.pack(pady=10, padx=20)

        self.botao_listar = ctk.CTkButton(self, text="Ver Senhas Salvas", fg_color="transparent", border_width=2, command=self.acao_listar)
        self.botao_listar.pack(pady=10)

        
        self.after(100, lambda: self.entry_servico.focus())

    def acao_salvar(self):
        servico = self.entry_servico.get()
        senha = self.entry_senha.get()
        if servico and senha:
            salvar_senha(servico, senha)
            self.entry_servico.delete(0, 'end')
            self.entry_senha.delete(0, 'end')
            self.acao_listar() # Atualiza a lista automaticamente

    def acao_listar(self):
        # Habilita para escrever, limpa, escreve e desabilita
        self.textbox_lista.configure(state="normal")
        self.textbox_lista.delete("0.0", "end")
        
        senhas = listar_senhas()
        for servico, senha in senhas:
            self.textbox_lista.insert("end", f"Serviço: {servico} | Senha: {senha}\n")
        
        self.textbox_lista.configure(state="disabled")

    def acao_excluir(self):
        servico = self.entry_servico.get()
        if servico:
            deletar_senha(servico)
            self.entry_servico.delete(0, 'end')
            self.acao_listar() 

if __name__ == "__main__":
    app = App()
    app.mainloop()