# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:32:22 2020

@author: a0970
"""

import tensorflow as tf

hello = tf.constant('Hellow Tensorflow')
sess = tf.Session()
print(sess.run(hello))

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())