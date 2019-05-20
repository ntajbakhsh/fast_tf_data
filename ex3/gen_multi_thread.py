import tensorflow as tf
from utils import py_gen
from utils import run_session

# ===== In this solution, multiple threads are assigned to a 2-stage data loader: stage 1 is slow, but stage 2 is fast.
# Note: this solution is not optimal.

# set up tf generator
Dataset = tf.data.Dataset
ds = Dataset.from_tensor_slices([0, 1, 2])
ds = ds.interleave(lambda x: Dataset.from_generator(py_gen, output_types=(tf.float32), args=(x,)),
                               cycle_length=3,
                               block_length=1,
                               num_parallel_calls=3)
data_tf = ds.make_one_shot_iterator().get_next()

run_session(data_tf)

"""
output:
    elapsed time: 1.828, [0. 1.]
    elapsed time: 0.001, [10. 11.]
    elapsed time: 0.001, [20. 21.]
    elapsed time: 0.001, [2. 3.]
    elapsed time: 0.001, [12. 13.]
    elapsed time: 0.001, [22. 23.]
    elapsed time: 0.001, [4. 5.]
    elapsed time: 0.001, [14. 15.]
    elapsed time: 0.001, [24. 25.]
    elapsed time: 0.001, [6. 7.]
    elapsed time: 0.001, [16. 17.]
    elapsed time: 0.001, [26. 27.]
    elapsed time: 0.001, [8. 9.]
    elapsed time: 0.001, [18. 19.]
    elapsed time: 0.001, [28. 29.]
    elapsed time: 1.498, [0. 1.]
    elapsed time: 0.001, [10. 11.]
    elapsed time: 0.001, [20. 21.]
    elapsed time: 0.001, [2. 3.]
    elapsed time: 0.001, [12. 13.]
    elapsed time: 0.001, [22. 23.]
    elapsed time: 0.001, [4. 5.]
    elapsed time: 0.001, [14. 15.]
    elapsed time: 0.001, [24. 25.]
    elapsed time: 0.001, [6. 7.]
    elapsed time: 0.001, [16. 17.]
    elapsed time: 0.001, [26. 27.]
    elapsed time: 0.001, [8. 9.]
    elapsed time: 0.001, [18. 19.]
    elapsed time: 0.001, [28. 29.]
    elapsed time: 1.499, [0. 1.]
    elapsed time: 0.001, [10. 11.]
    elapsed time: 0.001, [20. 21.]
    elapsed time: 0.001, [2. 3.]
    elapsed time: 0.001, [12. 13.]
    elapsed time: 0.001, [22. 23.]
    elapsed time: 0.001, [4. 5.]
    elapsed time: 0.001, [14. 15.]
    elapsed time: 0.001, [24. 25.]
    elapsed time: 0.001, [6. 7.]
    elapsed time: 0.001, [16. 17.]
    elapsed time: 0.001, [26. 27.]
    elapsed time: 0.001, [8. 9.]
    elapsed time: 0.001, [18. 19.]
    elapsed time: 0.001, [28. 29.]
"""
