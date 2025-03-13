import customtkinter as ctk

class AlertWidget(ctk.CTkToplevel):
    def __init__(self, master: ctk.CTk, typeAlert: str, title: str, message: str):
        super().__init__(master)
        self.lift()
        self.attributes("-topmost", True)
        self._configureWindow(typeAlert)
        self.userResponse = False
        self._createWidgets(title, message)
        self._loadWidgets(typeAlert)
        self.grab_set()

    def _configureWindow(self, typeAlert: str):
        self.resizable(0,0)
        self.title(typeAlert)

    def _createWidgets(self, title: str, message: str):
        self.frMain = ctk.CTkFrame(self, fg_color='white', corner_radius=0, width=300)
        self.frOptions = ctk.CTkFrame(self.frMain, fg_color='transparent', corner_radius=0)
        
        configBtOption = {'font':("", 16), 'fg_color':'#0077b6', 'corner_radius':0, 'text_color':"white",
        'hover_color':"#023e8a"}
        configLabel = {'font':("", 16), 'text_color':"black"}
        
        self.lbTitle = ctk.CTkLabel(self.frMain, text=title, **configLabel)
        self.lbMessage = ctk.CTkLabel(self.frMain, text=message, **configLabel)
        self.btYes = ctk.CTkButton(self.frOptions, text="Sim", **configBtOption)
        self.btNo = ctk.CTkButton(self.frOptions, text="Não", **configBtOption)
        self.btOk = ctk.CTkButton(self.frOptions, text="Ok", command=lambda : self._closeAlert(False), **configBtOption)
        self.btCancel = ctk.CTkButton(self.frOptions, text="Cancelar", command=lambda: self._closeAlert(False), **configBtOption)

    def _loadWidgets(self, typeAlert: str):
        self.frMain.pack(fill="both", expand=True)
        self.lbTitle.pack(fill="x")
        self.lbMessage.pack(fill="x")
        self.frOptions.pack(fill="x")
        if typeAlert == "Error" or typeAlert == "Warning" or typeAlert == "Success":
            self.btOk.pack(side="left", anchor="center")
        else:
            self.btYes.pack(side="left", anchor="center")
            self.btNo.pack(side="left", anchor="center")
            self.btCancel.pack(side="left", anchor="center")

    def _closeAlert(self, response: bool):
        self.userResponse = response
        self.destroy()

   