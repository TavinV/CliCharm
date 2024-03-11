import CliCharm


meu_programa = CliCharm.Program(name="Aplicativo Tavin", cmd_line="comando: ")



@CliCharm.command
def test(message):
    print(message)


meu_programa.mainLoop()