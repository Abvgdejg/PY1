# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""CIFAR10 small images classification dataset.
"""

import sys as _sys

from keras.datasets.cifar10 import load_data
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.datasets.cifar10", public_apis=None, deprecation=True,
      has_lite=False)