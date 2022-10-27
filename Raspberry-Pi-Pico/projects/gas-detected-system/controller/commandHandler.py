import sys
sys.path.append("../model")
import model.store

class CommandHandler:
    def __init__(self, allow_cmd_list=[]):
        self.cmd_queue = []
        self.allow_cmd_list = allow_cmd_list
    
    # 檢查命令是否在允許的名單中
    def checkCommandInAllowedList(self,cmd):
        for i in self.allow_cmd_list:
            if i in cmd:
                return True
        return False

    # 格式化從uart過來的命令
    def formatCommand(self,cmd):
        if len(cmd) == 0: return
        str = cmd.decode("utf-8")
        if ("vm" in str) and ("\r\n" in str):
            return str.split("<")[1].split("\r\n")[0]
        return "Not vaild command"
    
    # 將命令加入 queue 中
    def addCommandToQueue(self,cmd):
        self.cmd_queue.append(cmd)
    
    # 先進先出執行 queue 中的命令
    def executeCommandFromQueue(self):
        if len(self.cmd_queue) > 0:
            cmd = self.cmd_queue.pop(0)
            model.store.excuteCommand(cmd)
            message = "excuted: " + cmd
            print(message)
            
