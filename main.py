from dicionario import users
import math

def pearson(rating1, rating2):
  sum_xy = 0
  sum_x = 0
  sum_y = 0
  sum_x2 = 0
  sum_y2 = 0
  n = 0
  for key in rating1:
    if key in rating2:
      n += 1
      x = rating1[key]
      y = rating2[key]
      sum_xy += x * y
      sum_x += x
      sum_y += y
      sum_x2 += pow(x, 2)
      sum_y2 += pow(y, 2)
  if n == 0:
    return 0
  denominator = math.sqrt(sum_x2 - pow(sum_x, 2) / n) * math.sqrt(sum_y2 - pow(sum_y, 2) / n)
  if denominator == 0:
    return 0
  else:
    return (sum_xy - (sum_x * sum_y) / n) / denominator

def knn(userName, users):
  distancias = []
  for outro_usuario in users:
    if outro_usuario != userName:
      distancia = pearson(users[outro_usuario], users[userName])
      if distancia:
        distancias.append((distancia, outro_usuario))
  distancias.sort()
  return distancias #mude o k aqui

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
print(recommend('Almeida', users))
print('\n')
print(recommend('Ana', users))
print('\n')
print(recommend('Carlos', users))
print('\n')
print(recommend('Daniel', users))
print('\n')
print(recommend('Duarte', users))
print('\n')
print(recommend('Fabiana', users))
print('\n')
print(recommend('Jessica', users))
print('\n')
print(recommend('Maria', users))
print('\n')
print(recommend('Mateus', users))
print('\n')
print(recommend('Mike', users))
print('\n')
print(recommend('Paula', users))
print('\n')
print(recommend('Renato', users))
print('\n')
print(recommend('Roberta', users))
print('\n')
print(recommend('Sara', users))
print('\n')

#por algum motivo alguns usuarios como 
#Bianca, Clara, Ferb, Candace, Isabele
#Murilo, Paulinha, Gabriela, Perry
#estão dando erro de index
'''
print(recommend('Bianca', users))
print('\n')
print(recommend('Candece', users))
print('\n')
print(recommend('Clara', users))
print('\n')
print(recommend('Ferb', users))
print('\n')
print(recommend('Isabele', users))
print('\n')
print(recommend('Murilo', users))
print('\n')
print(recommend('Paulinha', users))
print('\n')
print(recommend('Gabriela', users))
print('\n')
print(recommend('Perry', users))
print('\n')
'''