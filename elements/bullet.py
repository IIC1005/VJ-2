if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        # POR HACER (2.0): Aspecto inicial de nuestra bala

        # POR HACER (2.1): Variables requeridas por nuestra bala
        pass

    def update(self):
        # POR HACER (2.2): Mover la bala y destruirla si se sale de la pantalla
        pass