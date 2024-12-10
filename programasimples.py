import tkinter as tk
from tkinter import messagebox

# Importa o módulo tkinter para criar a interface gráfica
# Importa o messagebox para exibir mensagens em janelas pop-up

# Função que será executada quando o botão for clicado
def enviar_dados():
    nome = entrada_nome.get()  # Obtém o nome digitado na caixa de entrada correspondente
    idade = entrada_idade.get()  # Obtém a idade digitada na caixa de entrada correspondente
    
    # Exibe uma mensagem personalizada em uma janela pop-up
    mensagem = f"Obrigado, {nome}!\nVocê tem {idade} anos. É um prazer conhecê-lo!"
    messagebox.showinfo("Mensagem", mensagem)

# Criação da janela principal
janela = tk.Tk()  # Inicializa a janela principal
janela.title("Introdução ao Python com Tkinter")  # Define o título da janela
janela.geometry("300x200")  # Define o tamanho da janela (largura x altura)

# Rótulo e entrada para o nome
tk.Label(janela, text="Digite seu nome:").pack(pady=5)  # Adiciona um texto explicativo para o campo do nome
entrada_nome = tk.Entry(janela)  # Cria uma caixa de entrada para o usuário digitar o nome
entrada_nome.pack(pady=5)  # Posiciona a caixa de entrada na janela

# Rótulo e entrada para a idade
tk.Label(janela, text="Digite sua idade:").pack(pady=5)  # Adiciona um texto explicativo para o campo da idade
entrada_idade = tk.Entry(janela)  # Cria uma caixa de entrada para o usuário digitar a idade
entrada_idade.pack(pady=5)  # Posiciona a caixa de entrada na janela

# Botão para enviar os dados
tk.Button(janela, text="Enviar", command=enviar_dados).pack(pady=10)  # Cria um botão que chama a função enviar_dados quando clicado

# Inicia o loop principal da interface gráfica
janela.mainloop()  # Mantém a janela aberta até que o usuário a feche