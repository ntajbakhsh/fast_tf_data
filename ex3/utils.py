import tensorflow as tf
import numpy as np
from time import sleep
from time import time


# data generator
def py_gen(num):
    for _ in range(3):
        tensor = np.arange(num * 10, (num + 1) * 10)
        sleep(1.5)
        for x in range(5):
            sleep(0.3)
            yield tensor[x * 2: (x + 1) * 2]


# model operation
def model(data):
    sleep(0.1)


def py_gen_p1(num):
    for _ in range(3):
        sleep(1.5)
        yield np.arange(num * 10, (num+1) * 10)

def py_gen_p2(tensor):
    for x in range(5):
        sleep(0.3)
        yield tensor[x * 2: (x + 1) * 2]

def run_session(data_tf):
    with tf.Session() as sess:
        while True:
            try:
                t1 = time()
                data_py = sess.run(data_tf)
                t2 = time()
                t = t2 - t1
                model(data_tf)
                msg = 'elapsed time: {:.3f}, {}'.format(t, data_py)
                print(msg)
            except tf.errors.OutOfRangeError:
                print('data generator(s) are exhausted')
                break
