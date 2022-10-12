from random import uniform


def rnd_num():
    return round(uniform(-1000, 1000), 1)


n = 30

txt = str(n) + '\n'
for x in range(n):
    txt += f'{rnd_num()}, {rnd_num()}\n'
print(txt)