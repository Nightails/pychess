from textual.widgets import Static, Input


class StatusPanel(Static):
    def __init__(self, turn: str):
        super().__init__()
        self.border_title = "Status"
        self.styles.border_title_align = "center"
        self.styles.border = ("round", "white")
        self.styles.content_align = ("center", "middle")
        self.update(turn)


class InfoPanel(Static):
    def __init__(self):
        super().__init__()
        self.border_title = "Info"
        self.styles.border = ("round", "white")
        self.styles.width = "1fr"

        self.update("Info about player and turn status go here")


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


class CMDPanel(Input):
    def __init__(self):
        super().__init__()
        self.border_title = "Command"
        self.styles.border = ("round", "white")
        self.styles.background = "black"

        self.placeholder = "Type move here"
