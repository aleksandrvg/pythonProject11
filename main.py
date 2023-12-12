from multiprocessing import Process
import threading
import time


def Hello(name):
    print("Привет", name)
    time.sleep(2)
Hello("Егор")
Hello("Максим")


if __name__ == "__main__":
    p1 = Process(target=Hello, args=('Ефим',), daemon=True)
    p2 = threading.Thread(target=Hello, args=('Алексей',), daemon=True)
    # p1.start()
    # p2.start()
    # print(p2.is_alive())
    # p1.join()
    # p2.join()

    p1.start()
    p1.join()
    while p1.is_alive():
        continue
    p2.start()
    p2.join()
    