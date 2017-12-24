def generator(n):
    while n:
        print('Zwracam %d z generatora' % n)
        yield n
        n -= 1
import time
for x in generator(10):
    time.sleep(0.5)
    print('Wypisuję %d w pętli. ' % x)
    time.sleep(0.5)
    
generator = ((x ,2*x) for x in range(10))
for a, b in generator:
    print(a, b)