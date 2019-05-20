import tensorflow as tf
from utils import py_gen
from utils import run_session

# ===== In this solution, the same thread prepares data and runs the TF operation

# commma is essential in "args=(name,)" otherwise an exception is thrown
# set up tf generator
Dataset = tf.data.Dataset
name = 'Gen_0'
ds = Dataset.from_generator(py_gen,
                            output_types=(tf.string),
                            args=(name,))
data_tf = ds.make_one_shot_iterator().get_next()

run_session(data_tf)
"""
output:
    elapsed time: 0.320, Gen_0 yields 0
    elapsed time: 0.302, Gen_0 yields 1
    elapsed time: 0.302, Gen_0 yields 2
    elapsed time: 0.302, Gen_0 yields 3
    elapsed time: 0.302, Gen_0 yields 4
"""
