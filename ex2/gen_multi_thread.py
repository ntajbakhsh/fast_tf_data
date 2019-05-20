import tensorflow as tf
from utils import DataGen
from utils import run_session

# ===== In this solution, multiple threads are assigned to the data loader, which is defined as instance method of a class.
# Note: this solution has an educational bug in it.

# set up tf generator
Dataset = tf.data.Dataset
dummy_ds = Dataset.from_tensor_slices(['Gen', 'Gen', 'Gen'])
dummy_ds = dummy_ds.interleave(lambda x: Dataset.from_generator(DataGen().py_gen, output_types=(tf.string), args=(x,)),
                               cycle_length=3,
                               block_length=1,
                               num_parallel_calls=3)
data_tf = dummy_ds.make_one_shot_iterator().get_next()

run_session(data_tf)

"""
output:
    elapsed time: 0.329, Gen_0 yields 0
    elapsed time: 0.001, Gen_0 yields 0
    elapsed time: 0.001, Gen_0 yields 0
    elapsed time: 0.001, Gen_0 yields 1
    elapsed time: 0.001, Gen_0 yields 1
    elapsed time: 0.001, Gen_0 yields 1
    elapsed time: 0.001, Gen_0 yields 2
    elapsed time: 0.001, Gen_0 yields 2
    elapsed time: 0.001, Gen_0 yields 2
    elapsed time: 0.001, Gen_0 yields 3
    elapsed time: 0.001, Gen_0 yields 3
    elapsed time: 0.001, Gen_0 yields 3
    elapsed time: 0.001, Gen_0 yields 4
    elapsed time: 0.001, Gen_0 yields 4
    elapsed time: 0.001, Gen_0 yields 4
"""
