import time
from CommandInterface import CommandInterface


class ExitCommand(CommandInterface):
    def execute(self):
        print("Exiting ...")
        time.sleep(2)
        print("Goodbye :)")
        exit(0)