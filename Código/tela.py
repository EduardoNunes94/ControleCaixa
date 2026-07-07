import customtkinter as ctk



def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'eduardo' and senha == '12345':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
        app.withdraw()
        tela_menu()

    else    :
        resultado_login.configure(text='Usuário ou senha incorreto!', text_color='white',font=('arial',12,'bold'))


def tela_menu():
    
    janela_menu = ctk.CTkToplevel(app)
    janela_menu.configure(fg_color='green')
    janela_menu.title('MENU')
    janela_menu.geometry('400x500') 
    

    def cadastro_prod():
        janela_menu.withdraw()
        tela_cad = ctk.CTkToplevel(janela_menu)
        tela_cad.title('CADASTRO DE PRODUTOS')
        tela_cad.configure(fg_color='green')
        tela_cad.geometry('400x500')
        lbl = ctk.CTkLabel(tela_cad,text='ARÉA DE CADASTRO',font=('arial',12,'bold'),text_color='white')
        lbl.pack(pady=50)

        def voltar_menu():
            tela_cad.destroy()
            janela_menu.deiconify()

        botaoSairCad = ctk.CTkButton(tela_cad,text='Voltar ao MENU',text_color='white',command=voltar_menu)
        botaoSairCad.place(x=10, y=10)
        botaoSairCad.configure(fg_color='#06402b', hover_color='#009929')

    def cadastro_pedido():
        janela_menu.withdraw()
        cadastro_pedido = ctk.CTkToplevel(janela_menu)
        cadastro_pedido.title('PEDIDOS')
        cadastro_pedido.configure(fg_color='green')
        cadastro_pedido.geometry('400x500')
        lbl = ctk.CTkLabel(cadastro_pedido,text='PEDIDOS',font=('arial',12,'bold'),text_color='white')
        lbl.pack(pady=40)

        def voltar_menu():
            cadastro_pedido.destroy()
            janela_menu.deiconify()

        botaoSairPed = ctk.CTkButton(cadastro_pedido,text='Voltar ao MENU',text_color='white',command=voltar_menu)
        botaoSairPed.place(x=10, y=10)
        botaoSairPed.configure(fg_color='#06402b', hover_color='#009929')



    def voltar():
        janela_menu.withdraw()
        app.deiconify()
        campo_senha.delete(0, 'end')
        campo_usuario.delete(0, 'end')


    # botões do menu 

    botaoPed = ctk.CTkButton(janela_menu,text='PEDIDOS', text_color='white',command=cadastro_pedido)
    botaoPed.pack(pady=15)
    botaoPed.configure(fg_color='#06402b',hover_color='#009929')
    botaoCad = ctk.CTkButton(janela_menu,text='CADASTRO DE PRODUTOS',text_color='white',command=cadastro_prod)
    botaoCad.pack(pady=15)
    botaoCad.configure(fg_color='#06402b',hover_color='#009929')
    botaoSair = ctk.CTkButton(janela_menu,text='SAIR',text_color='white',font=('arial',12,'bold'),command=voltar)
    botaoSair.pack(pady=15)
    botaoSair.configure(fg_color='#06402b',hover_color='#009929')





    



# ------- Criação da janela inicial

app = ctk.CTk()
app.title('CONTROLE DE CAIXA')
app.geometry('400x500')
app.configure(fg_color='green')

# ------- label - nome que fica em cima da caixa de digitação

label_usuario = ctk.CTkLabel(app,text='Usuário',font=('arial',15,'bold'))
label_usuario.pack(pady=5)

# ------- entry - campo onde digita o usuário

campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=5)

# ------- label senha

label_senha = ctk.CTkLabel(app,text='Senha',font=('arial',15,'bold'))
label_senha.pack(pady=5)

# ------- entry senha

campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=5)

# ------- Botão login

botao_login = ctk.CTkButton(app,text='Login',text_color='white',font=('arial',12,'bold'),command=validar_login)
botao_login.pack(pady=10)
botao_login.configure(fg_color='#06402b',hover_color='#009929')


# ------- campo feedback login

resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

# ------- Mensagem de texto no rodapé

msg_rodape = ctk.CTkLabel(app,text='SISTEMA EM TESTE!',text_color='black',font=('arial', 20))
msg_rodape.pack(pady=100)

# ------- Mensagem de texto no rodapé

msg_rodape = ctk.CTkLabel(app,text='VILA NOVA F.C.', text_color='black', font=('arial',15,'bold'))
msg_rodape.pack(pady=3)





app.mainloop()






















