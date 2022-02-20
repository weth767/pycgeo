import abc
import sys
import pygame
from errors import Messages
import tkinter as tk
from utils import Utils, Colors, Consts


class Canvas(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def draw(self, **kwargs):
        pass


class PygameCanvas(Canvas):
    screen = None
    width = Consts.DEFAULT_SCREEN_WIDTH
    height = Consts.DEFAULT_SCREEN_HEIGHT

    def __init__(self, **kwargs):
        """
        Pygame Canvas Module
        Args
        :arg width (float) width of screen
        :arg height (float) height of screen
        :arg use_cartesian_plan (bool) if cartesian plan mode will be used or not
        """
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(Consts.DEFAULT_FONT_FAMILY, Consts.DEFAULT_FONT_SIZE)
        self.w = kwargs.get('width') if kwargs.get('width') is not None else Consts.DEFAULT_SCREEN_WIDTH
        self.h = kwargs.get('height') if kwargs.get('height') is not None else Consts.DEFAULT_SCREEN_HEIGHT
        self.use_cartesian_plan = kwargs.get('use_cartesian_plan') \
            if kwargs.get('use_cartesian_plan') is not None else False
        if self.w is None or self.h is None:
            print(Messages.CV_MS01)
        self.screen = pygame.display.set_mode((self.w, self.h))

    def __build_cartesian_plan__(self):
        """
        Draw a cartesian plan into screen showing 25 by 25 point to each axis by the screen size
        :return:
        """
        half_height = self.h / 2
        half_width = self.w / 2
        pygame.draw.line(self.screen, Colors.black, (0, half_height), (self.w, half_height))
        pygame.draw.line(self.screen, Colors.black, (half_width, 0), (half_width, self.h))
        pygame.draw.circle(self.screen, Colors.black, (half_width, half_height), 2, 0)
        for w in range(1, int(half_width)):
            if w % 25 == 0:
                # eixo x positivo
                textxp = self.font.render(str(w), False, Colors.black)
                self.screen.blit(textxp, (half_width + w - 5, (half_height - 20)))
                pygame.draw.line(self.screen, Colors.black, (half_width + w, (half_height - 3)),
                                 (half_width + w, half_height + 3))
                # eixo x negativo
                textxn = self.font.render(f'-{str(w)}', False, Colors.black)
                self.screen.blit(textxn, (half_width - 5 - w, (half_height - 20)))
                pygame.draw.line(self.screen, Colors.black, (half_width - w, (half_height - 3)),
                                 (half_width - w, half_height + 3))

        for h in range(1, int(half_height)):
            if h % 25 == 0:
                # eixo y positivo
                textyp = self.font.render(str(h), False, Colors.black)
                self.screen.blit(textyp, (half_width - 20, (half_height - h - 5)))
                pygame.draw.line(self.screen, Colors.black, (half_width - 3, (half_height - h)),
                                 (half_width + 3, half_height - h))
                # eixo y negativo
                textyn = self.font.render(f'-{str(h)}', False, Colors.black)
                self.screen.blit(textyn, (half_width - 20, (half_height + h - 5)))
                pygame.draw.line(self.screen, Colors.black, (half_width - 3, (half_height + h)),
                                 (half_width + 3, half_height + h))

    def draw(self, **kwargs) -> None:
        """
        Draw method of Pygame Canvas Module
       Args:
          :arg screen (Surface, optional) New Pygame Surface if user need override screen
          :arg points (list) List of Point that will be drawn on screen
          :arg color (tuple, optional) Tuple represent intensity of RGB color of drawn points
          :arg background_color (tuple, optional) Tuple represent intensity of RGB color of screen background
          :arg
       Returns:
           None
       """
        self.screen = kwargs.get('screen') if kwargs.get('screen') is not None else self.screen
        points = kwargs.get('points') if kwargs.get('points') is not None else []
        color = kwargs.get('color') if kwargs.get('color') is not None else Colors.black
        background_color = kwargs.get('background_color') if kwargs.get('background_color') is not None else \
            Colors.white
        pygame.display.set_caption('Canvas')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(background_color)
            if self.use_cartesian_plan:
                self.__build_cartesian_plan__()
                for point in points:
                    x = self.w / 2 + point.x
                    y = self.h - (self.h / 2 + point.y)
                    pygame.draw.circle(self.screen, color, (x, y), 1, 1)
            else:
                for point in points:
                    pygame.draw.circle(self.screen, color, (abs(point.x), abs(self.h - point.y)), 1, 1)
            pygame.display.update()


class TkinterCanvas(Canvas):
    screen = None
    width = Consts.DEFAULT_SCREEN_WIDTH
    height = Consts.DEFAULT_SCREEN_HEIGHT

    def __init__(self, **kwargs):
        """
        Tkinter Canvas Module
        Args
        :arg width (float) width of screen
        :arg height (float) height of screen
        :arg use_cartesian_plan (bool) if cartesian plan mode will be used or not
        """
        self.w = kwargs.get('width') if kwargs.get('width') is not None else Consts.DEFAULT_SCREEN_WIDTH
        self.h = kwargs.get('height') if kwargs.get('height') is not None else Consts.DEFAULT_SCREEN_HEIGHT
        self.use_cartesian_plan = kwargs.get('use_cartesian_plan') \
            if kwargs.get('use_cartesian_plan') is not None else False
        if self.w is None or self.h is None:
            print(Messages.CV_MS01)
        self.screen = tk.Tk()
        self.screen.configure(width=self.w, height=self.h)

    def draw(self, **kwargs):
        """
        Draw method of Tkinter Canvas Module
          Args:
             :arg screen (Surface, optional) New Pygame Surface if user need override screen
             :arg points (list) List of Point that will be drawn on screen
             :arg color (tuple, optional) Tuple represent intensity of RGB color of drawn points
             :arg background_color (tuple, optional) Tuple represent intensity of RGB color of screen background

          Returns:
              None
        """
        self.screen = kwargs.get('screen') if kwargs.get('screen') is not None else self.screen
        points = kwargs.get('points') if kwargs.get('points') is not None else []
        color = kwargs.get('color') if kwargs.get('color') is not None else Colors.black
        color = Utils.rgb_to_hex(color[0], color[1], color[2])
        background_color = kwargs.get('background_color') if kwargs.get('background_color') is not None else \
            Colors.white
        background_color = Utils.rgb_to_hex(background_color[0], background_color[1], background_color[2])
        self.screen.title('Canvas')
        self.screen.configure(background=background_color)
        canvas = tk.Canvas(self.screen, width=self.w, height=self.h)
        for point in points:
            canvas.create_oval(point.x, self.h - point.y, point.x, self.h - point.y, width=0, fill=color)
        canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.screen.mainloop()
