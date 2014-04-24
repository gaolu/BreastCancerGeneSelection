class classRules:
    # trainLabel is the label of the training data
    # featureData is the list of training data
    # testData is the list of testing data
    # training and testing data share the same label list
    # for example, trainLabel=[1, 0, 1, 0, ..., 1, 0]
    # featureData = [[data00, data01], [data10, data11], ..., [dataN0, dataN1]]
    # testData = [[data00, data01], [data10, data11], ..., [dataN0, dataN1]]
    # the number of trainLabel in the list equals to the number of data in the data list
    # each set of data corresponds to each label in the same index
    
    
    def DLDA(self, trainLabel, featureData, testData):
        return trainLabel
    
    def kNN(self, trainLabel, featureData, testData):
        return trainLabel
    
    def linSVM(self, trainLabel, featureData, testData):
        return trainLabel