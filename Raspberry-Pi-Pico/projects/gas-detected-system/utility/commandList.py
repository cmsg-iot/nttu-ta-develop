
def getSeperatedCommandList(cmd):
    cmd_list = separateCommandWithSpace(cmd)
    cmd_list = formatCommandList(cmd_list)
    return cmd_list

def separateCommandWithSpace(cmd):
    return cmd.split()

def formatCommandList(cmd_list):
    new_list = ["","","",None]
    for idx,v in enumerate(cmd_list):
        new_list[idx] = v
    return new_list