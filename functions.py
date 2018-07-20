def IsInFile(file, finder):
    try:
        checkFile = open(file, "r")
        if checkFile.read().find(finder):
            return True
        else:
            return False
    except:
        return False
