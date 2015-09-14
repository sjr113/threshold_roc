__author__ = 'shen'

import matplotlib.pyplot as plt
from numpy import *


def label_pattern(pattern, parray):
    if pattern == "normal":
        return parray
    elif pattern == "log":
        return log(parray + 1e-6)
    else:
        print "Your parameter " + pattern + "does not exist!"
        return 0


def draw_roc(roc_data_list, legend, measure="rate", xpattern="log", ypattern="normal"):
    RoC_array = []
    for element in roc_data_list:
        arrar_temp = []
        for values in element.values():
            arrar_temp.append(values)
        RoC_array.append(arrar_temp)
    RoC_array = array(RoC_array)

# Accuracy : the proportion of true result among the total number of cases examined
# accuracy = (true_positive + true_negatives)/(true_positive + false_positive + false_negatives + true_negatives)
# accuracy_array = (RoC_array[0, :, i] + RoC_array[3, :, i])/(RoC_array[0, :, i] + RoC_array[1, :, i]
#  + RoC_array[2, :, i] + RoC_array[3, :, i])
# Precision : the proportion of the true positive against all the positive results
# precision = true_positive/(true_positive + false_positive)
# Recall : the proportion of the true positives against the true positives and false negatives
# recall = true_positive/(true_positive + false_negatives)
# recall_array = RoC_array[0, :, i]/(RoC_array[0, :, i] + RoC_array[2, :, i])
# False Alarm rate (False positive ): the proportion of the false positive against the false positives
# false_alarm_rate = false_positive/(false_positive + true_negatives)

    line_style = ["r--", "g^-", "bo-", "k--", "rs-", "ko-", "r^-"]
    line_width = [1, 1.5, 2, 2.5, 3, 3.5, 4]
    num = len(line_style)
    plt.figure(1)
    i = 0
# print shape(RoC_array)

    if measure == "rate":
        while i < (shape(RoC_array))[0]:
            roc_data = array(RoC_array[i])
            recall_array = (roc_data[:, 0]*1.0)/(roc_data[:, 0] + roc_data[:, 2] + 1e-6)
            false_alarm_rate_array = (roc_data[:, 1]*1.0)/(roc_data[:, 1] + roc_data[:, 3] + 1e-6)
            argsort_array = argsort(recall_array)
            a1 = false_alarm_rate_array[argsort_array]
            a2 = recall_array[argsort_array]
            argsort_array = argsort(a1)
            plt.plot(label_pattern(xpattern, a1[argsort_array]), label_pattern(ypattern, a2[argsort_array]), line_style[mod(i, num)], linewidth=line_width[mod(i, num)])
            i += 1
    elif measure == "number":
        while i < (shape(RoC_array))[0]:
            roc_data = array(RoC_array[i])
            # roc_data[:,0][1] = 12
            # roc_data[:,0][5] = 1.2
            argsort_array = argsort(roc_data[:, 0])
            a1 = (roc_data[:, 1])[argsort_array]
            a2 = (roc_data[:, 0])[argsort_array]
            argsort_array = argsort(a1)
            plt.plot(label_pattern(xpattern, a1[argsort_array]), label_pattern(ypattern, a2[argsort_array]), line_style[mod(i, num)], linewidth=line_width[mod(i, num)])
            i += 1
    elif measure == "log":
        while i < (shape(RoC_array))[0]:
            roc_data = array(RoC_array[i])
            argsort_array = argsort(roc_data[:, 0])
            a1 = (roc_data[:, 1])[argsort_array]
            a2 = (roc_data[:, 0])[argsort_array]
            argsort_array = argsort(a1)
            plt.plot(label_pattern(xpattern, log(a1[argsort_array] + 1e-6)), label_pattern(ypattern, log(a2[argsort_array] + 1e-6)), line_style[mod(i, num)], linewidth=line_width[mod(i, num)])
            i += 1
    xlabel = "False_positive_" + measure + "_" + xpattern
    plt.xlabel(xlabel)
    ylabel = "True_positive_" + measure + "_" + ypattern
    plt.ylabel(ylabel)
    plt.legend(legend)
    plt.title("RoC Curve")
# plt.text(2, 0.65, "RoC Lines")
    plt.show()


