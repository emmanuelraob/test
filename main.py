import pygame
import time 

from Ants.kingdom import Kingdom

# Colores y variables
BLACK = (31, 30, 26)
KINGDOM_AMOUNT = 3



def draw_window(kingdoms, screen):
    screen.fill(BLACK)
    for k in kingdoms:
        k.draw(screen)
    pygame.display.update()

def action(kingdoms, screen,delta_time):
    for k in kingdoms:
        k.every_frame_kingdom_work(screen, delta_time)
    
        

def run_simulation():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    
    
    kingdoms = []
    for i in range(KINGDOM_AMOUNT):
        kingdoms.append(Kingdom(screen,i,1))


    last_time = time.perf_counter()
    frame_count = 0
    accumulated_time = 0
    running = True

    while running:
        current_time = time.perf_counter()
        delta_time = current_time - last_time
        last_time = current_time
        accumulated_time += delta_time
        frame_count += 1

        # Calcular y mostrar FPS cada segundo
        if accumulated_time >= 1.0:
            fps = frame_count / accumulated_time
            pygame.display.set_caption(f"Ant sim - FPS: {fps:.0f}")
            frame_count = 0
            accumulated_time = 0
            for k in kingdoms:
                k.every_second_kingdom_work(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        action(kingdoms, screen, delta_time)
        draw_window(kingdoms, screen)

    pygame.quit()




if __name__ == "__main__":
    run_simulation()
    