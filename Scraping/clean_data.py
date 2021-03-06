# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 04:25:22 2020

@author: Doaa
"""
## import libs
import pandas as pd
import re
import numpy as np
from langdetect import detect

## extract ratting number google
def ratting_google(df, col):
    df[col]=df.rattings.str.extract('(\d+)')
    df[col]= df[col].astype(float)
    
    return(df.head())

### check Ar, En lang

def define_lang(df,col):
    df['lang']=''
    for i in range(len(df)):
        try:
                if detect(df[col][i]) == 'ar':
                        df['lang'][i]= detect(df[col][i])
                elif detect(df[col][i])=='en':
                            df['lang'][i]= detect(df[col][i])
        except:
                pass
    return(df['lang'].unique())  
## extract ratting number appal

def ratting(df,col):
    df[col]=df[col].str[0]
    df[col]= df[col].astype(float)
    return (df.head())
    
def ratting_class(df, col):
    df['ratting_class']=''
    df.loc[df[col] <= 3, 'ratting_class'] = 'Bad' 
    df.loc[df[col] == 4, 'ratting_class'] = 'moderate' 
    df.loc[df[col] == 5, 'ratting_class'] = 'good' 
    return(df.head())    
        
