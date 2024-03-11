import os

Error_messages = {
    "Command not found" : "The given command was not found. Use --Commands to show all commands available."
}

commands = {}

class Program:
    """
    Main class in Cli Charm
    """
    def __init__(self, name, cmd_line, brk_cmd = "_k", start_msg = "Welcome") -> None:
        self.name = name,
        self.cmd_line = cmd_line
        self.start_msg = start_msg
        self.commands = {}
        
    def mainLoop(self):
        print(self.start_msg)
        print(commands)
        while True:
            command_given = input(self.cmd_line).lower()
            
            if command_given == "__k":
                os.system("cls")
                break
                

            try:
                found_command = commands[command_given]
            except KeyError:
                print(Error_messages["Command not found"])


def command(func):
    
    def formated_command_function(name,*args):
        print("Wrapped")
        func(args)
        print("Finished")
    
    commands[func.__name__.lower()] = formated_command_function
    return formated_command_function
        
        