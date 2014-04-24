from classRules import *
class errorEstimator:
    def resubstitution(self, classRule, trainLabel, trainData, featureData):
        # myClassRule = classRules()
        # print 'in resubstituition'
        # print featureData
        print len(featureData)
        predictRet = classRule(trainLabel, self.transMat(featureData), featureData)
        # print predictRet
        # print type(predictRet), len(predictRet), predictRet[0]
        error = 0
        for i in range(len(predictRet)):
            error = error + abs(int(predictRet[i]) - int(trainLabel[i]))
        jValue = 1 - 1.0 / len(predictRet) * error
        return jValue
    
    def looCrossVal(self, classRule, trainLabel, trainData, featureData):
        print 'in loo cross validation'
        print 'the length of featureData is:', len(featureData)
        # k = len(featureData)
        error = 0
        transformedFeatureData = self.transMat(featureData)
        # print 'transfored feature data is:'
        print transformedFeatureData
        # print 'the length of the transformed feature data is:', len(transformedFeatureData)
        # transform the data matrix
        # for i in range(len(trainLabel)):
#             newTuple = []
#             print 'i is:', i
#             print len(featureData)
#             for j in range(len(featureData)):
#                 print 'j is:', j
#                 print len(featureData[j])
#                 newTuple.append(featureData[j][i])
#             transformdFeatureData.append(newTuple)
        for i in range(len(transformedFeatureData)):
            print 'the sample to be left is:', i
            # newTrainData = transformedFeatureData
#             del newTrainData[i]
#             newTrainLabel = trainLabel
#             del newTrainLabel[i]
            newTrainLabel = []
            newTrainData = []
            for j in range(len(trainLabel)):
                if j == i:
                    continue
                newTrainLabel.append(trainLabel[j])
            for j in range(len(transformedFeatureData)):
                if j == i:
                    continue
                newTrainData.append(transformedFeatureData[j])
            print len(newTrainLabel[0]), len(newTrainData[0])
            predictRet = classRule(newTrainLabel, newTrainData, transformedFeatureData[i])
            for ret in predictRet:
                error = error + abs(int(ret) - int(trainLabel[i]))
        jValue = 1 - 1.0 / len(trainLabel) * error
        return jValue
        
    def transMat(self, inputMat):
        rowNum = len(inputMat[0])
        colNum = len(inputMat)
        outputMat = []
        for row in range(rowNum): # rowNum=60
            newTuple = []
            for col in range(colNum): # colNum = 1-5
                newTuple.append(inputMat[col][row])
            outputMat.append(newTuple)
        return outputMat
                
        