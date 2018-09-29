#!/usr/bin/env python
import tensorflow as tf
from data_helper import data_helper
from functions import *
import numpy as np
class dota2model:
    def __init__(self,config):
        self.hero_cont=130
        self.hidden_size=config['hidden_size']
        self.MAX_GRAD_NORM=config['MAX_GRAD_NORM']
        self.LR=config['LR']
        self.attention_flag=config['attention_flag']
        self.build_placeholder()
        self.build_para()
        self.forward()
        self.computer_loss()
        self._train()

    def build_placeholder(self):
        self.x_input=tf.placeholder(dtype=tf.int64,shape=[None,10],name='x_input')
        self.y_std=tf.placeholder(dtype=tf.float32,shape=[None],name='y_std')

    def build_para(self):
        initializer = tf.random_uniform_initializer(-0.25, 0.25)
        with tf.variable_scope('embedding',initializer=initializer):
            self.embedding = tf.get_variable(name='emb',dtype=tf.float32, shape=[self.hero_cont, self.hidden_size])
        with tf.variable_scope('attention',initializer=initializer):
            if self.attention_flag==1:
                self.attention_weight=tf.get_variable(name='attention_weight',dtype=tf.float32,shape=[self.hidden_size,self.hidden_size])

            elif self.attention_flag==2:
                self.attention_weight_1=tf.get_variable(name='attention_weight_1',dtype=tf.float32,shape=[self.hidden_size*6,self.hidden_size*3])
                self.attention_weight_2=tf.get_variable(name='attention_weight_2',dtype=tf.float32,shape=[self.hidden_size*3,self.hidden_size*2])
                self.attention_weight_3=tf.get_variable(name='attention_weight_3',dtype=tf.float32,shape=[self.hidden_size*2,self.hidden_size])
                self.att_b1=tf.get_variable(name='att_b1',dtype=tf.float32,shape=[self.hidden_size*3])
                self.att_b2 = tf.get_variable(name='att_b2', dtype=tf.float32, shape=[self.hidden_size * 2])
                self.att_b3 = tf.get_variable(name='att_b3', dtype=tf.float32, shape=[self.hidden_size])

        with tf.variable_scope('output_layers'):
            self.w1=tf.get_variable(name='w1',dtype=tf.float32,shape=[self.hidden_size*10,self.hidden_size*10])
            self.w2=tf.get_variable(name='w2',dtype=tf.float32,shape=[self.hidden_size*10,self.hidden_size*10])
            self.b1=tf.get_variable(name='b1',dtype=tf.float32,shape=[self.hidden_size*10])
            self.b2 = tf.get_variable(name='b2',dtype= tf.float32, shape=[self.hidden_size * 10])
            self.w3=tf.get_variable(name='w3',dtype=tf.float32,shape=[self.hidden_size*10,1])
            self.b3=tf.get_variable(name='b3',dtype=tf.float32,shape=[1])

    def forward(self):
        self.x_input_embedding=tf.nn.embedding_lookup(self.embedding,self.x_input)

        if self.attention_flag==1:
            self.attention_1()
        elif self.attention_flag==2:
            self.attention_2()

        tmp1=tf.nn.relu(tf.matmul(self.attentioned_output,self.w1)+self.b1)
        tmp2=tf.nn.relu(tf.matmul(tmp1,self.w2)+self.b2)
        self.y_pre=tf.sigmoid(tf.matmul(tmp2,self.w3)+self.b3)

    def attention_2(self):
        attentioned_list=[]
        for i in range(10):
            '''
            tmp = self.x_input_embedding[:, i, :]
            tmp1 = self.x_input_embedding[:, 5:, :]
            tmp3 = tf.concat([tmp, tmp1], axis=1)
            tmp4 = tf.nn.relu(tf.matmul(tmp3, self.attention_weight_1) + self.att_b1)
            tmp5 = tf.nn.relu(tf.matmul(tmp4, self.attention_weight_2) + self.att_b2)
            tmp6 = tf.matmul(tmp5, self.attention_weight_3) + self.att_b3
            attentioned_list.append(tmp6)
            '''
            if i<5:
                attentioned_list.append(
                    tf.matmul(
                        tf.nn.tanh(
                            tf.matmul(
                                tf.nn.tanh(
                                    tf.matmul(
                                        tf.concat(
                                            [self.x_input_embedding[:, i, :], tf.reshape(self.x_input_embedding[:, 5:, :],shape=[-1,self.hidden_size*5])],
                                            axis=1),
                                        self.attention_weight_1) + self.att_b1),
                                self.attention_weight_2) + self.att_b2),
                        self.attention_weight_3)+ self.att_b3)
            else:
                attentioned_list.append(
                    tf.matmul(
                        tf.nn.tanh(
                            tf.matmul(
                                tf.nn.tanh(
                                    tf.matmul(
                                        tf.concat(
                                            [self.x_input_embedding[:, i, :], tf.reshape(self.x_input_embedding[:, :5, :],shape=[-1,self.hidden_size*5])],
                                            axis=1),
                                        self.attention_weight_1) + self.att_b1),
                                self.attention_weight_2) + self.att_b2),
                        self.attention_weight_3) + self.att_b3)
        self.attentioned_output = tf.concat(attentioned_list, 1)

    def attention_1(self):
        attentioned_list = []
        for i in range(10):
            if i < 5:
                '''
                tmp=tf.transpose(tf.matmul(x_input_embedding[:,i,:],self.attention_weight))
                tmp = tf.matmul(x_input_embedding[:,5:, :], tf.reshape(tmp,shape=[-1,self.hidden_size,1]))
                tmp=tf.reshape(tmp,shape=[-1,1,5])
                tmp=tf.nn.softmax(tmp,axis=2)
                tmp=tf.matmul(tmp,x_input_embedding[:,5:,:])
                tmp=tf.reshape(tmp,shape=[-1,self.hidden_size])
                attentioned_list.append(tmp)
                '''
                attentioned_list.append(
                    tf.reshape(
                        tf.matmul(
                            tf.nn.softmax(
                                tf.reshape(
                                    tf.matmul(
                                        self.x_input_embedding[:, 5:, :], tf.reshape(
                                            tf.transpose(
                                                tf.matmul(
                                                    self.x_input_embedding[:, i, :], self.attention_weight))
                                            , shape=[-1, self.hidden_size, 1])), shape=[-1, 1, 5]), axis=2)
                            , self.x_input_embedding[:, 5:, :]), shape=[-1, self.hidden_size]))
            else:
                attentioned_list.append(
                    tf.reshape(
                        tf.matmul(
                            tf.nn.softmax(
                                tf.reshape(
                                    tf.matmul(
                                        self.x_input_embedding[:, :5, :], tf.reshape(
                                            tf.transpose(
                                                tf.matmul(
                                                    self.x_input_embedding[:, i, :], self.attention_weight))
                                            , shape=[-1, self.hidden_size, 1])), shape=[-1, 1, 5]), axis=2)
                            , self.x_input_embedding[:, :5, :]), shape=[-1, self.hidden_size]))
        self.attentioned_output = tf.concat(attentioned_list, 1)

    def computer_loss(self):
        y_std = tf.reshape(self.y_std, shape=[-1,1])
        y_pre = tf.reshape(self.y_pre, shape=[-1,1])

        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(0.1)(self.w1))
        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(0.1)(self.w2))
        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(0.1)(self.w3))

        tf.add_to_collection("losses",
                             -tf.reduce_mean((y_std * tf.log(tf.clip_by_value(y_pre, 1e-10, 1.0)) +
                                             (1.- y_std)* tf.log(tf.clip_by_value(1. - y_pre, 1e-10, 1.0)))))

        self.loss = tf.add_n(tf.get_collection("losses"))

    def _train(self):
        trainable_variables = tf.trainable_variables()

        grads = tf.gradients(self.loss, trainable_variables)
        # grads, _ = tf.clip_by_global_norm(grads, self.MAX_GRAD_NORM)
        opt = tf.train.AdadeltaOptimizer(learning_rate=self.LR)
        self.train_op = opt.apply_gradients(zip(grads, trainable_variables))





def pre(pre_socre,truth):
    pre_socre=np.reshape(pre_socre,[-1])
    truth=np.reshape(truth,[-1])
    sum=0
    c=0
    for i,j in zip(pre_socre,truth):
        if c<30:
            print(i,j)
            c+=1
        i=int(i+0.5)
        if int(i)==int(j):
            sum=sum+1
    return sum/float(len(pre_socre))

if __name__=='__main__':

    config={'hidden_size':256,
            'MAX_GRAD_NORM':5,
            'LR':0.3,
            'attention_flag':2}


    dh_config = {'train_file': '../build_data/data_train',
                 'test_file': '../build_data/data_test',
                 'val_file': '../build_data/data_val'
                 }

    dh = data_helper(dh_config)
    model = dota2model(config)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        for i in range(100000):
            train_x,train_y=dh.next_batch(1000)
            sess.run(model.train_op, feed_dict={model.x_input: train_x,
                                                model.y_std: train_y})
            if i%100==0:
                val_x, val_y = dh.get_val_batch()
                loss,model_score=sess.run([model.loss,model.y_pre], feed_dict={model.x_input: val_x,
                                                      model.y_std: val_y})

                # print(sess.run([model.w3,model.w2,model.w1],feed_dict={model.x_input: val_x,
                #                                       model.y_std: val_y}
                #                ))
                print('*******************',loss,pre(model_score,val_y))
                # saver.save(sess, 'dota2model')
            # print(sess.run(model.loss, feed_dict={model.x_input: np.array([[1, 2, 3, 4, 5, 6, 7,8,9,10],
            #                                                                 [11,12,13,14,15,16,17,18,19,20]]),
            #                                   model.y_std:np.array([0,1])}))








