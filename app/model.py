import pickle
# import numpy as np

class model():
    def __init__(self) -> None:
        self.model_ = None
        self.preprocess_ = None

    def load(self):
        self.model_ = pickle.load(open( 'app/model', 'rb'))
        self.preprocess_ = pickle.load(open('app/scale','rb'))

    def predict(self,X):
        if self.model_:
            X = self.preprocess_.transform(X)
            return self.model_.predict(X)
        else:
            raise Exception('Model is not properly loaded.')


# if __name__ == '__main__':
#     # test = model()
#     # test.load()

#     # Test_case_1 = np.array([337,118,4,4.5,4.5,9.65,1])
#     # Test_case_2 = np.array([290,100,1,1.5,2,7.56,0])
    
#     # test = model()
#     # test.load()

#     # Test_case_1 = np.array([337,118,4,4.5,4.5,9.65,1])
    
#     # test.predict(Test_case_1.reshape(1,-1))
#     # # Result will be 3
#     Test_case_2 = np.array([290,100,1,1.5,2,7.56,0])



#     Scale = pickle.load(open("prediction/app/scale", "rb"))
#     Model = pickle.load(open("prediction/app/model", "rb"))
#     test1 = np.array([290,100,1,1,2,7.56,0])
#     print(Model.predict(Scale.transform(test1.reshape(1,-1))))
#     # Result will be 2
    
