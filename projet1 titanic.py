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
     text_surface = my_font.render(text, True, (0, 0, 0))
     screen.blit(text_surface, xy)
def clickcercle(mouse_x,mouse_y,cerclexy,r):
    distance = math.sqrt((mouse_x - cerclexy[0])**2 + (mouse_y - cerclexy[1])**2)#equation math pour distance
    if distance <= r:
        return True
def gui(tx,ty):
    
    pygame.init()
    
    modele = DecisionTreeClassifier()
    modele.fit(tx, ty)
    erreurtemp=0
    
    pygame.display.set_caption("Le Titanic")
    white = (255, 255, 255)
    running = True
    hc=0
    fc=0
    c1=0
    c2=0
    c3=0
    c123=0
    sib1=0
    hfc=2
    sliderage = Slider(screen, 60, 250, 300, 30, min=0, max=99, step=0.5)
    outputage = TextBox(screen, 180, 300, 70, 50, fontSize=30)
    slidersib = Slider(screen, 60, 500, 300, 30, min=0, max=10, step=1)
    outputsib = TextBox(screen, 180, 550, 50, 50, fontSize=30)
    sliderpar = Slider(screen, 500, 150, 300, 30, min=0, max=10, step=1)
    outputpar = TextBox(screen, 620,200, 50, 50, fontSize=30)
    submit=False
    while running:
     if submit==False:
        pygame.init()
        iy=150
        ix=screen_width/2
        tx=20
        image = pygame.image.load('titanic_sink1.png')
        titre="Peut tu survivre le titanic?"
        titrexy=(20,20)
        text('Arial',titrexy,30,titre)
        screen.blit(image, (ix, iy))
        pygame.display.flip()
        screen.fill(white)

#############################################################################
        hommexy=(100,130)
        femmexy=(300,130)
        hommet="Homme"
        femmet="Femme"
        text('Arial',(150,80),30,"Votre sexe")
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
        age=sliderage.getValue()
        agexy=(150,200)
        text('Arial',agexy,30,"Votre age")

##################################################################################################
        cx=50
        cd=100
        cy=400
        classe1xy=(cx,cy)
        classe2xy=(cx+cd,cy)
        classe3xy=(cx+cd+cd,cy)
        text('Arial',classe1xy,30,"1")
        text('Arial',classe2xy,30,"2")
        text('Arial',classe3xy,30,"3")
        text('Arial',(cx,cy-40),30,"Votre classe sociale")
        cx+=50
        classe1xy=(cx,cy+20)
        classe2xy=(cx+cd,cy+20)
        classe3xy=(cx+cd+cd,cy+20)
        cercle(classe1xy,20,5)
        cercle(classe2xy,20,5)
        cercle(classe3xy,20,5)
        if c1==1:
            cercle(classe1xy,10,0)
        elif c2==1:
            cercle(classe2xy,10,0)
        elif c3==1:
            cercle(classe3xy,10,0)

###################################################################################################
        


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                #########################################################################################
                #pour cocher les cercles
                clicked=clickcercle(mouse_x, mouse_y,hommexy,20)
                if clicked:
                    if hc==1:
                        hfc=2
                        hc=0
                    elif hc==0:
                        hfc=0
                        hc=1
                        fc=0
                clicked=clickcercle(mouse_x, mouse_y,femmexy,20)
                if clicked:
                    if fc==1:
                        hfc=2
                        fc=0
                    elif fc==0:
                        hfc=1
                        fc=1
                        hc=0
                clicked=clickcercle(mouse_x, mouse_y,classe1xy,20)
                if clicked:
                    if c1==1:
                        c123=0
                        c1=0
                    elif c1==0:
                        c123=1
                        c2,c3=0,0
                        c1=1
                clicked=clickcercle(mouse_x, mouse_y,classe2xy,20)
                if clicked:
                    if c2==1:
                        c123=0
                        c2=0
                    elif c2==0:
                        c123=2
                        c1,c3=0,0
                        c2=1
                clicked=clickcercle(mouse_x, mouse_y,classe3xy,20)
                if clicked:
                    if c3==1:
                        c123=0
                        c3=0
                    elif c3==0:
                        c123=3
                        c2,c1=0,0
                        c3=1
                clicked=clickcercle(mouse_x1,mouse_y1,button,100)
                if clicked:
                    if hfc!=2 and c123!=0:

                        new_data = pd.DataFrame({
                        'Pclass': [c123], 
                        'Sex': [hfc],
                        'Age': [age],  
                        'SibSp': [sibsp],  
                        'Parch': [parc]    
                            })
                        
                        new_data = pd.get_dummies(new_data)
                        Prediction=modele.predict(new_data)
                        submit=True
                    else:
                       erreurtemp=100
                       
                ########################################################################################
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if erreurtemp>0:
            erreurtemp-=1
            fonterreur = pygame.font.SysFont("Arial",30)
            texterreur = fonterreur.render("Erreur! Veuillez bien remplir tous les informations!", True, (255, 0, 0))
            screen.blit(texterreur, (400,300)) 
        button=(1050,150)
        buttonr=100
        events = pygame.event.get()
        mouse_x1, mouse_y1 = pygame.mouse.get_pos()
        clicked=clickcercle(mouse_x1,mouse_y1,button,buttonr)
        if clicked:
                pygame.draw.circle(screen, (0,0,255), button, buttonr,width=0)
        else:
            pygame.draw.circle(screen, (0,90,255), button, buttonr,width=0)
        outputage.setText(sliderage.getValue())
        outputsib.setText(slidersib.getValue())
        outputpar.setText(sliderpar.getValue())
        sibsp=slidersib.getValue()
        parc=sliderpar.getValue()
        text("Arial",(10,450),30,"Nombre de Fraterie et epoux")
        text("Arial",(500,100),30,"Nombre de Parent/enfant")
        text("Arial",(1000,135),30,"Resultat")
        pygame_widgets.update(events)  
     else:
        pygame.init()
        pygame.display.flip()
        screen.fill(white)
        surv = pygame.image.load('survive.png')
        mort = pygame.image.load('meurt.png')
        print(Prediction)
        if Prediction==0:
            screen.blit(mort, (400, 200))
            text("Arial",(400,0),30,"Tu n'a pas survecu le Titanic")
        else:
            screen.blit(surv, (400, 200))
            text("Arial",(400,0),30,"BRAVO! Tu a survecu le Titanic")
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.quit()
if accuracy>0.65:
    print("Titanic")
    gui(X,y)
else:
    print("Le programme n'est pas sûr de ses prédictions. Veuillez contacter un NSIen *IMMEDIATEMENT*!.")
