from dota2model import *
import tensorflow as tf
from sklearn import metrics
config = {'hidden_size': 256,
          'MAX_GRAD_NORM': 5,
          'LR': 0.2,
          'attention_flag': 2,
          'keep_prob': 0.8}
if len(sys.argv) == 2:
    config['attention_flag'] = int(sys.argv[1])

dh_config = {'train_file': '../build_data/data_train',
             'test_file': '../build_data/data_test',
             'val_file': '../build_data/data_val'
             }

dh = data_helper(dh_config)
model = dota2model(config)

max_auc=0
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    for i in range(100000):
        train_x, train_y = dh.next_batch(1000)
        sess.run(model.train_op, feed_dict={model.x_input: train_x,
                                            model.y_std: train_y})
        if i % 100 == 0:
            val_x, val_y = dh.get_val_batch()
            loss, model_score = sess.run([model.loss, model.y_pre], feed_dict={model.x_input: val_x,
                                                                               model.y_std: val_y})

            pre_value,auc_value=[pre(model_score, val_y), metrics.roc_auc_score(val_y,model_score)]
            print('*******************', loss,pre_value,auc_value)

            if auc_value>max_auc:
                max_auc=auc_value
                saver.save(sess, './tf_model/dota2model.ckpt')
