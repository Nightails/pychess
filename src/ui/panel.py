from textual.widgets import Static

class StatusPanel(Static):
    def __init__(self, turn: str):
        super().__init__()
        self.border_title = "Status"
        self.styles.border_title_align = "center"
        self.styles.border = ("round", "white")
        self.styles.content_align = ("center", "middle")
        self.update(turn)
