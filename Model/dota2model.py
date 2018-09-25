import tensorflow as tf
import numpy as np
import random as rd

class dota2model:
    def __init__(self,config):
        self.hero_cont=108
        self.hidden_size=config['hidden_size']
        self.build_placeholder()
        self.build_para()
        self.forward()
        self.computer_loss()

    def build_placeholder(self):
        self.x_input=tf.placeholder(dtype=tf.int32,shape=[None,10],name='x_input')
        self.y_std=tf.placeholder(dtype=tf.float32,shape=[None],name='y_std')

    def build_para(self):
        initializer = tf.random_uniform_initializer(-0.5, 0.5)
        with tf.variable_scope('embedding',initializer=initializer):
            self.embedding = tf.get_variable(name='emb',dtype=tf.float32, shape=[self.hero_cont, self.hidden_size])
        with tf.variable_scope('attention',initializer=initializer):
            self.attention_weight=tf.get_variable(name='attention_weight',dtype=tf.float32,shape=[self.hidden_size,self.hidden_size])
        with tf.variable_scope('output_layers'):
            self.w1=tf.get_variable(name='w1',dtype=tf.float32,shape=[self.hidden_size*10,self.hidden_size*10])
            self.w2=tf.get_variable(name='w2',dtype=tf.float32,shape=[self.hidden_size*10,self.hidden_size*10])
            self.b1=tf.get_variable(name='b1',dtype=tf.float32,shape=[self.hidden_size*10])
            self.b2 = tf.get_variable(name='b2',dtype= tf.float32, shape=[self.hidden_size * 10])
            self.w3=tf.get_variable(name='w3',dtype=tf.float32,shape=[self.hidden_size*10,1])
            self.b3=tf.get_variable(name='b3',dtype=tf.float32,shape=[1])

    def forward(self):
        x_input_embedding=tf.nn.embedding_lookup(self.embedding,self.x_input)
        attentioned_list=[]
        for i in range(10):
            if i<5:
                # tmp=tf.transpose(tf.matmul(x_input_embedding[:,i,:],self.attention_weight))
                # tmp = tf.matmul(x_input_embedding[:,5:, :], tf.reshape(tmp,shape=[-1,self.hidden_size,1]))
                # tmp=tf.reshape(tmp,shape=[-1,1,5])
                # tmp=tf.nn.softmax(tmp,axis=2)
                # tmp=tf.matmul(tmp,x_input_embedding[:,5:,:])
                # tmp=tf.reshape(tmp,shape=[-1,self.hidden_size])
                # attentioned_list.append(tmp)
                attentioned_list.append(
                    tf.reshape(
                        tf.matmul(
                            tf.nn.softmax(
                                tf.reshape(
                                    tf.matmul(
                                        x_input_embedding[:, 5:, :], tf.reshape(
                                            tf.transpose(
                                                tf.matmul(
                                                    x_input_embedding[:, i, :], self.attention_weight))
                                            , shape=[-1, self.hidden_size, 1])), shape=[-1, 1, 5]), axis=2)
                            , x_input_embedding[:, 5:, :]), shape=[-1, self.hidden_size]))
            else:
                attentioned_list.append(
                    tf.reshape(
                        tf.matmul(
                            tf.nn.softmax(
                                tf.reshape(
                                    tf.matmul(
                                        x_input_embedding[:, :5, :], tf.reshape(
                                            tf.transpose(
                                                tf.matmul(
                                                    x_input_embedding[:, i, :], self.attention_weight))
                                            , shape=[-1, self.hidden_size, 1])), shape=[-1, 1, 5]), axis=2)
                            , x_input_embedding[:, :5, :]), shape=[-1, self.hidden_size]))
        attentioned_output=tf.concat(attentioned_list,1)
        tmp1=tf.nn.relu(tf.matmul(attentioned_output,self.w1)+self.b1)
        tmp2=tf.nn.relu(tf.matmul(tmp1,self.w2)+self.b2)
        self.y_pre=tf.sigmoid(tf.matmul(tmp2,self.w3)+self.b3)


    def computer_loss(self):
        y_std = tf.reshape(self.y_std, shape=[-1, 1])
        y_pre = tf.reshape(self.y_pre, shape=[-1, 1])

        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(0.3)(self.w1))
        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(0.3)(self.w2))
        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(0.3)(self.w3))

        tf.add_to_collection("losses",-tf.reduce_sum((y_std * tf.log(tf.clip_by_value(y_pre, 1e-10, 1.0)) + (1 - y_std))* tf.log(tf.clip_by_value(1 - y_pre, 1e-10, 1.0))))

        self.loss = tf.add_n(tf.get_collection("losses"))


if __name__=='__main__':
    config={'hidden_size':256}
    model=dota2model(config)

    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    print(sess.run(model.loss, feed_dict={model.x_input: np.array([[1, 2, 3, 4, 5, 6, 7,8,9,10],
                                                                        [11,12,13,14,15,16,17,18,19,20]]),
                                          model.y_std:np.array([0,1])}))








