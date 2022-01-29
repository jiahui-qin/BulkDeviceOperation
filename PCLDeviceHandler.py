import os
from pickle import TRUE

class PclStartUpCheck:
    startUp = ""
    nextUp = ""
    model = ""
    subModel = ""
    curVersion = ""
    deleteFile = "null"
    newFile = ""


    def __init__(self, telnetString):
        lines = telnetString.splitlines()
        for line in lines:
            if line.startswith("Startup"):
                strings = line.split(':')
                startUp = strings[-1].strip()
                self.startUp = startUp
                models = startUp.split('_')
                self.model = models[1]
                self.subModel = models[2] + "_" + models[3]
                self.curVersion = models[0]
            if line.startswith("Next"):
                strings = line.split(':')
                nextUp = strings[-1].strip()
                self.nextUp = nextUp


    def print(self):
        print("cur device model is " + self.model + "_" + self.subModel + " with version: " + self.curVersion)

    def getDeleteFile(self, fileList):
        for file in fileList:
            filename = file.strip()
            if filename.endswith(".cc"):
                if filename != self.startUp:
                    self.deleteFile = "/mnt/flash2/" + filename

    def getUploadFilePath(self, localPath):
        ## localPath points to the address of the local file to be matched
        localFiles = []
        with os.scandir(localPath) as entries:
            for entry in entries:
                if entry.is_file():
                    localFiles.append(entry.name)
        for localFile in localFiles:
            if localFile.endswith('cc'):
                if compareVersion(localFile, self.startUp):
                    self.newFile = localPath + '/' + localFile

def compareVersion(file1, file2):
    model1 = file1.split('_')
    model2 = file2.split('_')
    ##if model1[1] == model2[1] and model1[2] == model2[2] and model1[3] == model2[3]:
    if model1[1] == model2[1]:
        return TRUE
    return False
