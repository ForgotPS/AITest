#encoding=utf-8
import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

matrix1 = tf.constant([[2],[2]])
matrix2 = tf.constant([[3,3]])
output = tf.matmul(matrix2, matrix1)

with tf.Session() as sess:
    result = sess.run(output)
    print(result)