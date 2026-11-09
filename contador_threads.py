import threading

contador = 0
lock = threading.Lock()


def incrementar():
    global contador

    for i in range(100000):
        with lock:
            contador += 1


threads = []

for i in range(4):
    t = threading.Thread(target=incrementar)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Contador final:", contador)