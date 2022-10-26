import sys
sys.path.append("../model")
import model.store

class CommandHandler:
    def __init__(self, allow_cmd_list=[]):
        self.cmd_queue = []
        self.allow_cmd_list = allow_cmd_list
    
    # 檢查命令是否在名單中
    def checkCommand(self,cmd):
        for i in self.allow_cmd_list:
            if i in cmd:
                return True
        return False

    # 格式化從uart過來的指令
    def formatCommand(self,cmd):
        if len(cmd) == 0: return
        str = cmd.decode("utf-8")
        if ("vm" in str) and ("\r\n" in str):
            return str.split("<")[1].split("\r\n")[0]
    
    # 將允許的指令加入 queue 中
    def addAllowedCommand(self,cmd):
        c = self.formatCommand(cmd)
        if c != None and self.checkCommand(c):
            self.cmd_queue.append(c)
    
    # 先進先出執行 queue 中的命令
    def executeCommandFromQueue(self):
        if len(self.cmd_queue) > 0:
            cmd = self.cmd_queue.pop(0)
            message = "excuted: " + cmd
            print(message)
            model.store.setMessage(message)
