# Dada una lista con preguntas que se responden por ’si’ o ’no y sus respuestas correctas, armar
# un juego que muestre cada una de las preguntas al jugador, verifique si es correcta o no e
# incremente el puntaje en caso de acertar. Se debe seleccionar en forma aleatoria la pregunta
# a mostrar y eliminarla una vez que ya la mostraron. El juego finaliza cuando no hay más
# perguntas en la lista. Un ejemplo de la lista con las preguntas podría ser:

from random import choice,shuffle

score=0
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], [' Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]

for item in range(len(preguntas)):
    target = choice(preguntas)
    preguntas.remove(target)
    print('='*30)
    print(target[0])
    print('='*30+'\n')
    answer = input().lower()
    if( answer == target[1]):
        score+=1
print("su puntuacion es de : {} \n".format(score))