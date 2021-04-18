import numpy as np
import pandas as pd

def read(file):
    try:
        data = pd.read_csv(file, sep = '\s+', header = None, names = [i for i in range(1,25)])
        return data
    
    except: return None


def reindex(data):
    data.index = [i for i in range(len(data))]


def mean_at_10hz(data, stride = 1):
    dict_data = dict()
    length = len(data)
    features = len(data.columns)
    
    for feature in range(features):      
        mean_list = []
        arr = data.iloc[:,feature].values
        for i in range(0, length, stride):
            
            if i+10 > length or (stride == 10 and length == i+10):
                mean_list.append(float(np.mean(arr[i:length])))
                dict_data[feature] = mean_list
                print(feature, 'col has been finished')
                print('size of',feature,'col :',len(mean_list))
                break
            mean_list.append(float(np.mean(arr[i:i+10])))
    return dict_data


def std_at_10hz(data, stride = 1):
    dict_data = dict()
    length = len(data)
    features = len(data.columns)
    for feature in range(features):        
        std_list = []
        arr = data.iloc[:,feature].values
        for i in range(0, length, stride):
            if i+10 > length or (stride == 10 and length == i+10):
                std_list.append(float(np.std(arr[i:length])))
                dict_data[feature] = std_list
                print(feature, 'col has been finished')
                print('size of',feature,'col :',len(std_list))
                break
            std_list.append(float(np.std(arr[i:i+10])))
    return dict_data

def max_at_10hz(data, stride = 1):
    dict_data = dict()
    length = len(data)
    features = len(data.columns)
    for feature in range(features):        
        max_list = []
        arr = data.iloc[:,feature].values
        for i in range(0, length, stride):
            if i+10 > length or (stride == 10 and length == i+10):
                max_list.append(float(arr[i:length].max()))
                dict_data[feature] = max_list
                print(feature, 'col has been finished')
                print('size of',feature,'col :',len(max_list))
                break
            max_list.append(float(arr[i:i+10].max()))
    return dict_data

def min_at_10hz(data, stride = 1):
    dict_data = dict()
    length = len(data)
    features = len(data.columns)
    for feature in range(features):        
        min_list = []
        arr = data.iloc[:,feature].values
        for i in range(0, length, stride):
            if i+10 > length or (stride == 10 and length == i+10):
                min_list.append(float(arr[i:length].min()))
                dict_data[feature] = min_list
                print(feature, 'col has been finished')
                print('size of',feature,'col :',len(min_list))
                break
            min_list.append(float(arr[i:i+10].min()))
    return dict_data

def median_at_10hz(data, stride = 1):
    dict_data = dict()
    length = len(data)
    features = len(data.columns)
    for feature in range(features):        
        median_list = []
        arr = data.iloc[:,feature].values
        for i in range(0, length, stride):
            if i+10 > length or (stride == 10 and length == i+10):
                median_list.append(float(np.median(arr[i:length])))
                dict_data[feature] = median_list
                print(feature, 'col has been finished')
                print('size of',feature,'col :',len(median_list))
                break
            median_list.append(float(np.median(arr[i:i+10])))
    return dict_data

def mad_at_10hz(data, stride = 1):
    dict_data = dict()
    length = len(data)
    features = len(data.columns)
    for feature in range(features):        
        mad_list = []
        arr = data.iloc[:,feature].values
        for i in range(0, length, stride):
            if i+10 > length or (stride == 10 and length == i+10):
                mad_list.append(float(np.median(np.absolute(arr[i:length] - np.median(arr[i:length])))))
                dict_data[feature] = mad_list
                print(feature, 'col has been finished')
                print('size of',feature,'col :',len(mad_list))
                break
            mad_list.append(float(np.median(np.absolute(arr[i:10] - np.median(arr[i:10])))))
    return dict_data

def entropy_at_10hz(data, stride = 1):
    dict_data = dict()
    length = len(data)
    features = len(data.columns)
    for feature in range(features):        
        etr_list = []
        arr = data.iloc[:,feature].values
        for i in range(0, length, stride):
            if i+10 > length or (stride == 10 and length == i+10):
                p = (arr[i:length] / arr[i:length].sum()) +1e-10
                etr = -((p*np.log2(p)).sum())
                etr_list.append(float(etr))
                dict_data[feature] = etr_list
                print(feature, 'col has been finished')
                print('size of',feature,'col :',len(etr_list))
                break
            p = (arr[i:i+10] / arr[i:i+10].sum()) +1e-10
            etr = -((p*np.log2(p)).sum())
            etr_list.append(float(etr))
    return dict_data

def magnitude(data):
    dict_data = dict()
    _data = data.drop([4,5,24],axis = 1)
    clength = len(_data.columns)
    rlength = len(_data)
    _data.columns = [i for i in range(clength)]
    
    for i in range(0,clength,3):
        mag_list = []
        for j in range(rlength):
            vectors = _data.iloc[j,i:i+3].values
            mag_list.append(float(np.linalg.norm(vectors)))
            if j == rlength -1 : 
                dict_data[i] = mag_list
                print('finished')
    return dict_data
