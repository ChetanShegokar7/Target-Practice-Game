# Created By : Chetan Shegokar
# Email : chetanshegokar777@gmail.com

# ***Instructions***
# If you miss the target continiously three time the game will be over.
# The ship and bullet speed will increase after every 3 times target hit.

# How to play?
# You can move the ship up and down using up and down arrow keys.
# To fire bullets use SPACEBAR key.
# To exit the game press ESCAPE KEY.

# can hit the target 100 times :D ?

import sys
import pygame

# import all required modules.
from target import Target
from ship import Ship
from bullets import Bullets
from settings import Settings
from button import Button
from stats import Stats
from time import sleep
import sound_effects as se

class TargetPractice:
    """The main class of the game."""
    def __init__(self):
        """Initialize the variables."""
        pygame.init()

        # Instance of settings and stats class.
        self.settings = Settings()
        self.stats = Stats()

        # Create screen and get rect.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Target Practice")
        
        # Instance of target class.
        self.target = Target(self)
        
        # Instance of Ship class.
        self.ship = Ship(self)

        # Group for bullets.
        self.bullets = pygame.sprite.Group()

        self._create_buttons()

    def _create_buttons(self):

        # Instance of Button class and create play button.
        self.play_button = Button(self, 'Play')

        # create hit button and set its initial position.
        self.hit_button = Button(self, 'Target Hit')
        self.hit_button.button_rect.top = 0
        self.hit_button.button_rect.left = 200

        # Create the hit count button and set its initial position.
        # This button represents the number below Target hit button.
        self.hit_count_button = Button(self, str(self.stats.target_hits))
        self.hit_count_button.button_rect.center = (
            self.hit_button.button_rect.center)
        self.hit_count_button.button_rect.top = (
            self.hit_button.button_rect.bottom + 10)

        # Create the Bullets Left button and set its initial position.
        self.target_miss_button = Button(self, "Bullets Left")
        self.target_miss_button.button_rect.right = (
            self.screen_rect.right - 200)
        self.target_miss_button.button_rect.top = 0

        # Create the bullet left button and set its initial position.
        # This button represents the number below Bullet left button.
        self.bullet_left_button = Button(self, str(self.stats.bullets_left))
        self.bullet_left_button.button_rect.center = (
            self.target_miss_button.button_rect.center)
        self.bullet_left_button.button_rect.top = (
            self.bullet_left_button.button_rect.bottom + 10)
    

    def run(self):
        """The main loop for the Target Practice."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.target.update_target()
                self.ship.update_ship()
                self._update_bullets()
            
            self._update_display()

    def _check_events(self):
        """Check for events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Check for keydown events."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._create_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Check for Keyup events."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Check for mouse events."""
        collision = self.play_button.button_rect.collidepoint(mouse_pos)
        if collision:
            self.stats.game_active = True
            self.stats.reset_stats()
          
    def _create_bullet(self):
        """Create new bullets and add to bullets group."""
        if len(self.bullets) <= self.settings.bullets_allowed:
            bullet = Bullets(self)
            se.bullet_fire.play()

            # add the new bullet to the bullets group.
            self.bullets.add(bullet)

        # if bullet passes outside the screen it will remove bullets.
        for bullet in self.bullets.copy():
            if bullet.bullet.x >= self.screen_rect.right:
                self.bullets.remove(bullet)

    def _update_bullets(self):
        """
        Update the bullets position, dectect bullet target collisions
        """
        # update bullets position.
        self.bullets.update()
        
        # for every bullet in the group detect collision with the target.
        for bullet in self.bullets:
            self.bullet_target_collision = pygame.sprite.spritecollideany(
                self.target, self.bullets)
            
            if self.bullet_target_collision:
                # if bulllet hit the taget.
                self._bullet_target_collision(bullet)
                
            # if bullet miss the target then the bullet is removed.
            if bullet.bullet.right >= self.screen_rect.right:
                self.bullets.remove(bullet)
                se.target_miss.play()
                self.stats.bullets_left -= 1
                
            # if bullets left becomes 0 then end the game.
            if self.stats.bullets_left <= 0:
                self.stats.game_active = False
                sleep(1)
                self.bullets.empty() 
                self.stats.reset_stats()
                
                self.settings.default_settings() 
        self._update_hit_count_button()
        self._update_bullets_left()
    
    def _bullet_target_collision(self, bullet):
        """What will happen after the bullet and target collision is here.""" 
        self.stats.reset_target_missed()
        self.stats.target_hit += 1
        self.stats.target_hits += 1

        self._update_hit_count_button()
                
        se.target_hit.play()
        self.bullets.remove(bullet)
                
        if self.stats.target_hit == 3:
            self.stats.reset_hit()
            self.settings.speed_up()

    def _update_hit_count_button(self):
        self.hit_count_button._prep_button(
            str(self.stats.target_hits))
        
        self.hit_count_button.button_rect.center = (
            self.hit_button.button_rect.center)
        
        self.hit_count_button.button_rect.top = (
            self.hit_button.button_rect.bottom + 10)

    def _update_bullets_left(self):
        self.bullet_left_button._prep_button(str(self.stats.bullets_left))
        
        self.bullet_left_button.button_rect.center = (
            self.target_miss_button.button_rect.center)
        
        self.bullet_left_button.button_rect.top = (
            self.bullet_left_button.button_rect.bottom + 10)
            

    def _update_display(self):
        """Display all objects to the screen."""

        # Fill the background with color.
        self.screen.fill(self.settings.bgcolor)
        
        # Display Bullets.
        for bullet in self.bullets.sprites():
            bullet.display_bullets()
        
        # Display Ship and target.
        self.ship.display_ship()
        self.target.display_target()
        
        self._display_menus_buttons()
        
        # if game not active display play button.
        if not self.stats.game_active:
            self.play_button.display_button()
        
        # Continiously update the screen.
        pygame.display.flip()
    
    def _display_menus_buttons(self):
        """Function to display all the menus and buttons."""
        self.hit_button.display_button()
        self.hit_count_button.display_button()
        self.bullet_left_button.display_button()
        self.target_miss_button.display_button()

if __name__ == '__main__':
    """This is similar to main function every thing inside this if statement
     will be executed, without this your game is not going to work.
    """
    # Instance of TargetPractice class
    tp = TargetPractice()
    tp.run()