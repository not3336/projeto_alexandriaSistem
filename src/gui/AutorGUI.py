import customtkinter as ctk
from controllers.AutorController import AutorController
from widgets.AlertWidget import AlertWidget

class AutorGUI(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        self.autores = []
        self.lift()
        self.attributes("-topmost", True)
        self._configureWindow()
        self._createWidgets()
        self._loadAutores()
        self._loadWidgets()
        self.grab_set()
        
    def _configureWindow(self):
        self.geometry("800x600")
        self.resizable(0,0)
        self.title("Gerenciamento de Autores")

    def _createWidgets(self):
        self.frMain = ctk.CTkFrame(self, fg_color='white', corner_radius=0)
        self.frMenu = ctk.CTkFrame(self.frMain, fg_color='#0077b6', corner_radius=0)
        self.frContent = ctk.CTkFrame(self.frMain, fg_color='transparent', corner_radius=0)
        
        configBtMenu = {'font':("", 16), 'fg_color':'transparent', 'bg_color':'transparent', 
                        'corner_radius':0, 'text_color':"white", 'hover_color':"#023e8a"}
        
        self.btList = ctk.CTkButton(self.frMenu, text="Listar", command=self._loadListAutoresFrame, **configBtMenu)
        self.btSearch = ctk.CTkButton(self.frMenu, text="Pesquisar", command=self._loadSearchAutorFrame, **configBtMenu)
        self.btRegister = ctk.CTkButton(self.frMenu, text="Cadastrar", command=self._loadRegisterAutorFrame, **configBtMenu)
        self.btEdit = ctk.CTkButton(self.frMenu, text="Editar", command=self._loadEditAutorFrame, **configBtMenu)
        
    def _loadWidgets(self):
        self.frMain.pack(fill="both", expand=True)
        self.frMenu.pack(fill="x")
        
        self.btList.pack(side='left', padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btSearch.pack(side='left', padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btRegister.pack(side="left", padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btEdit.pack(side="left", padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        
        self.frContent.pack(fill='both', expand=True)
        self._loadListAutoresFrame()

    def _loadAutores(self):
        try:
            response = AutorController.getAllAutores()
            if response['type'] == 'Success':
                self.autores = response['autores']
            else:
                AlertWidget(self.root, response['type'], response['title'], "\n".join(response['message']))                
        except Exception as e:
            AlertWidget(self.root, 'Error', "Erro ao carregar usuarios", str(e))


    def _loadListAutoresFrame(self):

        def _deleteAutor(id):
            response = AutorController.deleteAutor(id)
            typeAlert, title, message = response.values()
            AlertWidget(self.root, typeAlert, title, message)
            if typeAlert == "Success":
                self.autores = list(filter(lambda autor: autor.id != id, self.autores))
                self._loadListAutoresFrame()


        self._cleanContentFrame()

        self.frTableLivros = ctk.CTkFrame(self.frContent, fg_color="#ced4da", corner_radius=0)
        
        self.frTableLivros.grid_columnconfigure(0, weight=1)
        self.frTableLivros.grid_columnconfigure(1, weight=10)
        self.frTableLivros.grid_columnconfigure(2, weight=3)
        self.frTableLivros.grid_columnconfigure(3, weight=3)
        self.frTableLivros.grid_columnconfigure(4, weight=1)
        configLabelColumn = {"text_color":"black", 'font':("", 18)}

        lbId = ctk.CTkLabel(self.frTableLivros, text="ID", **configLabelColumn)
        lbNome = ctk.CTkLabel(self.frTableLivros, text="NOME", **configLabelColumn)
        lbDataNasc = ctk.CTkLabel(self.frTableLivros, text="DATA DE NASCIMENTO", **configLabelColumn)
        lbNacionalidade = ctk.CTkLabel(self.frTableLivros, text="NACIONALIDADE", **configLabelColumn)
    
        
        self.frTableLivros.pack(fill="both", expand=True, ipadx=10, ipady=10)
        lbId.grid(row=0, column=0)
        lbNome.grid(row=0, column=1)
        lbDataNasc.grid(row=0, column=2)
        lbNacionalidade.grid(row=0, column=3)

        if len(self.autores) > 0:
            configLabelRow = {"text_color":"black", 'font':("", 15)}
            for row, autor in enumerate(self.autores):
                ctk.CTkLabel(self.frTableLivros, text=autor.id, **configLabelRow).grid(row=row+1, column=0)
                ctk.CTkLabel(self.frTableLivros, text=autor.nome, **configLabelRow).grid(row=row+1, column=1)
                ctk.CTkLabel(self.frTableLivros, text=autor.data_nasc, **configLabelRow).grid(row=row+1, column=2)
                ctk.CTkLabel(self.frTableLivros, text=autor.nacionalidade, **configLabelRow).grid(row=row+1, column=3)
                ctk.CTkButton(self.frTableLivros, text="Excluir", command=lambda: _deleteAutor(autor.id)).grid(row=row+1, column=4)
        else:
            ctk.CTkLabel(self.frTableLivros, text="Nenhum Autor Cadastrado").grid(row=1, column=0, columnspan=4, sticky="we")
    
    def _loadRegisterAutorFrame(self):
        
        def cleanFields(*fields):
            for f in fields:
                f.delete(0, 'end')
            
        def filterDataEntry(event):
            vk = event.keysym
            w = event.widget
            if vk != "BackSpace":
                try:
                    c = vbDataNasc.get()[-1]
                    try:
                        c = int(c)
                        l = len(w.get())
                        if l < 11:
                            if l in (2,5):
                                w.insert(l+1, "/")
                        else: 
                            w.delete(len(w.get())-1, 'end')
                    except ValueError:
                        w.delete(len(w.get())-1, 'end')
                except IndexError:
                    pass

        def registerAutor():
            nome = self.entryNome.get()
            data_nasc = self.entryDataNasc.get()
            nacionalidade = self.entryNacionalidade.get()

            response = AutorController.createAutor(nome, data_nasc, nacionalidade)

            AlertWidget(self.root, response['type'], response['title'], "\n".join(response['message']))

            self._loadAutores()
            
        self._cleanContentFrame()
        self.frRegister = ctk.CTkFrame(self.frContent, fg_color='transparent')
        frAutorData = ctk.CTkFrame(self.frRegister, fg_color='transparent', border_color='black', border_width=1)

        frDataRow1 = ctk.CTkFrame(frAutorData, fg_color='transparent')
        frDataRow2 = ctk.CTkFrame(frAutorData, fg_color='transparent')
        
        frButtons = ctk.CTkFrame(self.frRegister, fg_color='transparent')
        
        configLabelData = {'text_color':'black', 'font':("", 15)}
        configEntryData = {'corner_radius':0, 'border_color':"grey", 'fg_color':'#ced4da', 'text_color':'black'}
        
        vbDataNasc = ctk.StringVar()

        lbNome = ctk.CTkLabel(frDataRow1, text="Nome: ", **configLabelData)
        lbDataNasc = ctk.CTkLabel(frDataRow2, text="Data de Nascimento: ", **configLabelData)
        lbNacionalidade = ctk.CTkLabel(frDataRow2, text="Nacionalidade: ", **configLabelData)

        self.entryNome = ctk.CTkEntry(frDataRow1, **configEntryData)
        self.entryDataNasc = ctk.CTkEntry(frDataRow2, textvariable=vbDataNasc, **configEntryData)
        self.entryNacionalidade = ctk.CTkEntry(frDataRow2, **configEntryData)
        
        self.entryDataNasc.bind('<KeyRelease>', filterDataEntry)
        
        btRegister = ctk.CTkButton(frButtons, text="Cadastrar", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
                                 corner_radius=0, command=registerAutor)
        btCleanFields = ctk.CTkButton(frButtons, text="Limpar Campos", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
            corner_radius=0, command= lambda : cleanFields(self.entryNome, self.entryDataNasc, self.entryNacionalidade))

        self.frRegister.pack(fill='both', expand=True)
        ctk.CTkLabel(self.frRegister, text="Ficha de Cadastro", font=("", 18), text_color="black").pack(padx=5, pady=10, anchor='w')
        frAutorData.pack(pady=10, padx=5, fill='x')
        
        frDataRow1.pack(fill='x', padx=5, pady=(5,0))
        frDataRow2.pack(fill='x', padx=5, pady=(0,5))

        
        lbNome.pack(side="left", padx=(10,5), pady=10)
        self.entryNome.pack(side="left", expand=True, fill='x', pady=10)
        lbDataNasc.pack(side="left", padx=5, pady=10)
        self.entryDataNasc.pack(side="left", fill='x', pady=10, padx=(0,10))
        lbNacionalidade.pack(side="left", expand=True, padx=(10,5), pady=10)
        self.entryNacionalidade.pack(side="left", fill='x', pady=10)
        
        frButtons.pack(fill='x', padx=5, pady=10)
        btRegister.pack(side='right')
        btCleanFields.pack(side='right')
        
    def _loadSearchAutorFrame(self):
        self._cleanContentFrame()
        frSearch = ctk.CTkFrame(self.frContent, fg_color="transparent")
        frLivroData = ctk.CTkFrame(self.frContent, fg_color='transparent')
        
        entryID = ctk.CTkEntry(frSearch, placeholder_text="ID do Autor", corner_radius=0, border_color="grey", fg_color='#ced4da')
        btSearch = ctk.CTkButton(frSearch, text="Buscar", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
                                 corner_radius=0)

        frSearch.pack(fill='x', ipadx=10, ipady=10)
        frLivroData.pack(fill='both', expand=True, ipadx=10, ipady=10)
        entryID.pack(side='left', padx=10)
        btSearch.pack(side="left")
    
    def _loadEditAutorFrame(self):
        self._cleanContentFrame()
        frSearch = ctk.CTkFrame(self.frContent, fg_color="transparent")
        frLivroData = ctk.CTkFrame(self.frContent, fg_color='transparent')
        
        entryID = ctk.CTkEntry(frSearch, placeholder_text="ID do Autor", corner_radius=0, border_color="grey", fg_color='#ced4da')
        btSearch = ctk.CTkButton(frSearch, text="Buscar", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
                                 corner_radius=0)

        frSearch.pack(fill='x', ipadx=10, ipady=10)
        frLivroData.pack(fill='both', expand=True, ipadx=10, ipady=10)
        entryID.pack(side='left', padx=10)
        btSearch.pack(side="left")
     
    def _cleanContentFrame(self):
        for w in self.frContent.winfo_children():
            w.destroy()