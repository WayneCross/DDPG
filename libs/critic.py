import tensorflow as tf
from tensorflow.keras.layers import Dense, BatchNormalization, Activation, Input, Concatenate
from tensorflow.keras import optimizers
import numpy as np

class Critic(object):
    def __init__(self, state_size, action_size, lr):
        self.state_size = state_size
        self.action_size = action_size
        self.lr = lr
        self.model = self.create_critic_network()


    def create_critic_network(self):
        state_in = Input(shape=(self.state_size,), dtype='float64')
        state_net = BatchNormalization()(state_in)
        state_net = Dense(16, activation='relu')(state_net)
        state_net = BatchNormalization()(state_net)

        action_in = Input(shape=(self.action_size,), dtype='float64')
        action_net = BatchNormalization()(action_in)
        action_net = Dense(16, activation='relu')(action_net)
        action_net = BatchNormalization()(action_net)

        net = Concatenate()([state_net, action_net])
        net = Dense(8, activation="relu")(net)
        net = BatchNormalization()(net)
        out = Dense(1, activation='linear')(net)
        model = tf.keras.Model(inputs=[state_in, action_in], outputs=[out])

        
        new_w = np.random.uniform(low=-3e-3, high=3e-3, size=(8,1))
        new_b = np.random.uniform(low=-3e-3, high=3e-3, size=(1))
        model.layers[-1].set_weights([new_w, new_b])
        
       
        return model

    