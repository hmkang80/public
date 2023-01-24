# class A:

#     def __init__(self):
#         print("I was born")
#         self.x = 0

#     def party(self):
#         self.x = self.x+1
#         return f"total count is {self.x}"
    
#     def __del__(self):
#         print("I was destucted")


# a = A()
# print(a.party())
# print(a.party())
# print(a.party())
# a=100

import tensorflow as tf



# Data
x_data = [1,2,3,4,5]
y_data = [3,5,7,9,11]

# W, b initiate
W = tf.Variable(2.9)
b = tf.Variable(0.5)

learning_rate = 0.01

for i in range(10000):
    # Gradient descent
    with tf.GradientTape() as tape:
        hypothesis = W * x_data + b
        cost = tf.reduce_mean(tf.square(y_data - hypothesis))
    W_grad, b_grad = tape.gradient(cost, [W, b])
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)
    if i % 1000 == 0:
        print(f"{i:5}|{W.numpy():10.4f}|{b.numpy():10.4f}|{cost:10.6f}")