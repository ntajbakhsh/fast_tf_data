import tensorflow as tf
from utils import py_gen
from utils import run_session

# ===== In this solution, multiple threads are used for data preparation.
# Note: num_parallel_calls must be less than or equal to cycle_length

# set up tf generator
Dataset = tf.data.Dataset
ds = Dataset.from_tensor_slices(['Gen_0', 'Gen_1', 'Gen_2'])
ds = ds.interleave(lambda x: Dataset.from_generator(py_gen, output_types=(tf.string), args=(x,)),
                   cycle_length=3,
                   block_length=1,
                   num_parallel_calls=3)
data_tf = ds.make_one_shot_iterator().get_next()

run_session(data_tf)

"""
output:
    elapsed time: 0.327, Gen_0 yields 0
    elapsed time: 0.001, Gen_1 yields 0
    elapsed time: 0.001, Gen_2 yields 0
    elapsed time: 0.001, Gen_0 yields 1
    elapsed time: 0.001, Gen_1 yields 1
    elapsed time: 0.001, Gen_2 yields 1
    elapsed time: 0.001, Gen_0 yields 2
    elapsed time: 0.001, Gen_1 yields 2
    elapsed time: 0.001, Gen_2 yields 2
    elapsed time: 0.001, Gen_0 yields 3
    elapsed time: 0.001, Gen_1 yields 3
    elapsed time: 0.001, Gen_2 yields 3
    elapsed time: 0.001, Gen_0 yields 4
    elapsed time: 0.001, Gen_1 yields 4
    elapsed time: 0.001, Gen_2 yields 4
"""
