def parImpar(num):
    if(num%2==0): #é par
        return True
    else:        #é impar
        return False


def numeroPositivo(num):
    if(num>=0):
        return True
    else:
        return False


def primo(num):
    numIsPrimo=True

    for i in range(2, num):
        if(num % i == 0):
            numIsPrimo = False

        if numIsPrimo:
            return True
        else:
            return False


def numPerfeito(num):

    for i in range(1, num):
        if num % i == 0:
            return True
        else:
            return False


def numTriagular(num):
    triangular = True

    for i in range(1, num):
    if num