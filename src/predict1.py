from keras.models import load_model
# import numpy as np

from src.preprocess import preprocesser


class Predict:
    model = load_model("../result/CNN_model1.h5")
    pre = preprocesser()
    testingSet_path = "../data/cnews.simple1.txt"
    list1 = []
    categories = ['财经', '房产', '教育', '科技', '军事', '汽车', '体育', '游戏', '娱乐', '其他']

    def update1(self):
        x_test = self.pre.word2idx2(self.testingSet_path, max_length=600)
        predict = self.model.predict(x_test)

        # num_py = np.array(predict)
        for i in range(len(predict)):
            max1 = predict[i][0]
            index = 0
            for j in range(len(predict[0])):
                if predict[i][j] > max1:
                    max1 = predict[i][j]
                    index = j
            self.list1.append(index)

    def predict(self):
        self.update1()
        res = ''
        head = '\''
        i = 0
        for val in self.list1:
            ans = i+1
            res = res+"\"" + str(ans) + "\":"+"\"" + self.categories[val] + "\","
        self.list1.clear()
        res1 = res[0:len(res)-1]
        res1 = '{' + res1 + '}'
        self.list1.clear()
        return res1
