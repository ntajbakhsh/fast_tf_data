import tensorflow as tf
from utils import py_gen
from utils import run_session_w_delay

# ===== In this solution, a dedicated thread is assigned to the data loader. Pre-fetching is further utilized.

# set up tf generator
Dataset = tf.data.Dataset
name = 'Gen_0'
ds = Dataset.from_generator(py_gen,
                            output_types=(tf.string),
                            args=(name,))
ds = ds.map(lambda x: x, num_parallel_calls=1)
ds = ds.prefetch(buffer_size=10)
data_tf = ds.make_one_shot_iterator().get_next()

run_session_w_delay(data_tf)

"""
output without pre-fetching:
    elapsed time: 0.322, Gen_0 yields 0
    elapsed time: 0.201, Gen_0 yields 1
    elapsed time: 0.201, Gen_0 yields 2
    elapsed time: 0.001, Gen_0 yields 3
    elapsed time: 0.201, Gen_0 yields 4
    elapsed time: 0.201, Gen_0 yields 5
    elapsed time: 0.201, Gen_0 yields 6
    elapsed time: 0.201, Gen_0 yields 7
    elapsed time: 0.201, Gen_0 yields 8
    elapsed time: 0.201, Gen_0 yields 9
"""
"""
output with pre-fetching:
    elapsed time: 0.324, Gen_0 yields 0
    elapsed time: 0.201, Gen_0 yields 1
    elapsed time: 0.201, Gen_0 yields 2
    elapsed time: 0.001, Gen_0 yields 3
    elapsed time: 0.001, Gen_0 yields 4
    elapsed time: 0.001, Gen_0 yields 5
    elapsed time: 0.001, Gen_0 yields 6
    elapsed time: 0.001, Gen_0 yields 7
    elapsed time: 0.001, Gen_0 yields 8
    elapsed time: 0.001, Gen_0 yields 9
"""