# pylint: disable=no-value-for-parameter,invalid-name,unexpected-keyword-arg
"""Learned Multiply Model"""

import logging

import tensorflow as tf

import deepr


LOGGER = logging.getLogger(__name__)


@deepr.layers.layer(inputs="x", outputs="y_pred")
def Multiply(tensors):
    alpha = tf.get_variable(name="alpha", shape=(), dtype=tf.float32)
    return tf.multiply(alpha, tensors, name="y_pred")
