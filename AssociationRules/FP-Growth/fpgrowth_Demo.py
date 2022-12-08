from datetime import datetime
import os
import matplotlib.pyplot as plt
import numpy as np

from apriori import Apriori
from fpgrowth import FPGrowth

def data_reader(data_file):
    data_set = []
    with open(data_file, 'r') as f:
        for line in f:
            data_set.append(line.split()[3:])
    return data_set


def load_data_set():
    """
    Load a sample data set (From Data Mining: Concepts and Techniques, 3th Edition)
    Returns: 
        A data set: A list of transactions. Each transaction contains several items.
    """
    # data_set = [['f','c','a','d','g','i','m','p'],
    #             ['a','b','c','f','l','m','o'],
    #             ['b','f','h','j','o','w'],
    #             ['c','b','k','s','p'],
    #             ['a','f','c','e','l','m','p','n']]
    # data_set = [['l1', 'l2', 'l5'], 
    #             ['l2', 'l4'], ['l2', 'l3'],
    #             ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'],
    #             ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]
    data_set =[['Bread','Milk'],
               ['Bread', 'Diaper', 'Beer', 'Eggs'],
               ['Milk', 'Diaper', 'Beer', 'Coke'],
               ['Bread', 'Milk', 'Diaper', 'Beer'],
               ['Bread', 'Milk', 'Diaper', 'Coke']]
    return data_set                                 ##返回list类别的data_set


def test_apriori(data_set, min_sup = 0.05):
    start = datetime.now()
    apriori = Apriori(data_set)
    apriori.generate_L(min_sup=min_sup)
    deltatime = datetime.now() - start
    time_cost = deltatime.seconds + deltatime.microseconds / 1000000
    print("Apriori over", time_cost)
    print("# of freq itemsets:", len(apriori.freq_itemsets))
    return apriori


def test_fpgrowth(data_set, min_sup=0.05):
    start = datetime.now()
    fp = FPGrowth(data_set, min_sup=min_sup)
    fp.build_fptree()
    deltatime = datetime.now() - start
    time_cost = deltatime.seconds + deltatime.microseconds / 1000000
    print("FP-Growth over",time_cost)
    print("# of freq itemsets:", len(fp.freq_itemsets))
    return fp

def print_freqItems(model):
    for item in model.freq_itemsets:
        print(item)

if __name__ == "__main__":
    """
    Test
    """
    data_set = load_data_set()
    apriori = test_apriori(data_set, min_sup = 0.4)
    print_freqItems(apriori)

    fp = test_fpgrowth(data_set, min_sup=0.4)
    print_freqItems(fp)