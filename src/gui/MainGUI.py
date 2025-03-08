import customtkinter as ctk
from gui.ClienteWindow import ClienteWindow
from gui.LivroWindow import LivroWindow

class MainGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._configureWindow()
        self._createWidgets()
        self._loadWidgets()
        
        self.mainloop()
            
    def _configureWindow(self):
        self.geometry("1024x768")
        self.minsize(1024, 768)
        self.title("Sistema de Bibliotéca")
        
    def _createWidgets(self):
        self.frMain = ctk.CTkFrame(self, corner_radius=0)
        self.frMenu = ctk.CTkFrame(self.frMain, width=150, corner_radius=0, fg_color="#0077b6")
        self.frContent = ctk.CTkFrame(self.frMain, fg_color="white", corner_radius=0)
        configBtMenu = {'corner_radius':0, 'bg_color':'transparent', 'fg_color':'transparent',
                        'hover_color':"#023e8a", 'font':("",16), 'height':50}
        
        self.btDashBord = ctk.CTkButton(self.frMenu, text="Dashboard", **configBtMenu)
        self.btCliente = ctk.CTkButton(self.frMenu, text="Clientes", command=self._loadClienteWindow,**configBtMenu)
        self.btLivro = ctk.CTkButton(self.frMenu, text="Livros",command=self._loadLivroWindow, **configBtMenu)
        self.btRelatorio = ctk.CTkButton(self.frMenu, text="Relatório", **configBtMenu)
        self.btEmprestimo = ctk.CTkButton(self.frMenu, text="Emprestimos", **configBtMenu)
        self.btReserva = ctk.CTkButton(self.frMenu, text="Reservas", **configBtMenu)
        
        
    def _loadWidgets(self):
        self.frMain.pack(expand=True, fill='both')
        self.frMenu.pack(fill='y', side='left')
        self.frContent.pack(expand=True, fill='both', side='left')
        
        self.btDashBord.pack(fill='x', ipadx=10)
        self.btEmprestimo.pack(fill='x',ipadx=10)
        self.btReserva.pack(fill='x',ipadx=10)
        self.btCliente.pack(fill='x',ipadx=10)
        self.btLivro.pack(fill='x',ipadx=10)
        self.btRelatorio.pack(fill='x',ipadx=10)
        
    def _loadClienteWindow(self):
        for w in self.frContent.winfo_children():
            w.destroy()
            
        ClienteWindow(self.frContent, self).pack(fill="both", expand=True)
    
    def _loadLivroWindow(self):
        for w in self.frContent.winfo_children():
            w.destroy()
            
        LivroWindow(self.frContent, self).pack(fill="both", expand=True)