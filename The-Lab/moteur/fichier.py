import os

class Fichier:
    '''
    permet de toucher o fichier
    '''
    fName=''
    encodage=''

    def __init__(self,fileName,encodage='utf8'):
        self.fName = fileName
        self.encodage = encodage

    # lecture

    def lecture(self):
        f = open(self.fName,'r',encoding=self.encodage)
        contenu = f.readlines()
        f.close()
        contenuFinal = ''
        for i in range(len(contenu)):
            contenuFinal = contenuFinal + str(contenu[i])
        return contenuFinal

    def lectureTable(self):
        f = open(self.fName,'r',encoding=self.encodage)
        contenu = f.readlines()
        f.close()
        contenuFinal = []
        for i in range(len(contenu)):
            contenuFinal.append(contenu[i].rstrip('\n'))

        return contenuFinal

    #write

    def write(self,contenu:str):
        '''
        contenu = str
        '''
        f = open(self.fName,'w',encoding=self.encodage)
        f.write(contenu)
        f.close()

    def writeTable(self,contenu:list):
        '''
        contenu = array
        '''
        f = open(self.fName,'w',encoding=self.encodage)
        for i in range(len(contenu)):
            if i != len(contenu)-1:
                contenu[i] = contenu[i] + '\n'
            f.writelines(contenu[i])
        f.close()

    def writeFollowing(self,contenu:str):
        f = open(self.fName,'a',encoding=self.encodage)
        f.write(contenu)
        f.close()

    def writeFollowingTable(self,contenu):
        f = open(self.fName,'a',encoding=self.encodage)
        for i in range(len(contenu)):
            contenu[i] = '\n' + contenu[i]
            f.writelines(contenu[i])
        f.close()

    # clear

    def clear(self):
        f = open(self.fName,'w',encoding=self.encodage)
        f.write('')
        f.close()

    # file

    def changeFile(self,NewName):
        self.fName = NewName

    def createFile(self,contenu:str=''):
        f = open(self.fName,'a',encoding=self.encodage)
        f.write(contenu)
        f.close()

    def duplicateFile(self,nameFile2:str):
        f = open(self.fName,'r',encoding=self.encodage)
        contenu = f.readlines()
        f.close()
        contenuFinal = ''
        for i in range(len(contenu)):
            contenuFinal = contenuFinal + str(contenu[i])
        f = open(nameFile2,'a',encoding=self.encodage)
        f.write(contenuFinal)
        f.close()

    def moveFile(self,nameFile2:str):
        f = open(self.fName,'r',encoding=self.encodage)
        contenu = f.readlines()
        f.close()
        contenuFinal = ''
        for i in range(len(contenu)):
            contenuFinal = contenuFinal + str(contenu[i])
        f = open(nameFile2,'a',encoding=self.encodage)
        f.write(contenuFinal)
        f.close()
        os.remove(self.fName)
        self.fName = nameFile2

    def removeFile(self):
        os.remove(self.fName)

    def existFile(self):
        try:
            f = open(self.fName,'r',encoding=self.encodage)
            f.close()
            return True
        except:
            return False

    #variableFile

    def variableFileLecture(self):
        contenu = self.lectureTable()
        nbVariable = len(contenu)
        contenuFinal = {}
        for i in range(nbVariable):
            contenu[i] = contenu[i].split("=")
            contenuFinal[contenu[i][0]] = contenu[i][1]
        return contenuFinal

    def variableFileWrite(self,contenu:dict):
        contenuFinal =[]
        print(list(contenu.keys()))
        for i in list(contenu.keys()):
            contenuFinal.append( str(i) + '=' + str(contenu[i]))
        print(contenuFinal)
        self.writeTable(contenuFinal)
