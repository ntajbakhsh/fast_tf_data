import tensorflow as tf
from time import sleep
from time import time

# data generator
def py_gen(gen_name):
    gen_name = gen_name.decode('utf-8')
    for num in range(20):
        sleep(0.3)
        yield '{} yields {}'.format(gen_name, num)


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

def run_session_w_delay(data_tf):
    with tf.Session() as sess:
        counter = 1
        while True:
            try:
                if counter == 4:
                    sleep(3)
                t1 = time()
                data_py = sess.run(data_tf)
                t2 = time()
                t = t2 - t1
                model(data_tf)
                msg = 'elapsed time: {:.3f}, {}'.format(t, data_py.decode('utf-8'))
                print(msg)
                counter += 1
            except tf.errors.OutOfRangeError:
                print('data generator(s) are exhausted')
                break