from commands import Command

class RemoteControl:
    def __init__(self):
        self.commands: list(Command) = []

    def press_button(self, command: Command):
        command.execute()
        self.commands.append(command)

    def undo_last(self):
        if self.commands:
            command: Command = self.commands.pop()
            command.undo()