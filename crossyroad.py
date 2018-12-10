add_library('sound')

import random
import math
import os
path = os.getcwd()
print(path)

a=loadImage(path+'/car1.png')

b=loadImage(path+'/car2.png')

m=loadImage(path+'/car3.png')

d=loadImage(path+'/car4.png')

e=loadImage(path+'/cartaxi.png')

f=loadImage(path+'/train.png')


def setup():
    global a,b,m,d,e,f,music
    size(700, 700)
    text('Play Game', 350, 350)
    path = os.getcwd()
    music = SoundFile(this, path+'/BGM.mp3')
    music.loop()


class character():

    def __init__(self):
        self.x = 350
        self.y = 675
        self.v = 25
        self.img = loadImage(path+'/P.png')
        self.stage = 2

    def display(self):
        self.img.resize(25, 25)
        image(self.img, self.x, self.y)
        
        
    def stageclear(self):
        if c.y == 0:
            c.y=675
            self.stage += 1
    
    def __str__(self):
        return str(self.stage-1)
    


class Obstacle:
    def __init__(self, x, y, v, i, sizex, sizey):
        self.x = x
        self.y = y
        self.v = v
        self.sizex=sizex
        self.sizey=sizey
        imagelist=[a,b,m,d,e,f]
        print imagelist
        self.car = imagelist[i]
        print('imagelist: ',imagelist)
 
        self.car.resize(sizex, sizey)
 

    def move(self):
         if c.y==0:
             self.v*=1.1*log(c.stage)
     
         if self.v>0:
             self.x+=self.v
        
             if self.x>=1000:
                self.x=0
 
         else:
             self.x+=self.v
             if self.x<=-300:
                self.x=700

         if self.x - self.sizex/2 <= c.x <= self.x + self.sizex/2 and self.y - self.sizey/2 <= c.y <= self.y + self.sizey/2:
             c.v=0
        
            
    def display(self):
         # self.car1.resize(70, 50)
         image(self.car, self.x, self.y)

class train(Obstacle):
    
    def move(self):
        if c.y==0:
            self.v*=1.02*log(c.stage)
        self.x+=self.v
        if self.x>=3000:
            self.x=-800
        
        if self.x - self.sizex/8 <= c.x <= self.x + self.sizex/2 and self.y - self.sizey/3 <= c.y <= self.y + self.sizey/3:
             c.v=0
        
class tree:
    global v
    def __init__(self, x, y):
       self.x=x
       self.y=y
       self.img=loadImage(path+'/c.png')
       self.img.resize(25, 25)
       self.up = 0
       self.down = 0
       self.right = 0
       self.left = 0
   
    def display(self):
       image(self.img, self.x, self.y)
       
    def distance(self):
       print('cx:', c.x)
       print('selfx:', self.x)
       print('cy:',c.y)
       print('selfy:',self.y)
            

class Board():
    def __init__(self):
        self.road = loadImage(path+'/Road.jpg')
        self.grass = loadImage(path+'/Grass.jpg')
        self.rail = loadImage(path+'/Rail.jpg')
        self.tree = loadImage(path+'/c.png')

    def display(self):
        self.road.resize(700, 75)
        self.grass.resize(700, 50)
        self.rail.resize(700, 25)
        self.tree.resize(25, 25)
        image(self.road, 0, 50)
        image(self.road, 0, 575)
        image(self.road, 0, 500)
        image(self.road, 0, 375)
        image(self.road, 0, 125)
        image(self.road, 0, 300)
        image(self.grass, 0, 325)
        image(self.grass, 0, 450)
        image(self.grass, 0, 200)
        image(self.rail, 0, 250)
        image(self.rail, 0, 275)
        image(self.rail, 0, 25)
        image(self.grass, 0, 650)
        image(self.grass, 0, -25)
        image(self.grass, 0, 300)

        


b = Board()

c = character()
v1 = Obstacle(1000, 400, random.randint(-5, -3), 0, 50, 25)
v2 = Obstacle(400, 175, random.randint(3, 5), 3, 35, 25)
v3 = Obstacle(200, 150, random.randint(-5,-3), 2, 55, 25)
v4 = Obstacle(600, 75, random.randint(-5, -3), 2, 55, 25)
v5 = Obstacle(500, 50, random.randint(-5, -3), 0, 55, 25)
v6 = Obstacle(450, 100, random.randint(-5, -3), 0, 55, 25)
v7 = Obstacle(300, 125, random.randint(3, 5), 4, 55, 25)
v8 = Obstacle(900, 500, random.randint(3, 5), 4, 55, 25)
v9 = Obstacle(1500, 575, random.randint(-5, -3), 0, 50, 25)
v10 = Obstacle(1200, 375, random.randint(-5, -3), 2, 50, 25)
v11 = Obstacle(250, 425, random.randint(-5, -3), 2, 55, 25)
v12 = Obstacle(200, 600, random.randint(3, 5), 4, 40, 25)
v13 = Obstacle(180, 550, random.randint(-5, -3), 2, 55, 25)
v14 = Obstacle(150, 525, random.randint(3, 5), 3, 40, 25)
v15 = Obstacle(0, 625, random.randint(3, 5), 3, 40, 25)



t1 = train(500, 250, 10, 5, 500, 25)
t2 = train(100, 25, 14, 5, 500, 25)
t3 = train(-400, 275, 8, 5, 600, 25)

tr1 = tree(350, 650)
tr2 = tree(475, 350)
tr3 = tree(350, 300)
tr4 = tree(300, 350)
tr5 = tree(250, 350)
tr6 = tree(100, 350)
tr7 = tree(500, 225)
tr8 = tree(425, 225)
tr9 = tree(375, 200)
tr10 = tree(225, 225)
tr11 = tree(225, 300)
tr12 = tree(150, 225)
tr13 = tree(125, 225)


def draw():
    stagenum = 'Stage ' + str(c)

    size(700, 700)
    background(0, 0, 0)

    b.display()
    c.display()
    v1.display()
    v2.display()
    v3.display()
    v4.display()
    v5.display()
    v6.display()
    v7.display()
    v8.display()
    v9.display()
    v10.display()
    v11.display()
    v12.display()
    v13.display()
    v14.display()
    v15.display()
    t1.display()
    t2.display()
    t3.display()
    tr1.display()
    tr2.display()
    tr3.display()
    tr4.display()
    tr5.display()
    tr6.display()
    tr7.display()
    tr8.display()
    tr9.display()
    tr10.display()
    tr11.display()
    tr12.display()
    tr13.display()
    tr1.distance()
    tr2.distance()
    tr3.distance()
    tr4.distance()
    tr5.distance()
    tr6.distance()
    tr7.distance()
    tr8.distance()
    tr9.distance()
    tr10.distance()
    tr11.distance()
    tr12.distance()
    tr13.distance()

    

    v1.move()
    v2.move()
    v3.move()
    v4.move()
    v5.move()
    v6.move()
    v7.move()
    v8.move()
    v9.move()
    v10.move()
    v11.move()
    v12.move()
    v13.move()
    v14.move()
    v15.move()
    t1.move()
    t2.move()
    t3.move()
    c.stageclear()
    if c.v == 0:
      textSize(0)
      text('GAME OVER!!!!', 270, 350)
      fill(200, 200, 0)

    if c.y >= 660:
       textSize(50)
       text(stagenum , 270, 350)
       fill(200, 200, 0)
        
def keyPressed():
    if (key == CODED):
        if keyCode == UP:
            c.y -= c.v
            if tr1.y+25 > c.y >= tr1.y and c.x==tr1.x:
                c.y+=25
            if tr2.y+25 > c.y >= tr2.y and c.x==tr2.x:
                c.y+=25
            if tr3.y+25 > c.y >= tr3.y and c.x==tr3.x:
                c.y+=25
            if tr4.y+25 > c.y >= tr4.y and c.x==tr4.x:
                c.y+=25
            if tr5.y+25 > c.y >= tr5.y and c.x==tr5.x:
                c.y+=25
            if tr6.y+25 > c.y >= tr6.y and c.x==tr6.x:
                c.y+=25
            if tr7.y+25 > c.y >= tr7.y and c.x==tr7.x:
                c.y+=25
            if tr8.y+25 > c.y >= tr8.y and c.x==tr8.x:
                c.y+=25
            if tr9.y+25 > c.y >= tr9.y and c.x==tr9.x:
                c.y+=25
            if tr10.y+25 > c.y >= tr10.y and c.x==tr10.x:
                c.y+=25
            if tr11.y+25 > c.y >= tr11.y and c.x==tr11.x:
                c.y+=25
            if tr12.y+25 > c.y >= tr12.y and c.x==tr12.x:
                c.y+=25
            if tr13.y+25 > c.y >= tr13.y and c.x==tr13.x:
                c.y+=25
  
                        
        if keyCode == DOWN:
            c.y += c.v
            if tr1.y-25 < c.y <= tr1.y and c.x==tr1.x:
                c.y-=25
            if tr2.y-25 < c.y <= tr2.y and c.x==tr2.x:
                c.y-=25
            if tr3.y-25 < c.y <= tr3.y and c.x==tr3.x:
                c.y-=25
            if tr4.y-25 < c.y <= tr4.y and c.x==tr4.x:
                c.y-=25
            if tr5.y-25 < c.y <= tr5.y and c.x==tr5.x:
                c.y-=25
            if tr6.y-25 < c.y <= tr6.y and c.x==tr6.x:
                c.y-=25
            if tr7.y-25 < c.y <= tr7.y and c.x==tr7.x:
                c.y-=25
            if tr8.y-25 < c.y <= tr8.y and c.x==tr8.x:
                c.y-=25
            if tr9.y-25 < c.y <= tr9.y and c.x==tr9.x:
                c.y-=25
            if tr10.y-25 < c.y <= tr10.y and c.x==tr10.x:
                c.y-=25
            if tr11.y-25 < c.y <= tr11.y and c.x==tr11.x:
                c.y-=25
            if tr12.y-25 < c.y <= tr12.y and c.x==tr12.x:
                c.y-=25
            if tr13.y-25 < c.y <= tr13.y and c.x==tr13.x:
                c.y-=25
                
  
       
        if keyCode == LEFT:
            c.x -= c.v
            if tr1.x >= c.x > tr1.x-25 and c.y==tr1.y:
                c.x+=25
            if tr2.x >= c.x > tr2.x-25 and c.y==tr2.y:
                c.x+=25
            if tr3.x >= c.x > tr3.x-25 and c.y==tr3.y:
                c.x+=25
            if tr4.x >= c.x > tr4.x-25 and c.y==tr4.y:
                c.x+=25
            if tr5.x >= c.x > tr5.x-25 and c.y==tr5.y:
                c.x+=25
            if tr6.x >= c.x > tr6.x-25 and c.y==tr6.y:
                c.x+=25
            if tr7.x >= c.x > tr7.x-25 and c.y==tr7.y:
                c.x+=25
            if tr8.x >= c.x > tr8.x-25 and c.y==tr8.y:
                c.x+=25
            if tr9.x >= c.x > tr9.x-25 and c.y==tr9.y:
                c.x+=25
            if tr10.x >= c.x > tr10.x-25 and c.y==tr10.y:
                c.x+=25
            if tr11.x >= c.x > tr11.x-25 and c.y==tr11.y:
                c.x+=25
            if tr12.x >= c.x > tr12.x-25 and c.y==tr12.y:
                c.x+=25
            if tr13.x >= c.x > tr13.x-25 and c.y==tr13.y:
                c.x+=25
            
            
       
         
        if keyCode == RIGHT:
            c.x += c.v
            if tr1.x+25 > c.x >= tr1.x and c.y==tr1.y:
                c.x-=25
            if tr2.x >= c.x > tr2.x-25 and c.y==tr2.y:
                c.x-=25
            if tr3.x >= c.x > tr3.x-25 and c.y==tr3.y:
                c.x-=25
            if tr4.x >= c.x > tr4.x-25 and c.y==tr4.y:
                c.x-=25
            if tr5.x >= c.x > tr5.x-25 and c.y==tr5.y:
                c.x-=25
            if tr6.x >= c.x > tr6.x-25 and c.y==tr6.y:
                c.x-=25
            if tr7.x >= c.x > tr7.x-25 and c.y==tr7.y:
                c.x-=25
            if tr8.x >= c.x > tr8.x-25 and c.y==tr8.y:
                c.x-=25
            if tr9.x >= c.x > tr9.x-25 and c.y==tr9.y:
                c.x-=25
            if tr10.x >= c.x > tr10.x-25 and c.y==tr10.y:
                c.x-=25
            if tr11.x >= c.x > tr11.x-25 and c.y==tr11.y:
                c.x-=25
            if tr12.x >= c.x > tr12.x-25 and c.y==tr12.y:
                c.x-=25
            if tr13.x >= c.x > tr13.x-25 and c.y==tr13.y:
                c.x-=25
        
