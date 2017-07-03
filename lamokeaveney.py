import random
import matplotlib.pyplot as plt

setlength = 90.0
songlength = 3.0

samesongpercentage = 0.3

totalsongs = int(setlength / songlength)
samesongs = int(totalsongs * samesongpercentage)
differentsongs = totalsongs - samesongs

commonsongs = range(0,samesongs)


shaunsongs = commonsongs + range(1000,1000+differentsongs)
lamosongs = commonsongs + range(5000,5000+differentsongs)

results = []

hits = 0.0
iterations = 0.0
hitp = 0.0

for _ in range(0,10000):
    random.shuffle(shaunsongs)
    random.shuffle(lamosongs)

    match = 0

    for song in commonsongs:
        if shaunsongs.index(song) == lamosongs.index(song):
            match = match+1

    iterations = iterations + 1.0

    if match>0:
        hits = hits+1.0

    hitp = hits/iterations

    results = results + [hitp]


print hitp

plt.plot(results)
plt.show()