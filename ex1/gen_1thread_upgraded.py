import tensorflow as tf
from utils import py_gen
from utils import run_session

# ===== In this solution, a dedicated thread is assigned to the data loader

# set up tf generator
Dataset = tf.data.Dataset
name = 'Gen_0'
ds = Dataset.from_generator(py_gen,
                            output_types=(tf.string),
                            args=(name,))
ds = ds.map(lambda x: x, num_parallel_calls=1)
data_tf = ds.make_one_shot_iterator().get_next()

run_session(data_tf)

"""
output:
    elapsed time: 0.322, Gen_0 yields 0
    elapsed time: 0.201, Gen_0 yields 1
    elapsed time: 0.201, Gen_0 yields 2
    elapsed time: 0.201, Gen_0 yields 3
    elapsed time: 0.201, Gen_0 yields 4
"""
