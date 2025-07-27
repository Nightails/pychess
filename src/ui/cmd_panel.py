from textual.widgets import Input


class CMDPanel(Input):
    def __init__(self):
        super().__init__()
        self.border_title = "Command"
        self.styles.border = ("round", "white")
        self.styles.background = "black"

        self.placeholder = "Type move here"
