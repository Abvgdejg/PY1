# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Boston housing price regression dataset.
"""

import sys as _sys

from keras.datasets.boston_housing import load_data
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.datasets.boston_housing", public_apis=None, deprecation=True,
      has_lite=False)