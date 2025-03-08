import customtkinter as ctk
from gui.AutorGUI import AutorGUI

class LivroWindow(ctk.CTkFrame):
    def __init__(self, master, root):
        super().__init__(master)
        self.root = root
        self._configWindow()
        self._createWidgets()
        self._loadWidgets()
        
    def _configWindow(self):
        self.configure(fg_color="transparent")
        self.configure(bg_color="transparent")
        self.configure(corner_radius=0)
        
    def _createWidgets(self):
        self.frMain = ctk.CTkFrame(self, fg_color='transparent', corner_radius=0)
        self.frMenu = ctk.CTkFrame(self.frMain, fg_color='#0077b6', corner_radius=0)
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
        self._loadListLivros()
    
    def _loadListLivros(self):
        self._cleanContentFrame()
        
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
        
        def cleanFields(*fields):
            for f in fields:
                f.delete(0, 'end')
           
        def filterEstoqueEntry(event):
            vk = event.keysym
            w = event.widget
            if vk != "BackSpace":
                try:
                    c = vk
                    try:
                        c = int(c)
                    except ValueError:
                        w.delete(len(w.get())-1, 'end')
                except IndexError:
                    pass
            
        self._cleanContentFrame()
        self.frRegister = ctk.CTkFrame(self.frContent, fg_color='transparent')
        frLivroData = ctk.CTkFrame(self.frRegister, fg_color='transparent', border_color='black', border_width=1)

        frDataRow1 = ctk.CTkFrame(frLivroData, fg_color='transparent')
        frDataRow2 = ctk.CTkFrame(frLivroData, fg_color='transparent')
        
        frButtons = ctk.CTkFrame(self.frRegister, fg_color='transparent')
        
        configLabelData = {'text_color':'black', 'font':("", 15)}
        configEntryData = {'corner_radius':0, 'border_color':"grey", 'fg_color':'#ced4da', 'text_color':'black'}
        
        lbTitulo = ctk.CTkLabel(frDataRow1, text="Título: ", **configLabelData)
        lbAutor = ctk.CTkLabel(frDataRow2, text="Autor: ", **configLabelData)
        lbGenero = ctk.CTkLabel(frDataRow1, text="Gênero: ", **configLabelData)
        lbQuantCopias = ctk.CTkLabel(frDataRow2, text="Quant. Copias: ", **configLabelData)
        lbQuantDisponivel = ctk.CTkLabel(frDataRow2, text="Quant. Disponível: ", **configLabelData)
        
        self.entryTitulo = ctk.CTkEntry(frDataRow1, **configEntryData)
        self.cbAutor = ctk.CTkComboBox(frDataRow2, state="readonly", **configEntryData)
        self.cbGenero = ctk.CTkComboBox(frDataRow1, state="readonly", **configEntryData)
        self.entryQuantCopias = ctk.CTkEntry(frDataRow2, width=40, **configEntryData)
        self.entryQuantDisponivel = ctk.CTkEntry(frDataRow2, width=40,**configEntryData)
        
        confButtonCad = {'fg_color': "#0077b6", 'hover_color': "#023e8a",
                         'text_color':"white", 'corner_radius': 0}
        
        self.btCadAutor = ctk.CTkButton(frDataRow2,text="+", width=30, command= self._openAutorGUI, **confButtonCad)
        self.btCadGenero = ctk.CTkButton(frDataRow1, text="+", width=30, **confButtonCad)
        
        self.entryQuantCopias.bind('<KeyRelease>', filterEstoqueEntry)
        self.entryQuantDisponivel.bind('<KeyRelease>', filterEstoqueEntry)
        
        btRegister = ctk.CTkButton(frButtons, text="Cadastrar", **confButtonCad)
        btCleanFields = ctk.CTkButton(frButtons, text="Limpar Campos", **confButtonCad,
            command= lambda : cleanFields(self.entryTitulo, self.cbAutor, self.cbGenero, self.entryQuantCopias,
                                          self.entryQuantDisponivel))

        self.frRegister.pack(fill='both', expand=True)
        ctk.CTkLabel(self.frRegister, text="Ficha de Cadastro", font=("", 18), text_color="black").pack(padx=5, pady=10, anchor='w')
        frLivroData.pack(pady=10, padx=5, fill='x')
        
        frDataRow1.pack(fill='x', padx=5, pady=(5,0))
        frDataRow2.pack(fill='x', padx=5, pady=(0,5))

        
        lbTitulo.pack(side="left", padx=5, pady=10)
        self.entryTitulo.pack(side="left", expand=True, fill='x', pady=10)
        lbGenero.pack(side="left", padx=5, pady=10)
        self.cbGenero.pack(side="left", fill='x', pady=10, padx=(0,5))
        self.btCadGenero.pack(side="left", pady=10, padx=(0,5))
        lbAutor.pack(side="left", padx=5, pady=10)
        self.cbAutor.pack(side="left", fill='x', expand=True, pady=10, padx=(0,5))
        self.btCadAutor.pack(side="left", pady=10, padx=(0,5))
        lbQuantCopias.pack(side="left", padx=(0,5), pady=10)
        self.entryQuantCopias.pack(side="left", fill='x', pady=10, padx=(0,5))
        lbQuantDisponivel.pack(side="left", padx=(0,5), pady=10)
        self.entryQuantDisponivel.pack(side="left",fill='x', pady=10, padx=(0,5))
        
        frButtons.pack(fill='x', padx=5, pady=10)
        btRegister.pack(side='right')
        btCleanFields.pack(side='right')
        
    def _loadSearchLivro(self):
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
        autorGUI = AutorGUI(self.root)
             
    def _cleanContentFrame(self):
        for w in self.frContent.winfo_children():
            w.destroy()