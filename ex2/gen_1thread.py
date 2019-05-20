import tensorflow as tf
from time import sleep
from time import time

# ===== In this solution, 1 thread is assigned to the data loader, which is defined as instance method of a class.

Dataset = tf.data.Dataset


# python generator
class DataGen():
    def __init__(self, gen_name):
        self.gen_name = gen_name

    def py_gen(self):
        for num in range(5):
            sleep(0.3)
            yield '{} yields {}'.format(self.gen_name, num)


# model operation
def model():
    sleep(0.1)

# commma is essential other wise unpacked
# set up tf generator
name = 'Gen_0'
dummy_ds = Dataset.from_generator(DataGen(name).py_gen,
                                  output_types=(tf.string))
data_tf = dummy_ds.make_one_shot_iterator().get_next()

with tf.Session() as sess:
    while True:
        t1 = time()
        data_py = sess.run(data_tf)
        t2 = time()
        model()
        t = t2 - t1
        print_msg = 'elapsed time: {:.3f}, {}'.format(t, data_py.decode('utf-8'))
        print(print_msg)

"""
output:
    elapsed time: 0.320, Gen_0 yields 0
    elapsed time: 0.302, Gen_0 yields 1
    elapsed time: 0.302, Gen_0 yields 2
    elapsed time: 0.302, Gen_0 yields 3
    elapsed time: 0.302, Gen_0 yields 4
"""
