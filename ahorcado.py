import unicodedata
import random
import os 

# Quita las tildes de las palabras pasadas como parametro
def normalize(word):

    normalized=unicodedata.normalize("NFD",word)
    normalized = "".join([c for c in normalized if not unicodedata.combining(c)])
    return normalized.replace("\n","")

# Comprueba que la longitud del parametro introducido sea 1 y que sea una letra
def chr_check(chr):

        if len(chr) == 1 and chr.isalpha()==True:
            return True
        else:
            return False

# Sistema de puntuación

def run():

    #Guardamos las palabras del txt en la variable words
    words=[]
    with open("./data.txt","r",encoding="utf-8") as f:
        for line in f:
            words.append(normalize(line))

    # Seleccionamos una palabra random de la lista    
    rand_word=list(words[random.randint(0,len(words))])        
    # Número de caracteres de la palabra
    len_word=len(rand_word)
    hang_word=list("_"*len_word)
    show_word=[" __ "]*len_word
    
    lives=len_word*2

    # No se saldra del bucle hasta que rand_word no sea igual a hang_word y si lives es superior a 0
    while rand_word!=hang_word and lives>0:

        # Limpia la pantalla
        os.system("cls")

        # Creamos una variable llamada show_word con la que mostraremos en mayusculas los caracteres de la palabra conforme estas se vayan acertando
        for i,c in enumerate(hang_word):
            if c.isalpha()==True:
                show_word[i]=" "+c+" "        

        # Juntamos la lista y lo ponemos en mayusculas
        print("".join(show_word).upper())    
        print("Tienes "+ str(lives) +" vidas.")

        # Pedimos el caracter
        chr=input()
        # Excepcción en caso de que el valor introducido sea erroneo
        try: 
            if(chr_check(chr)==False):
                raise ValueError("Solo puedes introducir una letra.")
        except ValueError as ve:
            print(ve)
            return False

        # Iteración que guarda en i el indice y en c el caracter de los dos valores que devuelve la función enumerate
        for i,c in enumerate(rand_word) :
            if c == chr:
                #Si el caracter introducido coincide con la letra o letras de la palabra, se remplazara "_" usando i como indice de la lista
                hang_word[i]=c
                found_c=True
            else: 
                found_c=False

        # Comprobar si el caracter introducido ya ha sido encontrado
        for r in hang_word:
            if r==chr:
                found_r=True
            else: 
                found_c=False

        # Si no encuentra caracter que coincida con alguna de las letras de la palabra o el caracter ya se haya encontrado te resta 1 vida
        if found_c!=True or found_r==True:
            lives=lives-1

    os.system("cls")
    if lives==0:        
        print("Te has muerto por noob, la palabra es : "+"".join(rand_word).upper())
    else:
        print("Ganaste, la palabra es : "+"".join(rand_word).upper())

if __name__ == '__main__':
    run()