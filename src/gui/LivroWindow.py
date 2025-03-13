import customtkinter as ctk
from tkinter import Event
from gui.AutorGUI import AutorGUI
from widgets.AlertWidget import AlertWidget
from controllers.AutorController import AutorController


#Essa classe é responsavél por exibir e gerenciar os livros da Biblioteca
#Optei por utilizar Frames no lugar de Toplevel, pois o sistema irá rodar quase tudo na janela CTk principal
class LivroWindow(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame, root: ctk.CTk):
        super().__init__(master)
        #Salva uma referência a tela CTk root
        self.root = root
        #Armazena os autores que serão exibidos no ComboBox
        self.autores = []
        self._configWindow()
        self._createWidgets()
        self._loadWidgets()
        
    def _configWindow(self):
        #Deixa o frame transparent e com bordas quadradas
        self.configure(fg_color="transparent")
        self.configure(bg_color="transparent")
        self.configure(corner_radius=0)
        
    def _createWidgets(self):
        #Frames principal
        self.frMain = ctk.CTkFrame(self, fg_color='transparent', corner_radius=0)
        #Frame que exibirá o menu de opções
        self.frMenu = ctk.CTkFrame(self.frMain, fg_color='#0077b6', corner_radius=0)
        #Frame que exibirá as demais conteúdo dos menus
        self.frContent = ctk.CTkFrame(self.frMain, fg_color='transparent', corner_radius=0)
        
        configBtMenu = {'font':("", 16), 'fg_color':'transparent', 'bg_color':'transparent', 
                        'corner_radius':0, 'text_color':"white", 'hover_color':"#023e8a"}
        
        self.lbTitle = ctk.CTkLabel(self.frMain, text="Gerenciamento de Livros", font=("", 25), text_color="black")
        
        self.btList = ctk.CTkButton(self.frMenu, text="Listar", command=self._loadListLivros, **configBtMenu)
        self.btSearch = ctk.CTkButton(self.frMenu, text="Pesquisar", command=self._loadSearchLivro, **configBtMenu)
        self.btRegister = ctk.CTkButton(self.frMenu, text="Cadastrar", command=self._loadRegisterLivro, **configBtMenu)
        self.btEdit = ctk.CTkButton(self.frMenu, text="Editar", command=self._loadEditLivro, **configBtMenu)
            
    def _loadWidgets(self):
        self.frMain.pack(fill="both", expand=True)
        self.lbTitle.pack(fill="x")
        self.frMenu.pack(fill="x")
        
        self.btList.pack(side='left', padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btSearch.pack(side='left', padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btRegister.pack(side="left", padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btEdit.pack(side="left", padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        
        self.frContent.pack(fill='both', expand=True)
        #Exibe o frame que contem a lista de todos os livros
        self._loadListLivros()
    
    def _loadListLivros(self):
        #Essa função carregará uma tela contendo uma tabela com todos os livros armazenados

        #Limpa as possíveis telas já abertas no frContent
        self._cleanContentFrame()
        #Será exibido os livros contidos no banco de dados em forma de tabela, contendo um botão para excluir.
        self.frTableLivros = ctk.CTkFrame(self.frContent, fg_color="#ced4da", corner_radius=0)
        
        self.frTableLivros.grid_columnconfigure(0, weight=1)
        self.frTableLivros.grid_columnconfigure(1, weight=10)
        self.frTableLivros.grid_columnconfigure(2, weight=4)
        self.frTableLivros.grid_columnconfigure(3, weight=3)
        self.frTableLivros.grid_columnconfigure(4, weight=1)
        self.frTableLivros.grid_columnconfigure(5, weight=2)
        
        lbId = ctk.CTkLabel(self.frTableLivros, text="ID", text_color="black")
        lbTitulo = ctk.CTkLabel(self.frTableLivros, text="TÍTULO", text_color="black")
        lbAutor = ctk.CTkLabel(self.frTableLivros, text="AUTOR", text_color="black")
        lbGenero = ctk.CTkLabel(self.frTableLivros, text="GÊNERO", text_color="black")
        lbQuantCopias = ctk.CTkLabel(self.frTableLivros, text="PREÇO", text_color="black")
        lbQuantDisponivel = ctk.CTkLabel(self.frTableLivros, text="ESTOQUE", text_color="black")
        
        self.frTableLivros.pack(fill="both", expand=True, ipadx=10, ipady=10)
        lbId.grid(row=0, column=0)
        lbTitulo.grid(row=0, column=1)
        lbAutor.grid(row=0, column=2)
        lbGenero.grid(row=0, column=3)
        lbQuantCopias.grid(row=0, column=4)
        lbQuantDisponivel.grid(row=0, column=5)
    
    def _loadRegisterLivro(self):
        #Função responsável por limpar os dados dos entrys e combobox
        def cleanFields():
            self.entryTitulo.delete(0, 'end')
            self.entryQuantCopias.delete(0, 'end')
            self.entryQuantDisponivel.delete(0, 'end')
            self.cbAutor.set("")
            self.cbGenero.set("")

        #Função que permite o usuário digitar apenas números nos entry quant. Disponível e de Copias
        def filterOnlyNumberEntry(event: Event, vb: ctk.StringVar):
            vk = event.keysym
            v = vb.get()
            w = event.widget
            
            if vk != "BackSpace":
                try:
                    c = v[-1] #Pega o ultimo caracter digitado
                    try:
                        c = int(c) #Verifica se o caracter digita é inteiro
                    except ValueError:
                        w.delete(len(w.get())-1, 'end') #Se o caracter não for inteiro, o mesmo será apagado
                except IndexError:
                    #Caso a StringVar esteja vazia, não faz nada
                    pass
            
        #Função que realizará a consulta a tabela Autores e retornará todos os autores cadastrados
        def _loadAutores():
            try:
                #Faz a busca por todos os autores no banco de dados
                response = AutorController.getAllAutores()
                if response['type'] == "Success": #Caso a resposta sejá Success
                    self.autores = response['autores'] # Armazena todos os autores na variável de instância
                else:
                    #Caso a resposta sejá Error ou Warning, exibe um alerta
                    AlertWidget(self.root, response['type'], response['title'], "\n".join(response['message']))
            except Exception as e:
                #Caso aconteça alguma Exception, exibe o erro que aconteceu
                AlertWidget(self.root, "Error", "Erro ao tentar consultar autores", str(e))


        self._cleanContentFrame()
        self.frRegister = ctk.CTkFrame(self.frContent, fg_color='transparent')
        frLivroData = ctk.CTkFrame(self.frRegister, fg_color='transparent', border_color='black', border_width=1)

        frDataRow1 = ctk.CTkFrame(frLivroData, fg_color='transparent')
        frDataRow2 = ctk.CTkFrame(frLivroData, fg_color='transparent')
        frDataRow3 = ctk.CTkFrame(frLivroData, fg_color='transparent')

        frButtons = ctk.CTkFrame(self.frRegister, fg_color='transparent')
        
        configLabelData = {'text_color':'black', 'font':("", 15)}
        configEntryData = {'corner_radius':0, 'border_color':"grey", 'fg_color':'#ced4da', 'text_color':'black'}
        confButtonCad = {'fg_color': "#0077b6", 'hover_color': "#023e8a",
                         'text_color':"white", 'corner_radius': 0}
        
        lbTitulo = ctk.CTkLabel(frDataRow1, text="Título: ", **configLabelData)
        lbISBN = ctk.CTkLabel(frDataRow2, text="ISBN: ", **configLabelData)
        lbAutor = ctk.CTkLabel(frDataRow2, text="Autor: ", **configLabelData)
        lbGenero = ctk.CTkLabel(frDataRow3, text="Gênero: ", **configLabelData)
        lbQuantCopias = ctk.CTkLabel(frDataRow3, text="Quant. Copias: ", **configLabelData)
        lbQuantDisponivel = ctk.CTkLabel(frDataRow3, text="Quant. Disponível: ", **configLabelData)
        
        _loadAutores() #Faz a busca por todos os autores cadastrados na tabela autores

        vbQuantCopias = ctk.StringVar()
        vbQuantDisponivel = ctk.StringVar()
        vbISBN = ctk.StringVar()

        self.entryTitulo = ctk.CTkEntry(frDataRow1, **configEntryData)
        self.entryISBN = ctk.CTkEntry(frDataRow2, textvariable=vbISBN, **configEntryData)
        self.cbAutor = ctk.CTkComboBox(frDataRow2, state="readonly", values=[autor.nome for autor in self.autores], #Pega apenas os nomes dos autores
                                        **configEntryData)
        self.cbGenero = ctk.CTkComboBox(frDataRow3, state="readonly", **configEntryData)
        self.entryQuantCopias = ctk.CTkEntry(frDataRow3, width=60, textvariable=vbQuantCopias, **configEntryData)
        self.entryQuantDisponivel = ctk.CTkEntry(frDataRow3, width=60, textvariable=vbQuantDisponivel,**configEntryData)
        
        #Adiciona a função de filtro ao evento de pressionar botão nas Entrys
        self.entryISBN.bind("<KeyRelease>", lambda event: filterOnlyNumberEntry(event, vbISBN))
        self.entryQuantCopias.bind('<KeyRelease>', lambda event: filterOnlyNumberEntry(event, vbQuantCopias))
        self.entryQuantDisponivel.bind('<KeyRelease>', lambda event: filterOnlyNumberEntry(event, vbQuantDisponivel))
        
        self.btCadAutor = ctk.CTkButton(frDataRow2,text="+", width=30, command= self._openAutorGUI, **confButtonCad)
        self.btCadGenero = ctk.CTkButton(frDataRow3, text="+", width=30, **confButtonCad)
        btRegister = ctk.CTkButton(frButtons, text="Cadastrar", **confButtonCad)
        btCleanFields = ctk.CTkButton(frButtons, text="Limpar Campos", **confButtonCad, command=cleanFields)

        self.frRegister.pack(fill='both', expand=True)
        ctk.CTkLabel(self.frRegister, text="Ficha de Cadastro", font=("", 18), text_color="black").pack(padx=5, pady=10, anchor='w')
        frLivroData.pack(pady=10, padx=5, fill='x')
        
        frDataRow1.pack(fill='x', padx=5, pady=(5,0))
        frDataRow2.pack(fill='x', padx=5, pady=(0,5))
        frDataRow3.pack(fill='x', padx=5, pady=(0,5))    
                
        lbTitulo.pack(side="left", padx=5, pady=10)
        self.entryTitulo.pack(side="left", expand=True, fill='x', pady=10)
        lbISBN.pack(side="left", padx=5, pady=10)
        self.entryISBN.pack(side="left", pady=10)
        lbAutor.pack(side="left", padx=5, pady=10)
        self.cbAutor.pack(side="left", fill='x', expand=True, pady=10, padx=(0,5))
        self.btCadAutor.pack(side="left", pady=10, padx=(0,5))
        lbGenero.pack(side="left", padx=5, pady=10)
        self.cbGenero.pack(side="left", fill='x', expand=True, pady=10, padx=(0,5))
        self.btCadGenero.pack(side="left", pady=10, padx=(0,5))
        lbQuantCopias.pack(side="left", padx=(0,5), pady=10)
        self.entryQuantCopias.pack(side="left", pady=10, padx=(0,5))
        lbQuantDisponivel.pack(side="left", padx=(0,5), pady=10)
        self.entryQuantDisponivel.pack(side="left", pady=10, padx=(0,5))
        
        frButtons.pack(fill='x', padx=5, pady=10)
        btRegister.pack(side='right')
        btCleanFields.pack(side='right')
        
    def _loadSearchLivro(self):
        #Faz o carregamento da tela de pesquisa de livros por ID
        self._cleanContentFrame()
        frSearch = ctk.CTkFrame(self.frContent, fg_color="transparent")
        frLivroData = ctk.CTkFrame(self.frContent, fg_color='transparent')
        
        entryID = ctk.CTkEntry(frSearch, placeholder_text="ID do Livro", corner_radius=0, border_color="grey", fg_color='#ced4da')
        btSearch = ctk.CTkButton(frSearch, text="Buscar", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
                                 corner_radius=0)

        frSearch.pack(fill='x', ipadx=10, ipady=10)
        frLivroData.pack(fill='both', expand=True, ipadx=10, ipady=10)
        entryID.pack(side='left', padx=10)
        btSearch.pack(side="left")
    
    def _loadEditLivro(self):
        #Faz o carregamento da tela de edição de livros cadastrados
        self._cleanContentFrame()
        frSearch = ctk.CTkFrame(self.frContent, fg_color="transparent")
        frLivroData = ctk.CTkFrame(self.frContent, fg_color='transparent')
        
        entryID = ctk.CTkEntry(frSearch, placeholder_text="ID do cliente", corner_radius=0, border_color="grey", fg_color='#ced4da')
        btSearch = ctk.CTkButton(frSearch, text="Buscar", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
                                 corner_radius=0)

        frSearch.pack(fill='x', ipadx=10, ipady=10)
        frLivroData.pack(fill='both', expand=True, ipadx=10, ipady=10)
        entryID.pack(side='left', padx=10)
        btSearch.pack(side="left")
     
    def _openAutorGUI(self):
        #Abre a janela de gerenciamento de autores
        autorGUI = AutorGUI(self.root)
             
    def _cleanContentFrame(self):
        for w in self.frContent.winfo_children():
            w.destroy()