from sounder import Sounder
from validcommands import commands

#analize output of gtts
def analize(text):
    # valid command list

    commandset = commands.givecommands()
    sounder = Sounder(commandset)
    index = sounder.search(text.lower().split())
    command = " ".join(commandset[index])
    return command
