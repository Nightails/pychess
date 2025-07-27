from textual.widgets import Static


class LogPanel(Static):
    def __init__(self):
        super().__init__()
        self.border_title = "Log"
        self.styles.border = ("round", "white")
        self.styles.width = "1fr"

        self.update("Previous moves go here")
