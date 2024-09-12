import pandas as pd
from sklearn.model_selection import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pygame
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

    

def gui(tx,ty):
    screen_width = 1280
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    modele = DecisionTreeClassifier()
    modele.fit(tx, ty)
    pygame.init()
    
    pygame.display.set_caption("Le Titanic")
    white = (255, 255, 255)
    running = True
    while running:

        iy=screen_height-screen_height/10
        ix=screen_width/2
        image = pygame.image.load('titanic_sink.png')
        screen.blit(image, (ix, iy))
        pygame.display.flip()
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
    pygame.quit()
if accuracy>0.65:
    print("yipeeee")
    gui(X,y)
else:
    print("Le programme n'est pas sûr de ses prédictions. Veuillez contacter un NSIen immédiatement.")
