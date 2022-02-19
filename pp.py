import pygame
from pygame.locals import *
import sys
import time
import random 
headpos = (255,213,102)
textpos = (240,240,240)
respos = (255,70,70)
BLACK = (0, 0, 0) 
GRAY = (127, 127, 127) 
WHITE = (255, 255, 255)
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0) 
CYAN = (0, 255, 255) 
MAGENTA = (255, 0, 255)
class Game:
    def __init__(self):
        self.w = 750
        self.h = 500
        self.typing = False
        self.end = False
        self.running = False
        self.input_text = ''
        self.show_text = ''
        self.word = ''
        self.used_time = 0
        self.start_time = 0
        self.res = 'START!'
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Type Speed test')
        
    def draw_text(self, screen, msg, p ,fsize, color):
        font = pygame.font.Font('/Users/derick/Downloads/PP Files/Calibri Regular.ttf', fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w/2, p))
        screen.blit(text, text_rect)
        pygame.display.update()

    def sentence(self):
        f = open('/Users/derick/Downloads/PP Files/sentences.txt').read()
        sen = f.split('\n')
        sen = random.choice(sen)
        return sen

    def reset(self):
        self.input_text = ''
        self.show_text = ''
        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Type Speed test')
        self.draw_text(self.screen, 'TYPE SPEED TEST', 90, 80, CYAN)
        self.word = str(self.sentence())
        if(len(self.word) == 0):
            self.reset()
        self.draw_text(self.screen, self.word, 160, 26, WHITE)
        pygame.draw.rect(self.screen, textpos, (50,250,650,50), 2)
        pygame.display.update()

    def calc(self):
        self.used_time = time.time() - self.start_time
        s1 = str(self.input_text)
        s2 = str(self.word)
        cnt = 0
        for i in range(0, len(s1)):
            try:
                if(s1[i] == s2[i]):
                    cnt += 1
            except:
                pass
        acc = cnt/len(s1)*100
        wpm = len(self.input_text)*60/(5*self.used_time)
        self.res = 'Time:'+str(round(self.used_time)) +" secs Accuracy:"+ str(round(acc)) + "%" + ' Wpm: ' + str(round(wpm))
        self.screen.fill(BLACK, (50,325,650,50))

    def run(self):
        self.reset()
        self.running = True
        while(self.running):
            self.screen.fill(BLACK, (50,250,650,50))
            pygame.draw.rect(self.screen, WHITE, (50,250,650,50), 2)
            self.draw_text(self.screen, self.show_text, 274, 26, GREEN)
            self.draw_text(self.screen, self.res, 350, 28, respos)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if(x >= 50 and x <= 650 and y >= 250 and y <= 300): 
                        self.typing = True
                        self.input_text = ''
                        self.show_text = ''
                        self.start_time = time.time()
                    if(x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset()
                elif event.type == pygame.KEYDOWN:
                    if self.typing and not self.end:
                        if event.key == pygame.K_RETURN:
                            self.input_text = ''
                            self.end = True
                            self.draw_text(self.screen, "Reset", self.h - 70, 26, GRAY)
                        elif event.key == pygame.K_SPACE:
                            self.show_text = ''
                            self.input_text += ' '
                            self.calc()
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                            self.show_text = self.show_text[:-1]
                        else:
                            self.input_text += event.unicode
                            self.show_text += event.unicode
Game().run()
