import tensorflow as tf
# tf.constant是一个计算，计算结果是一个张量，保存在变量a或者b中。
a = tf.constant([[1.0, 2.0]], name="a")
b = tf.constant([[3.0], [4.0]], name="b")
# 将a和b进行相加，相加后名字为"multiply"
result = tf.matmul(a, b, name = "multiply")
# 输出
print(result)
# 创建一个会话，通过Python上下文管理器来管理该会话
# 启动默认图表
with tf.Session() as sess:
    print("a = [[1.0, 2.0]], b = [[3.0], [4.0]]")
    print("两个向量相加: a * b = ", sess.run(result))
    # 将数据写到日志中
    summary_writer = tf.summary.FileWriter("log", sess.graph)
