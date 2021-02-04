import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV,Lasso
import pandas as pd
from sklearn import svm
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import BaggingRegressor
import xgboost as xgb
import matplotlib.pyplot as plt
import warnings
import os
warnings.filterwarnings("ignore")
import xlwt

#print(os.getcwd())
os.chdir('/Users/siming/Desktop/Columbia Courses /2020Fall/2 Business Analytics/GroupProject/yelp_dataset/Predictive Analysis')
dt = pd.read_csv('t1.csv',na_values='NONE')
dt

dt.shape
pd.set_option('display.width',None)
pd.set_option('display.max_rows', None)


###############################Model Part###############################
m,n=np.shape(dt)     
label_col=['reviews']
#drop_col=['id','neighbourhood_cleansed','neighbourhood_group_cleansed']   
# 'id','neighbourhood_cleansed','neighbourhood_group_cleansed'

feature_cols=[col for col in dt.columns if not col in label_col]
X=dt[feature_cols]
Y=dt[label_col]
X=np.array(X)
Y=np.array(Y)


# Loss Function Definition
def rmse_cv(model):
    rmse= np.sqrt(-cross_val_score(model, X, Y, 
                                   scoring="neg_mean_squared_error", cv = 10))
    return(rmse)

#Lasso Linear Regression
model_lasso = Lasso()
alphas = np.arange(10,20,1)
cv_lasso = [rmse_cv(Lasso(alpha = alpha)).mean() 
            for alpha in alphas]

cv_lasso = pd.Series(cv_lasso, index = alphas)
cv_lasso.plot(title = "Validation")
plt.xlabel("alpha")
plt.ylabel("rmse")
cv_lasso.min()  
cv_lasso

#####################XGBoost#####################

                                       
max_depths = [3,4,5]
learning_rates = [0.1,0.2,0.5]
n_estimatorss = [50,100,150]

model_XGB = xgb.XGBRegressor().fit(X,Y)
cv_XGB = [rmse_cv(xgb.XGBRegressor(max_depth =  max_depth, learning_rate=learning_rate, n_estimators=n_estimators)).mean() for max_depth in max_depths for learning_rate in learning_rates for n_estimators in n_estimatorss]
cv_XGB

cv_XGB = rmse_cv(xgb.XGBRegressor()).mean()
cv_XGB

lst1 = zip(feature_cols,model_XGB.feature_importances_)
lst1 = pd.DataFrame(lst1)
lst1.to_csv('XGB Importance.csv')
            


#####################Gradient Boosting Regressor#####################

#Feature Importance —— Ridge Regression
alphas = [1000,1500,2000,10000]
cv_clf = [rmse_cv(linear_model.Ridge(alpha = alpha)).mean() 
            for alpha in alphas]

cv_clf = pd.Series(cv_clf, index = alphas)
cv_clf.plot(title = "Validation")
plt.xlabel("alpha")
plt.ylabel("rmse")
cv_clf.min()  
cv_clf

clf = linear_model.Ridge(alpha=1).fit(X, Y)   #Change alpha

print ("Number of features used:{}".format(np.sum(clf.coef_!=0)))
cv_CLF = rmse_cv(linear_model.Ridge(alpha=1)).mean()  #Change alpha
cv_CLF

len(clf.coef_)
clf.coef_[0][1]
print(clf.coef_)
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet Name1")
for i in range(len(feature_cols)):
 sheet.write(i+1,2, clf.coef_[0][i])
 sheet.write(i+1,1, feature_cols[i][0])
workbook.save("result.xls")

lst2 = zip(feature_cols,clf.coef_)
lst2 = pd.DataFrame(clf.coef_)
lst2.to_csv('CLF Importance Coef.csv')

Selection=pd.read_csv('ImportanceAll.csv',na_values='NONE')
a=Selection.Column_Names.value_counts()
a.to_csv('Feature Selection.csv')


#####################Gradient Boosting Regressor#####################

GBR = GradientBoostingRegressor(n_estimators=10,learning_rate=0.9,subsample=0.8)
GBR = GradientBoostingRegressor()
avg_result = rmse_cv(GBR).mean()
print('The average result for gradient boosting decision tree is:')
print(avg_result)



#####################AdaBoost Regressor Linear Regression#####################

AdaBoost_linear = AdaBoostRegressor(LinearRegression())
avg_result = rmse_cv(AdaBoost_linear).mean()
print('The average result for AdaBoostRegressor(LinearRegression) is:')
print(avg_result)

#####################AdaBoost Regressor SVR#####################
#LinearSVR()
AdaBoost_linear = AdaBoostRegressor(SVR())
avg_result = rmse_cv(AdaBoost_linear).mean()
print('The average result for AdaBoostRegressor(LinearRegression) is:')
print(avg_result)




