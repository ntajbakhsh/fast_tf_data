# What's this repository about?
This repository provides the source codes for an article we have recently published:
 Building Multi-threaded Custom Data Pipelines for Tensorflow v1.12+.
  The article can be accessed [here](https://medium.com/@nimatajbakhsh/building-multi-threaded-custom-data-pipelines-for-tensorflow-f76e9b1a32f5)
   in html format or can be downloaded as a pdf from this repository. 

The article is a tutorial that explains tf.data through three easy-to-understand examples. 
Example 1 is a must-read, walking you through the most important concepts and pitfalls when using tf.data.
 You will learn how to write single-threaded and multi-threaded data pipelines as well as how to use
  pre-fetching to turn undesirable periodic delays into opportunities to keep your data queue full. 
  In Example 2, you will learn how to set up your data pipeline using a python class and how to avoid some
   common pitfalls. Example 3 teaches you how you can break a data pipeline into two smaller pipelines,
    further accelerating the data preparation process for your models.
   
# Structure of this repository

```python
├── ex1                                  # Must-read example
│   ├── gen_1thread.py                   # same thread for both data and model
│   ├── gen_1thread_upgraded_prefetch.py # 1 thread for data and 1 thread for model w/ prefetch
│   ├── gen_1thread_upgraded.py          # 1 thread for data and 1 thread for model w/o prefetch
│   ├── gen_multi_thread.py              # multi threaded solution
│   └── utils.py
├── ex1_noarg                            # same as ex1 but data loader needs no input arguments
│   ├── gen_multi_thread.py              # multi threaded solution
│   └── utils.py
├── ex2                                  # data loader is defined as an instance method of a class
│   ├── gen_1thread.py                   # same thread for both data and model
│   ├── gen_multi_thread.py              # multi threaded solution with an *educational bug*
│   ├── gen_multi_thread_v2.py           # multi threaded solution with bug fix
│   └── utils.py
├── ex3                                  # data loader consists of a slow followed by a fast stage
│   ├── gen_multi_thread.py              # *suboptimal* multi threaded solution
│   ├── gen_multi_thread_v2.py           # *optimal* multi threaded solution
│   └── utils.py
├── __init__.py
├── tf_dataset.pdf                       # Tutorial
├── readme.md
```

# Requirements
Tensorflow v1.12+ and Python 3.6