import csv
import itertools
from classRules import *
class featureSelection:
    def seqFwdSearch(self, trainFeatureName, trainData, trainFeatureList, trainLabel, totalK, creterionFunc):
        # preserve the original lists
        thisTrainFeatureName = trainFeatureName
        thisTrainFeatureList = trainFeatureList
        myClassRules = classRules()
        featureList = []
        featureNoList = []
        k = 0
        d = len(trainData)
        if totalK > d:
            totalK = d
        roundNo = 1
        while True:
            # print 'this is', roundNo, 'round'
            roundNo = roundNo + 1
            # classRule, trainLabel, trainData, featureData
            # print 'calculating maxJ for the first time'
            # print len(featureList + trainFeatureList[0])
            # currentFeatureList = featureList
            if len(featureList) != 0:
                newFeatureList = []
                for feature in featureList:
                    newFeatureList.append(feature)
                newFeatureList.append(thisTrainFeatureList[0])
                maxJ = creterionFunc(myClassRules.linSVM, trainLabel, trainData, newFeatureList)
            else:
                maxJ = creterionFunc(myClassRules.linSVM, trainLabel, trainData, [thisTrainFeatureList[0]])
            # print len(featureList)
            # print 'maxJ value is:', maxJ
            bestFeatureNo = 0
            featureNo = 0
            for feature in thisTrainFeatureList[1: ]:
                # print feature
                if featureNo in featureNoList:
                    # print 'continue'
                    continue
                # print 'now computing feature number:', featureNo
                if len(featureList) != 0:
                    newFeatureList = []
                    for features in featureList:
                        newFeatureList.append(features)
                    newFeatureList.append(feature)
                    jValue = creterionFunc(myClassRules.linSVM, trainLabel, trainData, newFeatureList)
                else:
                    jValue = creterionFunc(myClassRules.linSVM, trainLabel, trainData, [feature])
                if jValue > maxJ:
                    maxJ = jValue
                    bestFeatureNo = featureNo
                    # print maxJc
                featureNo = featureNo + 1
            featureNoList.append(thisTrainFeatureName[bestFeatureNo])
            featureList.append(thisTrainFeatureList[bestFeatureNo])
            del thisTrainFeatureList[bestFeatureNo]
            del thisTrainFeatureName[bestFeatureNo]
            # print len(thisTrainFeatureList), len(thisTrainFeatureName)
            # print featureNoList, featureList
            if len(featureNoList) == totalK:
                print 1.0 - maxJ
                break
        return featureNoList
        
    #self, trainFeatureName, trainData, trainFeatureList, trainLabel, totalK, creterionFunc
    def exhSearch(self, trainFeatureName, trainData, trainFeatureList, trainLabel, totalK, creterionFunc):
        myClassRules = classRules()
        featureList = []
        featureNoList = []
        n = len(trainFeatureList)
        combinationTuples = self.getCombinations(n, totalK)
        # print len(combinationTuples), type(combinationTuples), type(combinationTuples[0])
        combinationList = [list(i) for i in combinationTuples]
        # print len(combinationList), type(combinationList), type(combinationList[0]), len(combinationList[0]), type(combinationList[0][0])
        # featureNoList = [trainFeatureName[i] for i in combinationList[0]]
        # print featureNoList
        featureNoList = combinationList[0]
        featureList = [trainFeatureList[featureNo] for featureNo in featureNoList]
        maxJ = creterionFunc(myClassRules.linSVM, trainLabel, trainData, featureList)
        # print maxJ
        for combination in combinationList[1 : ]:
            featureList = [trainFeatureList[featureNo] for featureNo in combination]
            jValue = creterionFunc(myClassRules.linSVM, trainLabel, trainData, featureList)
            if jValue > maxJ:
                featureNoList = combination
                maxJ = jValue
        featureNameList = [trainFeatureName[i] for i in featureNoList]  
        print 1.0 - maxJ  
        return featureNameList
    
    def getCombinations(self, n, totalK):
        return list(itertools.combinations(range(n), totalK))
    
    def loadData(self, fileName):
        data = []
        labels = []
        dataID = []
        featureName = []
        featureDict = []
        with open(fileName, 'r') as file:
            rowNum = 0
            for line in file:
                dataList = line.split()
                if rowNum != 0:
                    dataID.append(dataList[0])
                    data.append([float(x) for x in dataList[1 : len(dataList) - 1]])
                    labels.append(dataList[-1])
                else:
                    featureName = dataList[1 : len(dataList) - 1]
                rowNum = rowNum + 1
        
        featureNo = 0        
        for feature in featureName:
            featureData = []
            for sample in data:
                featureData.append(sample[featureNo])
            featureDict.append(featureData)
            featureNo = featureNo + 1
        # print len(featureDict)
#         print featureDict[0]
#         print featureDict[-1]
        
        return dataID, data, labels, featureName, featureDict
    
    # def simple_crit_func(self, feat_sub):
    #     """ Returns sum of numerical values of an input list. """ 
    #     return sum(feat_sub)
    # 
    # def seq_forw_select(self, features, max_k, criterion_func, print_steps=False):
    #     """
    #     Implementation of a Sequential Forward Selection algorithm.
    # 
    #     Keyword Arguments:
    #         features (list): The feature space as a list of features.
    #         max_k: Termination criterion; the size of the returned feature subset.
    #         criterion_func (function): Function that is used to evaluate the
    #             performance of the feature subset.
    #         print_steps (bool): Prints the algorithm procedure if True.
    # 
    #     Returns the selected feature subset, a list of features of length max_k.
    # 
    #     """
    # 
    #     # Initialization
    #     feat_sub = []
    #     k = 0
    #     d = len(features)
    #     if max_k > d:
    #         max_k = d
    # 
    #     while True:
    #     
    #         # Inclusion step
    #         if print_steps:
    #             print('\nInclusion from feature space', features)
    #         crit_func_max = criterion_func(feat_sub + [features[0]])
    #         best_feat = features[0]
    #         for x in features[1:]:
    #             crit_func_eval = criterion_func(feat_sub + [x])
    #             if crit_func_eval > crit_func_max:
    #                 crit_func_max = crit_func_eval
    #                 best_feat = x
    #         feat_sub.append(best_feat)
    #         if print_steps:
    #             print('include: {} -> feature subset: {}'.format(best_feat, feat_sub))
    #         features.remove(best_feat)
    #     
    #         # Termination condition
    #         k = len(feat_sub)
    #         if k == max_k:
    #             break
    #             
    #     return feat_sub