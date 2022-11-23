def getFileListOfPath(rootPath,listdir):
    file_list = []
    for i in listdir:
        file_list.append(rootPath + "/" + i)
    return file_list