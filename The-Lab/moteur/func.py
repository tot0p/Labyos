#Thomas Lemaitre
#Pour le Changement de la lang

def whatislang(path):
    '''
    détermine la lang actuellement utilisé
    '''
    t = path.split('/')
    if "english" in t:
        return "english"
    elif "francais" in t:
        return "francais"