import pygame
import time 

from Ants.kingdom import Kingdom

#Variables
BLACK = (31, 30, 26)
KINGDOM_AMOUNT = 1
WIDTH, HEIGHT = 1000, 700
DAY = 2 #seconds 
WEEK = DAY*7 #seconds



def draw_window(kingdoms, screen):
    screen.fill(BLACK)
    for k in kingdoms:
        k.draw(screen)
    pygame.display.update()

def actions_every_frame(kingdoms, screen,delta_time):
    for k in kingdoms:
        k.every_frame_kingdom_work(screen, delta_time)

def actions_every_second(screen, kingdoms):
    for k in kingdoms:
        k.every_second_kingdom_work(screen)
    
    
def actions_every_day():
    pass

def actions_every_week():
    pass

def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    
    kingdoms = []
    for i in range(KINGDOM_AMOUNT):
        kingdoms.append(Kingdom(screen,i,1))


    last_time = time.time()
    frame_count = 0
    accumulated_time = 0
    complete_total_time = 0
    total_time = 0 
    day_counter = 0
    week_counter = 0

    running = True
    while running:
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        accumulated_time += delta_time
        total_time += delta_time
        frame_count += 1

        #Days and week counter
        if total_time >= DAY:
            day_counter += 1
            total_time -= DAY
            actions_every_day()
            if day_counter%7 == 0:
                day_counter = 0
                week_counter += 1
                actions_every_week()


        # Calculate and show fps every second
        if accumulated_time >= 1.0:
            fps = frame_count / accumulated_time
            pygame.display.set_caption(f"Ant sim - FPS: {fps:.0f}")
            frame_count = 0
            accumulated_time = 0
            actions_every_second(screen, kingdoms)
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        actions_every_frame(kingdoms, screen, delta_time)
        draw_window(kingdoms, screen)

        print(f"Tiempo transcurrido: {total_time:.0f} horas, Dias: {day_counter}, Semanas: {week_counter} ", end='\r')


    pygame.quit()




if __name__ == "__main__":
    run_simulation()
    