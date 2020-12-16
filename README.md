## 1. All the hyper parameters which need be selected manually in each model
- Linear Regression Model
1. Degree of Polynomial features
2. K in KFold
- Ridge Model
1. C
2. Max Iteration
3. degree of polynomial features
4. K in KFold
- Random Forrest Regressor 
1. Number of Trees
2. criterion
3. degree of polynomial features
4. K in KFold
## 2. Data Preprocessing
In the step of data preprocessing, we used `pandas` to implement related functions.
```python
# fill N/A
# give a constant when there is a range of value
def get_features(file):
    obesity = file['Obesity']
    features = file.iloc[:, 1:24]
    # print(len(obesity.dropna())/len(obesity)) 98%, we do not need to drop those features with N/A
    obesity.fillna(obesity.mean(), inplace=True)
    return features, obesity
```
## 3. Project Target
We collected three data sets, which represented three different dimensions to describe multiple countries' people's   
daily food(fat proportion, food kcal proportion and protein proportion), we wanted to find a relatively general pattern,  
which could show which dimension will contribute the most to people's obesity, so that we can create a reference when we try to keep our own health.