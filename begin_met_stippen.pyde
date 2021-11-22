import random
num = 1
counter = 0

def setup():
    
    
    size(500, 500)
    background(10000)
    


def draw():
    
    global num
    global counter
    
    fill(211)
    rect(150, 150, 200, 200)
    

    
    if num == 1:
        fill(0)
        ellipse(250, 250, 40, 40)
        
    elif num == 2:
         fill(0)
         ellipse(220, 220, 40, 40)
         ellipse(280, 280, 40, 40)
         
         
    elif num == 3:
         fill(0)
         ellipse(200, 200, 40, 40)
         ellipse(250, 250, 40, 40)
         ellipse(300, 300, 40, 40)
    
                      
    elif num == 4:
         fill(0)
         ellipse(200, 200, 40, 40)
         ellipse(200, 300, 40, 40)
         ellipse(300, 300, 40, 40)
         ellipse(300, 200, 40, 40)
    
                               
    elif num == 5:
         fill(0)
         ellipse(200, 200, 40, 40)
         ellipse(200, 300, 40, 40)
         ellipse(300, 300, 40, 40)
         ellipse(300, 200, 40, 40)
         ellipse(250, 250, 40, 40)
    
                                        
    elif num == 6:
         fill(0)
         ellipse(200, 200, 40, 40)
         ellipse(200, 300, 40, 40)
         ellipse(300, 300, 40, 40)
         ellipse(300, 200, 40, 40)
         ellipse(200, 250, 40, 40)
         ellipse(300, 250, 40, 40)
         
         
        
def mousePressed():
    
    global num
        
    if 150 < mouseX < 150 + 200 and 150 < mouseY < 150 + 200:
       num = random.randint(1, 6)
