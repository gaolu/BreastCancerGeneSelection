from featureSelection import *
from errorEstimator import *
def main():
    myFeatureSel = featureSelection()
    fileName = 'Training_Data.txt'
    trainName, trainData, trainLabel, trainFeatureName, trainFeatureList = myFeatureSel.loadData(fileName)
    fileName = 'Testing_Data.txt'
    testName, testData, testLabel, testFeatureName, testFeatureList = myFeatureSel.loadData(fileName)
    
    myErrorEstimator = errorEstimator()
    totalK = 3
    # featureNameList = myFeatureSel.seqFwdSearch(trainFeatureName, trainData, trainFeatureList, trainLabel, totalK, myErrorEstimator.resubstitution)
    # print featureNameList
    
    # featureNameList = myFeatureSel.seqFwdSearch(trainFeatureName, trainData, trainFeatureList, trainLabel, totalK, myErrorEstimator.looCrossVal)
    # print featureNameList

    # featureNameList = myFeatureSel.exhSearch(trainFeatureName, trainData, trainFeatureList, trainLabel, totalK, myErrorEstimator.resubstitution)
    # print featureNameList
    
    featureNameList = myFeatureSel.exhSearch(trainFeatureName, trainData, trainFeatureList, trainLabel, totalK, myErrorEstimator.looCrossVal)
    print featureNameList
    # ex_features = [6, 3, 1, 6, 8, 2, 3, 7, 9, 1]
#     res_forw = myFeatureSel.seq_forw_select(features=ex_features, max_k=3, criterion_func=myFeatureSel.simple_crit_func, print_steps=True) 
#     print res_forw
    
    
    

# start from main()
if __name__ == "__main__":
    main()