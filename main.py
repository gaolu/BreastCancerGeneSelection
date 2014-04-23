from featureSelection import *
from errorEstimator import *
def main():
    myFeatureSel = featureSelection()
    fileName = 'Training_Data.txt'
    trainName, trainData, trainLabel, trainFeatureName, trainFeatureDict = myFeatureSel.loadData(fileName)
    fileName = 'Testing_Data.txt'
    testName, testData, testLabel, testFeatureName, testFeatureDict = myFeatureSel.loadData(fileName)
    
    myErrorEstimator = errorEstimator()
    
    # ex_features = [6, 3, 1, 6, 8, 2, 3, 7, 9, 1]
#     res_forw = myFeatureSel.seq_forw_select(features=ex_features, max_k=3, criterion_func=myFeatureSel.simple_crit_func, print_steps=True) 
#     print res_forw
    
    
    

# start from main()
if __name__ == "__main__":
    main()