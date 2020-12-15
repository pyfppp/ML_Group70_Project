import pandas
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA


# get details of food in different files and make prediction about the probability of obesity

# fill N/A
# give a constant when there is a range of value
def get_features(file):
    obesity = file['Obesity']
    features = file.iloc[:, 1:24]
    # print(len(obesity.dropna())/len(obesity)) 98%, we do not need to drop those features with N/A
    obesity.fillna(obesity.mean(), inplace=True)
    return features, obesity


def get_training_data():
    file_fat_kal = pandas.read_csv("Food_Supply_kcal_Data.csv")
    file_protein_supply = pandas.read_csv("Protein_Supply_Quantity_Data.csv")
    file_fat_quantity = pandas.read_csv("Fat_Supply_Quantity_Data.csv")
    x, y = get_features(file_fat_kal)
    return x, y


def get_KFold(x, y, model_type: str):
    k_list = [2, 4, 6, 8, 10, 20, 40]
    x = np.array(x)
    y = np.array(y).reshape(-1, 1)
    poly = PolynomialFeatures(degree=3)
    x_ = poly.fit_transform(x)
    score_list = []
    train_error_mse = []
    test_error_mse = []
    train_error_std = []
    test_error_std = []
    for k in k_list:
        kf = KFold(n_splits=k)
        temp_train = []
        temp_test = []
        if model_type == 'linear_regression':
            model = LinearRegression()
        elif model_type == 'random_forrest':
            model = RandomForestRegressor()
        elif model_type == 'ridge':
            model = Ridge()
        for train, test in kf.split(x_):
            model.fit(x_[train], y[train])
            temp_train.append(mean_squared_error(y[train], model.predict(x_[train])))
            temp_test.append(mean_squared_error(y[test], model.predict(x_[test])))
        score_list.append(model.score(x_, y))
        train_error_mse.append(np.array(temp_train).mean())
        test_error_mse.append(np.array(temp_test).mean())
        train_error_std.append(np.array(temp_train).std())
        test_error_std.append(np.array(temp_test).std())
    plot_mse_and_score(score_list, train_error_std, test_error_std, train_error_mse, test_error_mse, degree_list,
                       model_type, 'poly degree')


def get_poly(x, y, model_type: str):
    kf = KFold(n_splits=10)
    degree_list = [2, 3, 4, 5, 6]
    x = np.array(x)
    y = np.array(y).reshape(-1, 1)
    score_list = []
    train_error_mse = []
    test_error_mse = []
    train_error_std = []
    test_error_std = []
    for poly_degree in degree_list:
        temp_train = []
        temp_test = []
        if model_type == 'linear_regression':
            model = LinearRegression()
        elif model_type == 'random_forrest':
            model = RandomForestRegressor()
        elif model_type == 'ridge':
            model = Ridge()
        poly = PolynomialFeatures(degree=poly_degree)
        x_ = poly.fit_transform(x)
        for train, test in kf.split(x_):
            model.fit(x_[train], y[train])
            temp_train.append(mean_squared_error(y[train], model.predict(x_[train])))
            temp_test.append(mean_squared_error(y[test], model.predict(x_[test])))
        score_list.append(model.score(x_, y))
        train_error_mse.append(np.array(temp_train).mean())
        test_error_mse.append(np.array(temp_test).mean())
        train_error_std.append(np.array(temp_train).std())
        test_error_std.append(np.array(temp_test).std())
    plot_mse_and_score(score_list, train_error_std, test_error_std, train_error_mse, test_error_mse, degree_list,
                       model_type, 'poly degree')


def plot_mse_and_score(score_list, train_error_std, test_error_std, train_error_mean, test_error_mean, x_list,
                       model_type, x_list_name):
    axs1 = plt.subplot(211)
    plt.errorbar(x_list, train_error_mean, yerr=train_error_std, label='train_mse')
    plt.errorbar(x_list, test_error_mean, yerr=test_error_std, label='test_mse')
    plt.title(model_type + 'Error VS ' + x_list_name)
    plt.xlabel(x_list_name)
    plt.ylabel('error')
    plt.legend()
    axs2 = plt.subplot(212)
    plt.plot(x_list, score_list, marker='o')
    plt.xlabel(x_list_name)
    plt.ylabel('score')
    plt.title('score in different' + x_list_name)
    plt.show()


def get_prediction(x, y):
    lr = LinearRegression()
    kf = KFold(n_splits=10)
    poly = PolynomialFeatures(degree=3)
    x, y = get_training_data()


if __name__ == '__main__':
    model_and_parameters = {"linear_regression": ['polynomial features\' degree', 'Number of KFold'],
                            "ridge": ['max iteration', 'C', 'polynomial features\' degree', 'Number of KFold'],
                            "random_forrest": ['number of trees', 'criterion', 'polynomial features\' degree',
                                               'Number of KFold']}
    print('This is the Group70 week5 assignment')
    file_fat_kal = pandas.read_csv("Food_Supply_kcal_Data.csv")
    file_protein_supply = pandas.read_csv("Protein_Supply_Quantity_Data.csv")
    file_fat_quantity = pandas.read_csv("Fat_Supply_Quantity_Data.csv")
    x, y = get_features(file_fat_kal)
    # print('searching ' + list(model_and_parameters.keys())[0] + ' polynomial features degree ...')
    # get_poly(x, y, list(model_and_parameters.keys())[0])
    print('searching ' + list(model_and_parameters.keys())[0] + ' K in KFold...')
    get_KFold(x, y, list(model_and_parameters.keys())[0])
    # model = get_model(x, y)