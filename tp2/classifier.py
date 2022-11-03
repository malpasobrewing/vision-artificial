import numpy as np

import csv

from joblib import dump
from sklearn import tree
from tp2 import constants


def create_classifier():
    labels, dataset = load_descriptors()
    classifier = tree.DecisionTreeClassifier().fit(dataset, labels)
    tree.plot_tree(classifier)
    dump(classifier, constants.CLASSIFIER_FILE_NAME)

    return classifier


def load_descriptors():
    with open(r'' + constants.DESCRIPTORS_FILE_NAME, 'r') as file_to_read:
        reader = csv.reader(file_to_read, delimiter=',')

        dataset = []
        labels = []

        for line in reader:
            hu_moments = []
            for moment in line[1:len(line)]:
                hu_moments.append(float(moment))
            dataset.append(np.array(hu_moments, dtype=np.float32))
            labels.append(np.array([float(line[0])], dtype=np.int32))

        # for line in reader:
        #     labels.append(get_label_id(line[0]))
        #     dataset.append(line[1:len(line)])

        return labels, dataset


def get_label_id(val):
    return val.split('.')[0]


if __name__ == '__main__':
    create_classifier()

