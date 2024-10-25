import time
import sys

def ft_progress(range_list):
    tam_bar = 30
    tot = len(range_list)
    ini = time.time()

    for i in range_list:
        temp = time.time() - ini
        porc = (i + 1)/tot
        eta = temp / (i + 1) * (tot - (i + 1))

        barra = ('=' * int(porc * tam_bar)).ljust(tam_bar)
        sys.stdout.write(f'\r ETA: {eta:.2f}s | {porc:.2%} Concluido | [{ barra}] | Iteração: {i + 1}/{tot} | Tempo Decorrido: {temp:.2f}s')
        sys.stdout.flush()

        yield i 
    sys.stdout.write('\n')
    sys.stdout.flush()



from time import sleep

a_list = range(1000)
ret = 0
for elem in ft_progress(a_list):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)