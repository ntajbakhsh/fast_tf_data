import tensorflow as tf
from time import sleep
from time import time

# data generator
def py_gen():
    for num in range(5):
        sleep(0.3)
        yield '{} yields {}'.format('no name', num)


# model operation
def model(data):
    sleep(0.1)

def run_session(data_tf):
    with tf.Session() as sess:
        while True:
            try:
                t1 = time()
                data_py = sess.run(data_tf)
                t2 = time()
                t = t2 - t1
                model(data_tf)
                msg = 'elapsed time: {:.3f}, {}'.format(t, data_py.decode('utf-8'))
                print(msg)
            except tf.errors.OutOfRangeError:
                print('data generator(s) are exhausted')
                break
