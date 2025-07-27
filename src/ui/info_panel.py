from textual.widgets import Static


class InfoPanel(Static):
    def __init__(self):
        super().__init__()
        self.border_title = "Info"
        self.styles.border = ("round", "white")
        self.styles.width = "1fr"

        self.update("Info about player and turn status go here")
