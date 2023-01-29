from dicionario import *

def euclidean(rating1, rating2):
  distancia = 0
  for chave in rating1:
    if chave in rating2:
      distancia += (rating1[chave] - rating2[chave])**2
  return (distancia)**(1 / 2)
  
#testando
print(euclidean(users["Renato"], users["Sara"]))
print(euclidean(users["Renato"], users["Mateus"]))
print(euclidean(users["Renato"], users["Fabiana"]))



def KNN(userName, users):
  distancias = []
  for outro_usuario in users:
    if outro_usuario != userName:
      distancia = euclidean(users[outro_usuario], users[userName])
      distancias.append((distancia, outro_usuario))
  distancias.sort()
  return distancias

#testando
print('\n')
print(KNN("Renato", users))
