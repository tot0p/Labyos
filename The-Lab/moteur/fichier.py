import os

#lib de 2019 coder par thomas

class Fichier:
    '''
    permet de toucher au fichier
    '''

    def __init__(self,fileName,encodage='utf8'):
        self.fName = fileName
        self.encodage = encodage

    # lecture

    def lecture(self):
        '''
        lis le fichier et return sont contenu
        '''
        f = open(self.fName,'r',encoding=self.encodage)
        contenu = f.readlines()
        f.close()
        contenuFinal = ''
        for i in range(len(contenu)):
            contenuFinal = contenuFinal + str(contenu[i])
        return contenuFinal

    def lectureTable(self):
        '''
        return un list des ligne du fichier
        '''
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
        et ecrit dans le fichier
        '''
        f = open(self.fName,'w',encoding=self.encodage)
        f.write(contenu)
        f.close()

    def writeTable(self,contenu:list):
        '''
        contenu = array
        et ecrit dans le fichier avec chaque element de la list correspondant a une ligne
        '''
        f = open(self.fName,'w',encoding=self.encodage)
        for i in range(len(contenu)):
            if i != len(contenu)-1:
                contenu[i] = contenu[i] + '\n'
            f.writelines(contenu[i])
        f.close()

    def writeFollowing(self,contenu:str):
        """
        ecrit a la suite d'un fichier
        """
        f = open(self.fName,'a',encoding=self.encodage)
        f.write(contenu)
        f.close()

    def writeFollowingTable(self,contenu):
        """
        ecrit a la suite d'un fichier de type table
        """
        f = open(self.fName,'a',encoding=self.encodage)
        for i in range(len(contenu)):
            contenu[i] = '\n' + contenu[i]
            f.writelines(contenu[i])
        f.close()

    # clear

    def clear(self):
        '''
        efface le contenue du fichier
        '''
        f = open(self.fName,'w',encoding=self.encodage)
        f.write('')
        f.close()

    # file

    def changeFile(self,NewName):
        '''
        permet de changer de fichier
        NewName str le nom du fichier a ouvrir
        '''
        self.fName = NewName

    def createFile(self,contenu:str=''):
        '''
        permet de créer un fichier avec comme contenu contenu :str
        '''
        f = open(self.fName,'a',encoding=self.encodage)
        f.write(contenu)
        f.close()

    def duplicateFile(self,nameFile2:str):
        """
        permet de duplicer un fichier le fichier copie a comme nom nameFile2 : str
        """
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
        """
        permet de changer de place le fichier avec comme chemin nameFile2 : str
        """
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
        '''
        permet de supprimer un fichier
        '''
        os.remove(self.fName)

    def existFile(self):
        '''
        permet de vérifier l'existance d'un fichier 
        return True si il exist et False sinon
        '''
        try:
            f = open(self.fName,'r',encoding=self.encodage)
            f.close()
            return True
        except:
            return False

    #variableFile

    def variableFileLecture(self):
        '''
        return un dict des variables du fichiers
        avec les ligne sous forme de (key=salut)
        '''
        contenu = self.lectureTable()
        nbVariable = len(contenu)
        contenuFinal = {}
        for i in range(nbVariable):
            contenu[i] = contenu[i].split("=")
            contenuFinal[contenu[i][0]] = contenu[i][1]
        return contenuFinal

    def variableFileWrite(self,contenu:dict):
        '''
        permet d'ecrire le dictionnaire de variable dans un fichier
        '''
        contenuFinal =[]
        print(list(contenu.keys()))
        for i in list(contenu.keys()):
            contenuFinal.append( str(i) + '=' + str(contenu[i]))
        print(contenuFinal)
        self.writeTable(contenuFinal)
