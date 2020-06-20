import math
import multiprocessing as mp
import os


# ----------------------------------------------------------------------------------------------------------------------
# https://github.com/madhug-nadig/Parallel-Processing-Nadig/blob/master/Python%20multiprocessing%20example-%20Process.py
# ----------------------------------------------------------------------------------------------------------------------


def process_info():
    print('Module:' + str(__name__) + '\n')
    print('Parent Process id:' + str(os.getppid()) + '\n')
    print('Process id:' + str(os.getpid()) + '\n\n')


def cubes_and_sqare_root(a, x, output):
    process_info()
    output.put((int(x), math.sqrt(a ** 3)))


def main():
    # Using the queue as the message passing paradigm
    output = mp.Queue()
    processes = [mp.Process(target=cubes_and_sqare_root, args=(x, x, output)) for x in range(1, 8)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    results = [output.get() for process in processes]

    print(results)


if __name__ == '__main__':
    # print(sys.argv[0])
    main()

