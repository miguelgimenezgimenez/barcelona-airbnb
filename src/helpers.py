import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

sns.set(rc={'figure.figsize':(18,12)})


checkPValue = lambda p,threshold=0.05: "--> Null(H0) hypotesis rejected" if p < threshold else "--> We cannot reject the null hypotesis"
from scipy.stats import t,ttest_1samp

def get_pvalue(item):

    neighbourhood_group_mean = neighbourhood_group_description[(neighbourhood_group_description['neighbourhood_group']==item.neighbourhood_group[0])
                                             & (neighbourhood_group_description['room_type']=="Entire home/apt")]['price']['mean']
    
   
    sample =  nyc_abnb[(nyc_abnb['neighbourhood']==item.neighbourhood[0]) 
             & (nyc_abnb['room_type']=="Entire home/apt") ]
    
    f,pval = ttest_1samp(sample['price'] ,neighbourhood_group_mean)

    return pval[0]



class PDF(object):
    def __init__(self, pdf, size=(200,200)):
        self.pdf = pdf
        self.size = size

    def _repr_html_(self):
        return '<iframe src={0} width={1[0]} height={1[1]}></iframe>'.format(self.pdf, self.size)

    def _repr_latex_(self):
        return r'\includegraphics[width=1.0\textwidth]{{{0}}}'.format(self.pdf)