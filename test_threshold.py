__author__ = 'shen'
import numpy as np
import draw_roc
import threshold_data

hypothesis_array = np.array([0.1, 0.8, 0.5, 0.2, 0.9, 0.7, 0.9, 0.1, 0.04, 0.98,
                             0.6, 0.6, 0.6, 0.2, 0.5, 0.4, 0.7, 0.65, 0.65, 0.58,
                             0.47, 0.48, 0.49, 0.51, 0.53, 0.54, 0.55, 0.68, 0.58, 0.59,
                             0.96, 0.95, 0.94, 0.93, 0.84, 0.82, 0.81, 0.62, 0.75, 0.88,
                             0.14, 0.15, 0.24, 0.26, 0.24, 0.38, 0.34, 0.21, 0.22, 0.11])

given_label_array = np.array([1,3,2,1,3,3,3,1,1,3,
                            2,2,2,1,2,1,3,2,2,2,
                            2,1,2,1,2,2,2,3,3,2,
                            3,3,3,2,3,2,3,2,3,3,
                            1,1,1,2,1,1,1,2,1,1])

print "hypothesis_array"
print hypothesis_array
print "given_label_array"
print given_label_array
target_label = 2
legend = ["threshold"]
Roc_array = threshold_data.threshhold_changed_roc_array(hypothesis_array, given_label_array, target_label, flag=0)
print "Roc_array"
print Roc_array
draw_roc.draw_roc(Roc_array, legend, measure="number", xpattern="normal", ypattern="normal")

