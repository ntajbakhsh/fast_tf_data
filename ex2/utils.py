import tensorflow as tf
from time import sleep
from time import time


class DataGen():
    counter = 0

    def __init__(self):
        self.gen_num = DataGen.counter
        DataGen.counter += 1

    def py_gen(self, gen_name):
        gen_name = gen_name.decode('utf8') + '_' + str(self.gen_num)
        for num in range(5):
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
