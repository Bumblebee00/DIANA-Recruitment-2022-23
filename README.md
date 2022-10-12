# My solution

Funziona così:
1) scegli un punto
2) trova il punto più vicino a te
3) memorizza questo segmento
4) ripeti fino a quando non li hai percorsi tutti

Tuttavia, dopo aver finito, dato che questo problema mi sembrava molto "generale" ho fatto alcune ricerche su internet scoprendo che è il famoso "[Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)". Dopodichè ho trovato un implementzione dell'algoritmo "[Held–Karp](https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm)" (che risolve il problema in O(2^n * n^2)) su [Git Hub](https://github.com/CarlEkerot/held-karp) e ho semplicemente adattato il formato del nostro input a questo codice scritto da Carl Ekerot. Dato che non volevo modificare il suo codice, dopo aver chiamato la funzione held_karp aggiungo il primo punto alla fine della lista per chiudere il loop.

Questa repo contiene:
il file MarsPathPlanning.py che contiene il codice per eseguire il mio algoritmo,
il file HeldKarp.py che contiene il codice per l'algoritmo esatto
il file points_generator.py che serve a generare nuovi file di input
la cartella points che contiene tutti i filedi input
la cartella graphs che contiene il percorso generato dal programma, con entrambi gli algoritmi (mio in rosso, HeldHarp in verde)

