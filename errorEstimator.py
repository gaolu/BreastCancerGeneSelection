from classRules import *
class errorEstimator:
    def resubstitution(self, classRule, trainLabel, trainData, featureData):
        # myClassRule = classRules()
        # print 'in resubstituition'
        # print featureData
        predictRet = classRule(trainLabel, featureData, featureData)
        # print predictRet
        # print type(predictRet), len(predictRet), predictRet[0]
        error = 0
        for i in range(len(predictRet)):
            error = error + abs(int(predictRet[i]) - int(trainLabel[i]))
        jValue = 1 - 1.0 / len(predictRet) * error
        return jValue
    
    def looCrossVal(self, classRule, trainLabel, trainData, featureData):
        print 'in loo cross validation'
        # k = len(featureData)
        error = 0
        transformedFeatureData = []
        for i in range(len(trainLabel)):
            newTuple = []
            for j in range(len(featureData)):
                newTuple.append(featureData[j][i])
            transformdFeatureData.append(newTuple)
        for i in range(len(transformedFeatureData)):
            newTrainData = transformedFeatureData
            del newTrainData[i]
            newTrainLabel = trainLabel
            del newTrainLabel[i]
            predictRet = classRule(newTrainLabel, newTrainLabel, transformedFeatureData[i])
            for ret in predictRet:
                error = error + abs(ret - trainLabel[i])
        jValue = 1 - 1.0 / len(trainLabel) * error
        return jValue