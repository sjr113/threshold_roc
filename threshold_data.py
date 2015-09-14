__author__ = 'shen'

import numpy as np


def threshhold_changed_roc_array(hypothesis_array, given_label_array, target_label, flag=0):
    argsort_array = np.argsort(hypothesis_array)
    sort_hypothesis = hypothesis_array[argsort_array]
    sort_given_label = given_label_array[argsort_array]
    threshold_array = []
    sample_num = (np.shape(hypothesis_array))[0]  # the number of sample
    if target_label not in given_label_array:
        print "Error"
        return None
    else:
        pass
    for i in range(sample_num):
        if sort_given_label[i] == target_label:
            threshold_array.append(sort_hypothesis[i])
    threshold_array = np.array(threshold_array)
    threshold_array = np.unique(threshold_array)
    if flag != 1 and flag != 0:
        flag = 0
    threshold_Roc_array = []
    dict_threshold = {}
    # print refer_threshold
    if flag == 0:
        refer_threshold = threshold_array[0]
        for thresh_value in threshold_array:
            true_positive = 0
            false_positive = 0
            false_negtive = 0
            true_negtive = 0
            for i in range(sample_num):
                if hypothesis_array[i] <= thresh_value and hypothesis_array[i] > refer_threshold:
                    if given_label_array[i] == target_label:
                        true_positive += 1
                    else:
                        false_positive += 1
                # elif hypothesis_array[i] >= refer_threshold:
                else:
                    if given_label_array[i] == target_label:
                        false_negtive += 1
                    else:
                        true_negtive += 1
            dict_threshold[("threshold="+str(thresh_value))] = [true_positive, false_positive, false_negtive, true_negtive]
        threshold_Roc_array.append(dict_threshold)
    else:
        threshold_array = threshold_array[::-1]
        refer_threshold = threshold_array[0]
        print threshold_array[0]
        print threshold_array
        for thresh_value in threshold_array:
            true_positive = 0
            false_positive = 0
            false_negtive = 0
            true_negtive = 0
            for i in range(sample_num):
                if hypothesis_array[i]>=thresh_value and hypothesis_array[i] < refer_threshold:
                    if given_label_array[i] == target_label:
                        true_positive += 1
                    else:
                        false_positive += 1
                else:
                    if given_label_array[i] == target_label:
                        false_negtive += 1
                    else:
                        true_negtive += 1
            dict_threshold[("threshold="+str(thresh_value))] = [true_positive, false_positive, false_negtive, true_negtive]
        threshold_Roc_array.append(dict_threshold)
    return threshold_Roc_array

