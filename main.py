import tkinter as tk
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
  denominator = math.sqrt(sum_x2 - pow(sum_x, 2) /
                          n) * math.sqrt(sum_y2 - pow(sum_y, 2) / n)
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
  return distancias  #mude o k aqui


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
  return sorted(recommendations,
                key=lambda artistTuple: artistTuple[1],
                reverse=True)

def show_values(username, users):
    recommendations = recommend(username, users)
    text.delete("1.0", tk.END)
    text.insert(tk.END, f"USER: {username}\n")
    text.insert(tk.END, f"\nMOVIES RATED:\n")
    for item, value in users[username].items():
        text.insert(tk.END, f"{item}: {value}\n")
    text.insert(tk.END, f"\nRECOMMENDATIONS:\n")
    for item, value in recommendations:
        text.insert(tk.END, f"{item}: {value}\n")

root = tk.Tk()
root.geometry("400x600")
root.title("Movie Recommendation System")

label = tk.Label(root, text="Select User:")
label.pack(pady=10)

user_var = tk.StringVar(root)
user_var.set("Almeida")

dropdown = tk.OptionMenu(root, user_var, *users.keys())
dropdown.pack()

button = tk.Button(root, text="Show Recommendations", command=lambda: show_values(user_var.get(), users))
button.pack(pady=10)

text = tk.Text(root, height=30, width=50)
text.pack()

root.mainloop()