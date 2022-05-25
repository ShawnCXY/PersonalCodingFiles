# coding:utf-8

import tensorflow as tf
import tensorflow_probability as tfp

from tensorflow import keras
from keras.layers import Input, Dense, LSTM, Dropout, TimeDistributed, Lambda

class DeepAR(tf.keras.models.Model):
    def __init__(self, lstm_units, n_steps_in, n_steps_out, n_features):
        super().__init__()

        self.lstm = tf.keras.layers.LSTM(lstm_units, return_sequences=True, return_state=True, input_shape=(n_steps_in, n_features))
        self.dense_mu = tf.keras.layers.Dense(1) 
        self.dense_sigma = tf.keras.layers.Dense(1, activation='softplus')

    def call(self, inputs, initial_state=None):
        outputs, state_h, state_c = self.lstm(inputs, initial_state=initial_state)

        mu = self.dense_mu(outputs)
        sigma = self.dense_sigma(outputs)
        state = [state_h, state_c]

        return [mu, sigma, state]

def log_gaussian_loss(mu, sigma, y_true):
    """
    Gaussian loss function
    """
    return -tf.reduce_sum(tfp.distributions.Normal(loc=mu, scale=sigma).log_prob(y_true))

