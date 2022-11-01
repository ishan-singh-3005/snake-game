import pygame
import random
from random import randrange
import time

pygame.init()

ORANGE = (255, 123, 7)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

SCREEN_SIZE = 500
win = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snake Game")

SNAKE_BLOCK = 10
SNAKE_SPEED = 10

FONT = pygame.font.SysFont('comicsans', 40)

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, BLACK, [x[0], x[1], snake_block, snake_block])

def display_score(score):
    score_text = FONT.render("Score: " + str(score), 1, ORANGE)
    win.blit(score_text, (SCREEN_SIZE - score_text.get_width() - 10, 10))

def close_menu(score):
    win.fill(BLACK)
    score_text = FONT.render("Your final score was: " + str(score), 1, ORANGE)
    command_1 = FONT.render("Press C to replay", 1, ORANGE)
    command_2 = FONT.render("Press Q to quit", 1, ORANGE)
    win.blit(score_text, (SCREEN_SIZE / 2 - score_text.get_width() / 2, 50))
    win.blit(command_1, (SCREEN_SIZE / 2 - command_1.get_width() / 2, 100))
    win.blit(command_2, (SCREEN_SIZE / 2 - command_2.get_width() / 2, 140))

def main():
    game_over = False
    x1 = SCREEN_SIZE / 2
    y1 = SCREEN_SIZE / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, SCREEN_SIZE - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_SIZE - SNAKE_BLOCK) / 10.0) * 10.0
    run = True
    while run:
        while game_over:
            close_menu(Length_of_snake - 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        main()
                    elif event.key == pygame.K_q:
                        pygame.quit()
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0
 
        if x1 >= SCREEN_SIZE or x1 < 0 or y1 >= SCREEN_SIZE or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        win.fill(BLUE)
        pygame.draw.rect(win, GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True
 
            draw_snake(SNAKE_BLOCK, snake_List)        

        draw_snake(SNAKE_BLOCK, snake_List) 
        display_score(Length_of_snake - 1)   
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_SIZE - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_SIZE - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1
        
        clock.tick(SNAKE_SPEED)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()