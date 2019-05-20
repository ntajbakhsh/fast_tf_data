import tensorflow as tf
from utils import py_gen
from utils import run_session

# ===== In this solution, multiple threads are used for data preparation when no input arguments are required.

# set up tf generator
Dataset = tf.data.Dataset
ds = Dataset.from_tensor_slices(['xxx', 'xxx', 'xxx'])
ds = ds.interleave(lambda x: Dataset.from_generator(py_gen, output_types=(tf.string)),
                   cycle_length=3,
                   block_length=1,
                   num_parallel_calls=3)
data_tf = ds.make_one_shot_iterator().get_next()

run_session(data_tf)

"""
output:
    elapsed time: 0.330, no name yields 0
    elapsed time: 0.001, no name yields 0
    elapsed time: 0.001, no name yields 0
    elapsed time: 0.001, no name yields 1
    elapsed time: 0.001, no name yields 1
    elapsed time: 0.001, no name yields 1
    elapsed time: 0.001, no name yields 2
    elapsed time: 0.001, no name yields 2
    elapsed time: 0.001, no name yields 2
    elapsed time: 0.001, no name yields 3
    elapsed time: 0.001, no name yields 3
    elapsed time: 0.001, no name yields 3
    elapsed time: 0.001, no name yields 4
    elapsed time: 0.001, no name yields 4
    elapsed time: 0.001, no name yields 4
"""
