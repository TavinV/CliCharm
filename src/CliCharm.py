class ErrorMessagesClass:
    def __init__(self, cmd_not_found, cmds_args_missing, divison_by_zero, type_error) -> None:
        self.cmd_not_found = cmd_not_found
        self.cmds_args_missing = cmds_args_missing
        self.divison_by_zero = divison_by_zero
        self.type_error = type_error
        

ErrorMessages = ErrorMessagesClass(cmd_not_found="Comando não encontrado!",cmds_args_missing="Comando está sem 1 ou mais argumentos!", divison_by_zero= "Não posso dividir por zero", type_error="O tipo de arg está incorreto!")

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
        
        while True:
            command_given = input(self.cmd_line).lower()
            
            try:
                found_command = self.commands[command_given]
            except KeyError:
                print(ErrorMessages.cmd_not_found)

def command(func, name):
    
    def wrapper(*args, **kwargs):
        print("Start")
        
        func(*args,**kwargs)
        
        print("Finish")
        
    return wrapper