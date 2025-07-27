from textual.widgets import Input


class CMDInput(Input):
    def __init__(self):
        super().__init__()
        self.border_title = "Command"
        self.styles.border = ("round", "white")
