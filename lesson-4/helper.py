class Helpers():
    def check_empty(checkVar):
        if checkVar == None:
            return False
        if checkVar == False:
            return False
        if checkVar == '':
            return False
        if len(checkVar) == 0:
            return False
