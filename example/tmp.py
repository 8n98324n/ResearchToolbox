import rpy2.robjects as robjects
from rpy2.robjects import r, StrVector, ListVector, DataFrame

rpy2_setup_code = '''
library(RHRV)
suppressPackageStartupMessages(library(dplyr))
'''
robjects.r(rpy2_setup_code)