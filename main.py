from dicionario import *

def euclidean(rating1, rating2):
  distancia = 0
  for chave in rating1:
    if chave in rating2:
      distancia += (rating1[chave] - rating2[chave])**2
  return (distancia)**(1 / 2)

#acho que isso ta errado
def knn(userName, users):
  distancias = []
  for outro_usuario in users:
    if outro_usuario != userName:
      distancia = euclidean(users[outro_usuario], users[userName])
      if distancia:
        distancias.append((distancia, outro_usuario))
  distancias.sort()
  return distancias[:5] #mude o k aqui


def recommend(username, users):
  
    # first find nearest neighbor
    nearest = knn(username, users)[0][1] 

    recommendations = []
    # now find movies neighbor rated that user didn't know
    neighborRatings = users[nearest]
    userRatings = users[username]
    for item in neighborRatings:
        if not item in userRatings:
            recommendations.append((item, neighborRatings[item]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

#testando
print('\n')
print(knn("Almeida", users))

print('\n')
print(recommend('Almeida', users))