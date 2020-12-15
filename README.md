#ML_Group70_Project
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