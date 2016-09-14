import csv as csv
import matplotlib as plt
import numpy as np
import pandas as pd

training_file_object = csv.reader(open('../data/train.csv'))
test_file_object = csv.reader(open('../data/test.csv'))

training_header = next(training_file_object)
training_data = list(training_file_object)

test_header = next(test_file_object)
test_data = list(test_file_object)

training_data = np.array(training_data)

number_passengers = np.size(training_data[0::,1].astype(np.float))
number_survived = np.sum(training_data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers
