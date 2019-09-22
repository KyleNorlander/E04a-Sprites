#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.blue_5)
        self.animal_list = arcade.SpriteList()


    def setup(self):
        self.animal_sprite = arcade.Sprite("assets/bush2.png", 0.5)
        self.animal_sprite.center_x = 500
        self.animal_sprite.center_y = 50
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/bushOrange1.png", 0.5)
        self.animal_sprite.center_x = 320
        self.animal_sprite.center_y = 100
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/cloud1.png", 0.5)
        self.animal_sprite.center_x = 500
        self.animal_sprite.center_y = 500
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/house1.png", 0.5)
        self.animal_sprite.center_x = 550
        self.animal_sprite.center_y = 150
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/house2.png", 0.5)
        self.animal_sprite.center_x = 200
        self.animal_sprite.center_y = 150
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/fence.png", 0.5)
        self.animal_sprite.center_x = 480
        self.animal_sprite.center_y = 100
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/sun.png", 0.5)
        self.animal_sprite.center_x = 600
        self.animal_sprite.center_y = 560
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/tree.png", 0.5)
        self.animal_sprite.center_x = 620
        self.animal_sprite.center_y = 150
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/treePine.png", 0.5)
        self.animal_sprite.center_x = 50
        self.animal_sprite.center_y = 150
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/treeDead.png", 0.5)
        self.animal_sprite.center_x = 300
        self.animal_sprite.center_y = 150
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/cloud5.png", 0.5)
        self.animal_sprite.center_x = 90
        self.animal_sprite.center_y = 270
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/cloud8.png", 0.5)
        self.animal_sprite.center_x = 300
        self.animal_sprite.center_y = 370
        self.animal_list.append(self.animal_sprite)



    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()