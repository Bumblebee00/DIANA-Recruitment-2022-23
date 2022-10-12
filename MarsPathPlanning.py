from matplotlib import pyplot as plt
from math import sqrt
from HeldKarp import held_karp

path = "points/points.txt"

txt = '''
La mia soluzione al problema è la prima che verrà stampata a schermo, dopo queata introduzione, ed è mostrata con i \
grafici rossi. L'ultimo elemento della lista è il punto di partenza, e anche questo ultimo segmento è contato nella \
distanza totale. Tuttavia, dopo aver finito, dato che questo problema mi sembrava molto "generale" ho fatto alcune \
ricerche su internet scoprendo che è il famoso "Travelling salesman problem". Dopodichè ho trovato un implementzione \
dell'algoritmo "Held–Karp" (che risolve il problema in O(2^n * n^2)) su Git Hub (https://github.com/CarlEkerot/held-karp) \
e ho semplicemente adattato il formato del nostro input a questo codice scritto da Carl Ekerot. Dato che non volevo \
modificare il suo codice, dopo aver chiamato la funzione held_karp aggiungo il primo punto alla fine della lista per \
chiudere il loop. Questa soluzione esatta sarà stampata a schermo per ultima, e i grafici saranno di colore rosso.
'''
print(txt)


def point_from_str(s):
    return tuple([float(coo) for coo in s.split(', ')])


def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def my_approach(points):
    # Funziona così:
    # 1) scegli un punto
    # 2) trova il punto più vicino a te
    # 3) memorizza questo segmento
    # 4) ripeti fino a quando non li hai percorsi tutti
    current_p = points[0]  # contains x, y values
    non_used_points = points.copy()[1:]  # contains x, y values
    used_points = [0]  # contains indexes
    tot_dist = 0

    for i in range(len(points) - 1):
        # distances to all the remaining points
        distances = [distance(current_p, non_used_points[j]) for j in range(len(non_used_points))]
        shorter_distance = min(distances)
        closer_point = non_used_points[distances.index(shorter_distance)]  # contains x, y values

        non_used_points.remove(closer_point)
        used_points.append(points.index(closer_point))
        tot_dist += shorter_distance
        current_p = closer_point
    # adds first element at the end to close the loop
    tot_dist += distance(points[0], current_p)
    used_points.append(0)
    return used_points, tot_dist


# gather data
with open(path, "r") as f:
    data = list(f)
data = [point_from_str(p[:-1]) for p in data[1:]]

# plot the points
for p in data:
    plt.plot(p[0], p[1], marker="o")
plt.show()

# execute my approach
order_of_points, total_distance = my_approach(data)
# print result
print("My solution: ")
print(*order_of_points)
print(str(total_distance) + 'm')
# plot result
plt.title(f"My solution: {round(total_distance, 1)}m")
plt.plot([data[i][0] for i in order_of_points], [data[i][1] for i in order_of_points], 'r')
plt.plot(data[0], marker='o')
plt.show()

# create distance matrix
n = len(data)
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j] = matrix[j][i] = distance(data[i], data[j])

# execute exact approach
print("Held–Karp Alghoritm (exact) solution:")
total_distance, order_of_points = held_karp(matrix)
total_distance += distance(data[0], data[order_of_points[-1]])
order_of_points.append(0)
# print result
print(*order_of_points)
print(str(total_distance) + 'm')
# plot results
plt.title(f"Held–Karp Alghoritm (not mine): {round(total_distance, 1)}m")
plt.plot([data[i][0] for i in order_of_points], [data[i][1] for i in order_of_points], 'g')
plt.plot(data[0], marker='o')
plt.show()
