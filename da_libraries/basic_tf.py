import tensorflow as tf

a = tf.Variable([1, 2, 3])
b = tf.Variable([4, 5, 6])

b.assign_sub(a)

print(b)

