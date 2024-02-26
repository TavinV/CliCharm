import CliCharm


meu_programa = CliCharm.Program(name="Aplicativo Tavin", cmd_line="comando: ")



@CliCharm.command
def test(message, message2, messageKeyWord="none"):
    print(message)
    print(messageKeyWord)
    print(message2)

meu_programa.mainLoop()