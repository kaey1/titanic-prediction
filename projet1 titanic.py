import pandas as pd
from sklearn.model_selection import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

import math
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
screen_width = 1280
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
y_pred = model.predict(X_test)
accuracy=accuracy_score(y_test, y_pred, normalize=True) 
def cercle(pos,radian,w):
    noir=(0,0,0)
    global screen,screen_height,screen_width
    pygame.draw.circle(screen, noir, pos, radian,width=w)
def text(font,xy,size,text):
     my_font = pygame.font.SysFont(font, size)
     text_surface = my_font.render(text, False, (0, 0, 0))
     screen.blit(text_surface, xy)
def clickcercle(mouse_x,mouse_y,cerclexy,clicked,anti):
    distance = math.sqrt((mouse_x - cerclexy[0])**2 + (mouse_y - cerclexy[1])**2)
    if distance <= 20:
        if clicked==1:
             clicked=0
             
        else:
            clicked=1
            anti=0
    return clicked,anti

def gui(tx,ty):
    
    pygame.init()
    
    modele = DecisionTreeClassifier()
    modele.fit(tx, ty)
    
    
    pygame.display.set_caption("Le Titanic")
    white = (255, 255, 255)
    running = True
    hc=0
    fc=0
    slider = Slider(screen, 60, 250, 300, 30, min=0, max=99, step=1)
    output = TextBox(screen, 180, 300, 50, 50, fontSize=30)

    while running:
        pygame.init()
        iy=1
        ix=screen_width/3
        tx=20
        image = pygame.image.load('titanic_sink.png')
        titre="peut tu survivre le titanic?"
        titrexy=(20,20)
        text('Arial',titrexy,30,titre)
        screen.blit(image, (ix, iy))
        pygame.display.flip()
        screen.fill(white)

#############################################################################
        hommexy=(100,130)
        femmexy=(300,130)
        hommet="homme"
        femmet="femme"
        text('Arial',(150,80),30,"votre sexe")
        text('Arial',hommexy,30,hommet)
        text('Arial',femmexy,30,femmet)
        hommexy=(50,150)
        femmexy=(250,150)
        cercle(hommexy,20,5)
        cercle(femmexy,20,5)
        if hc==1:
            cercle(hommexy,10,0)
        elif fc==1:
            cercle(femmexy,10,0)

################################################################################################
        age=slider.getValue()
        agexy=(150,200)
        text('Arial',agexy,30,"Votre age")

##################################################################################################
        classe1xy=(100,300)
        classe2xy=(150,300)
        classe3xy=(250,300)
        

###################################################################################################
#sibsp et parch
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                hc,fc=clickcercle(mouse_x, mouse_y,hommexy,hc,fc)
                fc,hc=clickcercle(mouse_x, mouse_y,femmexy,fc,hc)
                if hc==1:
                    hfc=0
                elif fc==1:
                    hfc=1
                else:
                    hfc=2

        events = pygame.event.get()
        output.setText(slider.getValue())
        
        pygame_widgets.update(events)        
    pygame.quit()
if accuracy>0.65:
    print("Titanic")
    gui(X,y)
else:
    print("Le programme n'est pas sûr de ses prédictions. Veuillez contacter un NSIen immédiatement.")
