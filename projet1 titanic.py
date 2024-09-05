import pandas as pd
from sklearn.model_selection import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import tkinter as tk
df=pd.read_csv('titanic.csv')
df = df.drop("Name", axis='columns')
df = df.drop("Cabin", axis='columns')
df = df.drop("PassengerId", axis='columns')
df = df.drop("Ticket", axis='columns')
df = df.drop("Embarked", axis='columns')
df = df.drop("Fare", axis='columns')
df['Age'].fillna(df['Age'].median(), inplace=True)
df.loc[df['Sex'] == 'male', 'Sex'] = 0
df.loc[df['Sex'] == 'female', 'Sex'] = 1
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy=accuracy_score(y_test, y_pred, normalize=True) 
def button_clicked():
    print("Button clicked!")
if accuracy>0.65:
    print("yipeeee")
    root = tk.Tk()
    root.geometry("400x400")
# Creating a button with specified options
    button = tk.Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

    button.pack(padx=20, pady=20)

    root.mainloop()
else:
    print("Le programme n'est pas sûr de ses prédictions. Veuillez contacter un NSIen immédiatement.")
