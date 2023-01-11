import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
 

data = pd.read_csv("diabetes.csv")
data.head()



df = data[['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']]
corr = data.corr()
sns.heatmap(corr, cmap='YlGnBu', annot=True,
    linewidths=.3, linecolor='white',
    xticklabels=corr.columns.values,
    yticklabels=corr.columns.values)

X = df.iloc[:, :-1]
X.head()

y = data.iloc[:, -1]
y.head()

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, random_state=0, test_size=0.25)

# Build KNN model and compute the accuracy
treedec = DecisionTreeClassifier()
treedec.fit(X_train, y_train)

# Test the model
y_pred = treedec.predict(X_test)
print(y_pred)

# Model Score
result= treedec.score(X_test, y_test)
print("The final result of Decision Tree algo is :", result)
