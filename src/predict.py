from keras.models import load_model
from sklearn import metrics

from preprocess import preprocesser
import numpy as np

pre = preprocesser()
model = load_model("../result/CNN_model1.h5")
print(model.summary())
testingSet_path = "../result/training_sample1.txt"
x_test = pre.word2idx2(testingSet_path, max_length=600)
predict = model.predict(x_test)
list1 = []
categories = ["体育", "财经", "房产", "家居", "教育", "科技", "时尚", "时政", "游戏", "娱乐"]
num_py = np.array(predict)
for i in range(len(predict)):
    max1 = predict[i][0]
    index = 0
    for j in range(len(predict[0])):
        if predict[i][j] > max1:
            max1 = predict[i][j]
            index = j
    list1.append(index)
for val in list1:
    print(categories[val])
