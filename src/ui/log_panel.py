from textual.widgets import Static


class LogPanel(Static):
    contents = ["Previous moves go here"]

    def __init__(self):
        super().__init__()
        self.border_title = "Log"
        self.styles.border = ("round", "white")
        self.styles.width = "1fr"

        self.update(self.contents[0])

    def update_log(self, content):
        self.contents.append(content)
        self.update("\n".join(self.contents))
