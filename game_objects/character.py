import pygame

import pygame

class CircleCharacter:
    def __init__(self, screen, x, y, radius, color=(0, 0, 0)):
        """
        Initialize the CircleCharacter with a position, radius, and color.

        Parameters:
        - screen: The Pygame screen where the circle will be drawn.
        - x: The initial x-coordinate of the circle's center.
        - y: The initial y-coordinate of the circle's center.
        - radius: The radius of the circle.
        - color: The color of the circle (default is black).
        """
        self.screen = screen  # Store the screen for rendering
        self.x = x  # Set the initial x position
        self.y = y  # Set the initial y position
        self.radius = radius  # Set the radius of the circle
        self.color = color  # Set the color of the circle

    def move_left(self):
        """Move the circle left by 5 pixels."""
        if self.x > 0:
            self.x -= 5  # Decrease the x-coordinate

    def move_right(self):
        """Move the circle right by 5 pixels."""
        if self.x < self.screen.get_width():
            self.x += 5  # Increase the x-coordinate

    def move_down(self):
        """Move the circle down by 5 pixels."""
        if self.y < self.screen.get_height():
            self.y += 5  # Increase the y-coordinate

    def move_up(self):
        """Move the circle up by 5 pixels."""
        if self.y > 0:
            self.y -= 5  # Decrease the y-coordinate

    def change_color(self, color):
        """
        Change the color of the circle.

        Parameters:
        - color: The new color for the circle.
        """
        self.color = color  # Update the circle's color
        
    def render(self):
        """Draw the circle on the screen."""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
