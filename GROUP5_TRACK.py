# Members: Alex Hooper, Jerry Fan, Grant Zalomek

from BirdBrain import Finch
import time 

bird = Finch()
print("Place on white surface")
time.sleep(6)
print("Scanning white...")
white = bird.getLine('R')+bird.getLine('L')/2
white=white/2
print("Place on black surface")
time.sleep(6)
print("Scanning black...")
black = bird.getLine('R')+bird.getLine('L')/2
black=black/2
time.sleep(6)
print(black)
print(white)
threshold = white+black/2

while not bird.getButton('A'):
    if bird.getDistance()>10:
        if bird.getLine('L') < threshold and bird.getLine('R') < threshold:
            bird.setMotors(0,1)
        elif bird.getLine('L') < threshold:
            bird.setMotors(0,1)
        elif bird.getLine('R') < threshold:
            bird.setMotors(1,0)
        else:
            bird.setMotors(1,1)
    else:
        bird.stop()
        bird.playNote(80,2)
        time.sleep(2)
        for i in range(3):
            bird.setBeak(0,0,100)
            bird.setTail("all", 0, 100,0)
            time.sleep(1.5)
            bird.setBeak(0,0,0)
            bird.setTail("all",0,0,0)
            time.sleep(1.5)
        bird.setTurn('L', 90,100)
        bird.setMove('F',20,100)
        bird.setTurn('R',90,100)
        bird.setMove('F', 40, 100)
        bird.stopAll()
        break

