import customtkinter as ctk
from functools import reduce

class ClienteWindow(ctk.CTkFrame):
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
        
        self.lbTitle = ctk.CTkLabel(self.frMain, text="Gerenciamento de Clientes", font=("", 25), text_color="black")
        
        self.btList = ctk.CTkButton(self.frMenu, text="Listar", command=self._loadListClientes, **configBtMenu)
        self.btSearch = ctk.CTkButton(self.frMenu, text="Pesquisar", command=self._loadSearchCliente, **configBtMenu)
        self.btRegister = ctk.CTkButton(self.frMenu, text="Cadastrar", command=self._loadRegisterCliente, **configBtMenu)
        self.btEdit = ctk.CTkButton(self.frMenu, text="Editar", command=self._loadEditCliente, **configBtMenu)
            
    def _loadWidgets(self):
        self.frMain.pack(fill="both", expand=True)
        self.lbTitle.pack(fill="x")
        self.frMenu.pack(fill="x")
        
        self.btList.pack(side='left', padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btSearch.pack(side='left', padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btRegister.pack(side="left", padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        self.btEdit.pack(side="left", padx=0, ipady=5, ipadx=5, fill='x', expand=True)
        
        self.frContent.pack(fill='both', expand=True)
        self._loadListClientes()
        
    def _registerNewCliente(self):
        cpf = self.entryCpf.get()
        cpf = reduce(lambda f,l: f+l if not(f in ".-" or l in ".-") else f, cpf)
        
        telefone = self.entryTelefone.get()
        telefone = reduce(lambda f,l: f+l if not(f in "() -" or l in "() -") else "" if f == "(" else f, telefone)
        print(cpf)
        print(telefone)
    
    def _loadListClientes(self):
        self._cleanContentFrame()
        
        self.frTableClientes = ctk.CTkFrame(self.frContent, fg_color="#ced4da", corner_radius=0)
        
        self.frTableClientes.grid_columnconfigure(0, weight=1)
        self.frTableClientes.grid_columnconfigure(1, weight=10)
        self.frTableClientes.grid_columnconfigure(2, weight=4)
        self.frTableClientes.grid_columnconfigure(3, weight=4)
        self.frTableClientes.grid_columnconfigure(4, weight=5)
        
        lbId = ctk.CTkLabel(self.frTableClientes, text="ID", text_color="black")
        lbNome = ctk.CTkLabel(self.frTableClientes, text="NOME", text_color="black")
        lbCpf = ctk.CTkLabel(self.frTableClientes, text="CPF", text_color="black")
        lbTelefone = ctk.CTkLabel(self.frTableClientes, text="TELEFÔNE", text_color="black")
        lbEmail = ctk.CTkLabel(self.frTableClientes, text="EMAIL", text_color="black")
        
        self.frTableClientes.pack(fill="both", expand=True, ipadx=10, ipady=10)
        lbId.grid(row=0, column=0)
        lbNome.grid(row=0, column=1)
        lbCpf.grid(row=0, column=2)
        lbTelefone.grid(row=0, column=3)
        lbEmail.grid(row=0, column=4)
    
    def _loadRegisterCliente(self):
        def cleanFields(*fields):
            for f in fields:
                f.delete(0, 'end')
            
        def filterCpfEntry(event):
            vk = event.keysym
            w = event.widget
            if vk != "BackSpace":
                try:
                    c = vbCPF.get()[-1]
                    try:
                        c = int(c)
                        l = len(w.get())
                        if l < 15:
                            if l in (3,7,11):
                                if l in (3,7):
                                    w.insert(l+1, ".")
                                else:
                                    w.insert(l+1,"-")
                        else: 
                            w.delete(len(w.get())-1, 'end')
                    except ValueError:
                        w.delete(len(w.get())-1, 'end')
                except IndexError:
                    pass
            
        def filterTelefoneEntry(event):
            vk = event.keysym
            w = event.widget
            if vk != "BackSpace":
                try:
                    #O comando de delete acaba executando quando qualquer tecla, diferente de backspace, é pressionada
                    #É preciso corrigir o bug
                    c = vbTelefone.get()[-1] 
                    try:
                        c = int(c)
                        l = len(w.get())
                        if l < 16:
                            if l in (1,3,5,10):
                                if l == 1:
                                    w.insert(l-1, "(")
                                elif l == 3:
                                    w.insert(l+1, ")")
                                elif l == 5:
                                    w.insert(l+1, " ")
                                elif l == 10:
                                    w.insert(l+1, "-")
                        else: 
                            w.delete(len(w.get())-1, 'end')
                    except ValueError:
                        w.delete(len(w.get())-1, 'end')
                except IndexError:
                    pass
        
        def filterNumeroAddress(event):
            vk = event.keysym
            w = event.widget
            
            if vk != "BackSpace":
                try:
                    c = vbNumero.get()[-1]
                    try:
                        c = int(c)
                    except ValueError:
                        w.delete(len(w.get())-1, 'end')
                except IndexError:
                    pass
        
        def filterCepEntry(event):
            vk = event.keysym
            w = event.widget
            if vk != "BackSpace":
                try:
                    c = vbCEP.get()[-1]
                    try:
                        c = int(c)
                        l = len(w.get())
                        if l < 10:
                            if l == 5:
                                w.insert(l+1,"-")
                        else: 
                            w.delete(len(w.get())-1, 'end')
                    except ValueError:
                        w.delete(len(w.get())-1, 'end')
                except IndexError:
                    pass
        
        self._cleanContentFrame()
        self.frRegister = ctk.CTkFrame(self.frContent, fg_color='transparent')
        frClienteData = ctk.CTkFrame(self.frRegister, fg_color='transparent', border_color='black', border_width=1)

        frDataRow1 = ctk.CTkFrame(frClienteData, fg_color='transparent')
        frDataRow2 = ctk.CTkFrame(frClienteData, fg_color='transparent')
        
        frClienteAddress = ctk.CTkFrame(self.frRegister, fg_color='transparent', border_color='black', border_width=1)
        
        frAddressRow1 = ctk.CTkFrame(frClienteAddress, fg_color='transparent')
        frAddressRow2 = ctk.CTkFrame(frClienteAddress, fg_color='transparent')
        
        frButtons = ctk.CTkFrame(self.frRegister, fg_color='transparent')
        
        configLabelData = {'text_color':'black', 'font':("", 15)}
        configEntryData = {'corner_radius':0, 'border_color':"grey", 'fg_color':'#ced4da', 'text_color':'black'}
        
        vbCEP = ctk.StringVar()
        vbNumero = ctk.StringVar()
        vbCPF = ctk.StringVar()
        vbTelefone = ctk.StringVar()
        
        lbNome = ctk.CTkLabel(frDataRow1, text="Nome: ", **configLabelData)
        lbCpf = ctk.CTkLabel(frDataRow1,text="CPF: ", **configLabelData)
        lbTelefone = ctk.CTkLabel(frDataRow2, text="Telefône: ", **configLabelData)
        lbEmail = ctk.CTkLabel(frDataRow2, text="Email: ", **configLabelData)
        lbLogradouro = ctk.CTkLabel(frAddressRow1, text="Logradouro: ", **configLabelData)
        lbBairro = ctk.CTkLabel(frAddressRow1, text="Bairro: ", **configLabelData)
        lbNumero = ctk.CTkLabel(frAddressRow1, text="Numero: ", **configLabelData)
        lbCidade = ctk.CTkLabel(frAddressRow2, text="Cidade: ", **configLabelData)
        lbEstado = ctk.CTkLabel(frAddressRow2, text="Estado: ", **configLabelData)
        lbCEP = ctk.CTkLabel(frAddressRow2, text="CEP: ", **configLabelData)
        
        
        self.entryNome = ctk.CTkEntry(frDataRow1, **configEntryData)
        self.entryCpf = ctk.CTkEntry(frDataRow1, textvariable=vbCPF,**configEntryData)
        self.entryTelefone = ctk.CTkEntry(frDataRow2,textvariable=vbTelefone, **configEntryData)
        self.entryEmail = ctk.CTkEntry(frDataRow2, **configEntryData)
        self.entryLogradouro = ctk.CTkEntry(frAddressRow1,**configEntryData)
        self.entryBairro = ctk.CTkEntry(frAddressRow1, **configEntryData)
        self.entryNumero = ctk.CTkEntry(frAddressRow1,width=40,textvariable=vbNumero, **configEntryData)
        self.entryCidade = ctk.CTkEntry(frAddressRow2, **configEntryData)
        self.entryEstado = ctk.CTkEntry(frAddressRow2,width=50, **configEntryData)
        self.entryCEP = ctk.CTkEntry(frAddressRow2, width=100,textvariable=vbCEP, **configEntryData)
        
        self.entryCpf.bind('<KeyRelease>', filterCpfEntry)
        self.entryTelefone.bind('<KeyRelease>', filterTelefoneEntry)
        self.entryNumero.bind('<KeyRelease>', filterNumeroAddress)
        self.entryCEP.bind('<KeyRelease>', filterCepEntry)
        
        btRegister = ctk.CTkButton(frButtons, text="Cadastrar", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
                                 corner_radius=0, command=self._registerNewCliente)
        btCleanFields = ctk.CTkButton(frButtons, text="Limpar Campos", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
            corner_radius=0, command= lambda : cleanFields(self.entryNome, self.entryCpf, self.entryTelefone,
                                                           self.entryEmail, self.entryLogradouro, self.entryBairro,
                                                           self.entryNumero, self.entryCidade, self.entryEstado,
                                                           self.entryCEP))

        self.frRegister.pack(fill='both', expand=True)
        ctk.CTkLabel(self.frRegister, text="Ficha de Cadastro", font=("", 18), text_color="black").pack(padx=5, pady=10, anchor='w')
        frClienteData.pack(pady=10, padx=5, fill='x')
        frClienteAddress.pack(pady=(0,10), padx=5, fill='x')
        
        frDataRow1.pack(fill='x', padx=5, pady=(5,0))
        frDataRow2.pack(fill='x', padx=5, pady=(0,5))
        frAddressRow1.pack(fill='x', padx=5, pady=(5,0))
        frAddressRow2.pack(fill='x', padx=5, pady=(0,5))
        
        lbNome.pack(side="left", padx=(10,5), pady=10)
        self.entryNome.pack(side="left", expand=True, fill='x', pady=10)
        lbCpf.pack(side="left", padx=5, pady=10)
        self.entryCpf.pack(side="left", fill='x', pady=10, padx=(0,10))
        lbTelefone.pack(side="left", padx=(10,5), pady=10)
        self.entryTelefone.pack(side="left", fill='x', pady=10)
        lbEmail.pack(side="left", padx=5, pady=10)
        self.entryEmail.pack(side="left", expand=True, fill='x', pady=10, padx=(0,10))
        
        lbLogradouro.pack(side="left", padx=(10,5), pady=10)
        self.entryLogradouro.pack(side="left", expand=True, fill='x', pady=10)
        lbBairro.pack(side="left", padx=5, pady=10)
        self.entryBairro.pack(side="left", fill='x', pady=10)
        lbNumero.pack(side="left", padx=5, pady=10)
        self.entryNumero.pack(side="left", padx=(0,10), pady=10)
        lbCidade.pack(side="left", padx=5, pady=10)
        self.entryCidade.pack(side="left", expand=True, fill='x', pady=10)
        lbEstado.pack(side="left", padx=5, pady=10)
        self.entryEstado.pack_propagate(0)
        self.entryEstado.pack(side="left", pady=10)
        lbCEP.pack(side="left", padx=5, pady=10)
        self.entryCEP.pack(side="left", fill='x', pady=10, padx=(0,10))
        
        frButtons.pack(fill='x', padx=5, pady=10)
        btRegister.pack(side='right')
        btCleanFields.pack(side='right')
        
    def _loadSearchCliente(self):
        self._cleanContentFrame()
        frSearch = ctk.CTkFrame(self.frContent, fg_color="transparent")
        frClienteData = ctk.CTkFrame(self.frContent, fg_color='transparent')
        
        entryID = ctk.CTkEntry(frSearch, placeholder_text="ID do cliente", corner_radius=0, border_color="grey", fg_color='#ced4da')
        btSearch = ctk.CTkButton(frSearch, text="Buscar", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
                                 corner_radius=0)

        frSearch.pack(fill='x', ipadx=10, ipady=10)
        frClienteData.pack(fill='both', expand=True, ipadx=10, ipady=10)
        entryID.pack(side='left', padx=10)
        btSearch.pack(side="left")
    
    def _loadEditCliente(self):
        self._cleanContentFrame()
        frSearch = ctk.CTkFrame(self.frContent, fg_color="transparent")
        frClienteData = ctk.CTkFrame(self.frContent, fg_color='transparent')
        
        entryID = ctk.CTkEntry(frSearch, placeholder_text="ID do cliente", corner_radius=0, border_color="grey", fg_color='#ced4da')
        btSearch = ctk.CTkButton(frSearch, text="Buscar", fg_color="#0077b6",hover_color="#023e8a", text_color="white",
                                 corner_radius=0)

        frSearch.pack(fill='x', ipadx=10, ipady=10)
        frClienteData.pack(fill='both', expand=True, ipadx=10, ipady=10)
        entryID.pack(side='left', padx=10)
        btSearch.pack(side="left")
     
    def _cleanContentFrame(self):
        for w in self.frContent.winfo_children():
            w.destroy()
        