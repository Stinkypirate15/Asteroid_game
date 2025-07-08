import pygame
from circleshape import CircleShape
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        else:
            random_rotate=random.uniform(20,50)
            new_rotation = self.velocity.rotate(random_rotate)
            new_rotation_2 = self.velocity.rotate(-random_rotate)
            new_asteroid_Radius=self.radius- ASTEROID_MIN_RADIUS
           
           
            new_asteroid_Spawn=Asteroid(self.position.x,self.position.y,new_asteroid_Radius,)
            new_asteroid_Spawn_2=Asteroid(self.position.x,self.position.y,new_asteroid_Radius,)
            velocity1=new_rotation * 1.2
            velocity2=new_rotation_2 * 1.2
            new_asteroid_Spawn.velocity=velocity1
            new_asteroid_Spawn_2.velocity=velocity2
            
            Asteroid.add(new_asteroid_Spawn)
            Asteroid.add(new_asteroid_Spawn_2)
