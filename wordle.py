from functools import partial
from statistics import mode
import random


def choose_secret(filename):
    """Dado un nombre de fichero, esta funciÃ³n devuelve una palabra aleatoria de este fichero transformada a mayÃºsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayÃºsculas. Ej. "CREMA"
    """
    fichero=open(filename,mode="rt",encoding="utf-8")
    if fichero.readline()!="":
        lista=fichero.readlines()
        linea=random.choice(lista)
        palabraSecreta=lista[linea]
        palabraSecreta=palabraSecreta.upper()
        return palabraSecreta
    else:
        raise ValueError("el fichero no tiene palabras")

    
def compare_words(word, secret):
    """Dadas dos palabras en mayÃºsculas (word y secret), esta funciÃ³n calcula las posiciones de las letras de word que aparecen en la misma posiciÃ³n en secret, y las posiciones de las letras de word que aparecen en secret pero en una posiciÃ³n distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posiciÃ³n en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras estÃ¡n en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    word=word.upper()
    same_letter=[]
    same_position=[]

    if(word.len()==secret.len()):
        for i in secret:
            if word[i] == secret[i]:
                same_position.append(i)
    
        for j in word:
            for k in secret:
                if word[j] == secret[k]:
                    same_letter.append[j]
        return same_position,same_letter
    else:
        raise  ValueError("la longitud de las palabras recibidas no es la misma")



def print_word(word,same_letter_position,same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta funciÃ³n crearÃ¡ un string donde aparezcan en mayÃºsculas las letras de la palabra que ocupen las posiciones de same_position, en minÃºsculas las letras de la palabra que ocupen las posiciones de same_letter y un guiÃ³n (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    palabra="-----"

    for i in same_letter_position:
        if(same_letter_position[i]<6 and same_letter_position[i]>=0):
            palabra[same_letter_position[i]]=word[same_letter_position[i]]
        else:
            raise ValueError("contiene valor negativo o mayor de la longitud de la palabra")
        
    for j in same_letter:
        if(same_letter[j]<6 and same_letter[j]>=0):
            palabra[same_letter[j]]=word[same_letter[j]].lower()
        else:
            raise ValueError("contiene valor negativo o mayor de la longitud de la palabra")
    transformed= palabra
    return transformed
        

    
def choose_secret_advanced():
    """Dado un nombre de fichero, esta funciÃ³n filtra solo las palabras de 5 letras que no tienen acentos (Ã¡,Ã©,Ã­,Ã³,Ãº). De estas palabras, la funciÃ³n devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayÃºsculas
    """
 
def check_valid_word(selected):
    """Dada una lista de palabras, esta funciÃ³n pregunta al usuario que introduzca una palabra hasta que introduzca una que estÃ© en la lista. Esta palabra es la que devolverÃ¡ la funciÃ³n.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que estÃ¡ en la lista.
    """
    i=0
    palabra=None
    while i!=1:
        palabra=input("introduzca una palabra que este en la lista porfavor:")
        palabraMayus=palabra.upper()
        for j in selected:
            if palabraMayus==selected[j].upper():
                    i=1
    return palabra



if __name__ == "__main__":
    try:
        secret=choose_secret()
    except ValueError:
        print("fichero sin palabras")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        try:
            same_position, same_letter = compare_words()
        except ValueError:
            print("la longitud de las palabras no es la  misma")
        try:
            resultado=print_word()
        except ValueError:
            print("contiene valor negativo o mayor de la longitud de la palabra")
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   