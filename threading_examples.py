from threading import Thread, Lock, current_thread
from queue import Queue
import time

# all threads can access this global variable
database_value = 0


def increase(lock):
    global database_value  # needed to modify the global value

    # use context manager
    with lock:
        # get a local copy (simulate data retrieving)
        local_copy = database_value

        # simulate some modifying operation
        local_copy += 1
        time.sleep(0.1)

        # write the calculated new value into the global variable
        database_value = local_copy


def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            # processing..
            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == "__main__":
    lock = Lock()
    print('Start value: ', database_value)

    t1 = Thread(target=increase, args=(lock,))
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')

    q = Queue()

    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  # dies when the main thread dies
        thread.start()

    for i in range(1, 100):
        q.put(i)

    q.join()
