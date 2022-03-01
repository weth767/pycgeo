import abc
import sys
import tkinter
import pygame
import tkinter as tk
from tkinter import font
from shapes import Shape
from utils import Utils, Colors, Consts


class Canvas(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, width=None, height=None, show_cartesian_plan=False,
                 show_cartesian_plan_numbers=True, show_cartesian_plan_lines=True):
        """
        Canvas Module
        :param width: Optional(float) Width of screen
        :param height: Optional(float) Height of screen
        :param show_cartesian_plan: bool If cartesian plan mode will be used or not. Default is False
        :param show_cartesian_plan_numbers If cartesian plan number will be showed. Default is True
        :param show_cartesian_plan_lines If cartesian plan lines will be showed. Default is True
        :return None
        """
        pass

    @abc.abstractmethod
    def __build_cartesian_plan__(self, **kwargs) -> None:
        """
        Method to build cartesian plan mode in Canvas Module, set lines and numbers to each axis,
        showing 25 by 25 point to each axis by the screen size by default
        :param kwargs: Case is necessary to use any parameter
        :return None:
        """
        pass

    @abc.abstractmethod
    def draw(self, shapes: list[Shape], screen=None, color=None,
             background_color=None, title="Canvas") -> None:
        """
        Method to draw shapes on screen
        :param screen: Optional[any] Instance of screen. It's changes as module implementation
        :param shapes: list[Shape]
        :param color: Optional[tuple]
        :param background_color: Optional[tuple]
        :param title: str. Default is 'Canvas'
        :return None
        """
        pass


class PygameCanvas(Canvas):
    def __init__(self, width=None, height=None, show_cartesian_plan=False,
                 show_cartesian_plan_numbers=True, show_cartesian_plan_lines=True):

        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(Consts.DEFAULT_FONT_FAMILY, Consts.DEFAULT_FONT_SIZE)
        self.width = width if width is not None else Consts.DEFAULT_SCREEN_WIDTH
        self.height = height if height is not None else Consts.DEFAULT_SCREEN_HEIGHT
        self.show_cartesian_plan = show_cartesian_plan
        self.show_cartesian_plan_numbers = show_cartesian_plan_numbers
        self.show_cartesian_plan_lines = show_cartesian_plan_lines
        self.screen = pygame.display.set_mode((self.width, self.height))

    def __build_cartesian_plan__(self):
        half_height = self.height / 2
        half_width = self.width / 2
        # draw axis lines and circle of center
        if self.show_cartesian_plan_lines:
            pygame.draw.line(self.screen, Colors.BLACK, (0, half_height), (self.width, half_height))
            pygame.draw.line(self.screen, Colors.BLACK, (half_width, 0), (half_width, self.height))
            pygame.draw.circle(self.screen, Colors.BLACK, (half_width, half_height), 2, 0)

        if self.show_cartesian_plan_numbers:
            # draw x-axis positive and negative marks and numbers
            # -5 value was used into both numbers render, to fix number position
            # -20 have same purpose
            for w in range(1, int(half_width)):
                if w % 25 == 0:
                    # positive x-axis
                    text_x_axis_positive = self.font.render(str(w), False, Colors.BLACK)
                    self.screen.blit(text_x_axis_positive, (half_width + w - 5, (half_height - 20)))
                    pygame.draw.line(self.screen, Colors.BLACK, (half_width + w, (half_height - 3)),
                                     (half_width + w, half_height + 3))
                    # negative x-axis
                    text_x_axis_negative = self.font.render(f'-{str(w)}', False, Colors.BLACK)

                    self.screen.blit(text_x_axis_negative, (half_width - 5 - w, (half_height - 20)))
                    pygame.draw.line(self.screen, Colors.BLACK, (half_width - w, (half_height - 3)),
                                     (half_width - w, half_height + 3))

            # draw y-axis positive and negative marks and numbers
            for h in range(1, int(half_height)):
                if h % 25 == 0:
                    # positive y-axis
                    text_y_axis_positive = self.font.render(str(h), False, Colors.BLACK)
                    self.screen.blit(text_y_axis_positive, (half_width - 20, (half_height - h - 5)))
                    pygame.draw.line(self.screen, Colors.BLACK, (half_width - 3, (half_height - h)),
                                     (half_width + 3, half_height - h))
                    # negative y-axis
                    text_y_axis_negative = self.font.render(f'-{str(h)}', False, Colors.BLACK)
                    self.screen.blit(text_y_axis_negative, (half_width - 20, (half_height + h - 5)))
                    pygame.draw.line(self.screen, Colors.BLACK, (half_width - 3, (half_height + h)),
                                     (half_width + 3, half_height + h))

    def draw(self, shapes: list[Shape], screen=None, color=None,
             background_color=None, title="Canvas") -> None:

        self.screen = screen if screen is not None else self.screen
        shapes = shapes if shapes is not None else []
        color = color if color is not None and len(color) >= 3 else Colors.BLACK
        background_color = background_color if background_color is not None and len(background_color) >= 3 else \
            Colors.WHITE
        pygame.display.set_caption(title)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(background_color)
            if self.show_cartesian_plan:
                self.__build_cartesian_plan__()
                for shape in shapes:
                    for point in shape.points:
                        x = self.width / 2 + point.x
                        y = self.height - (self.height / 2 + point.y)
                        pygame.draw.circle(self.screen, color, (x, y), 1, 1)
            else:
                for shape in shapes:
                    for point in shape.points:
                        pygame.draw.circle(self.screen, color, (abs(point.x), abs(self.height - point.y)), 1, 1)
            pygame.display.update()


class TkinterCanvas(Canvas):
    def __init__(self, width=None, height=None, show_cartesian_plan=False,
                 show_cartesian_plan_numbers=True, show_cartesian_plan_lines=True):

        self.width = width if width is not None else Consts.DEFAULT_SCREEN_WIDTH
        self.height = height if height is not None else Consts.DEFAULT_SCREEN_HEIGHT
        self.show_cartesian_plan = show_cartesian_plan
        self.show_cartesian_plan_numbers = show_cartesian_plan_numbers
        self.show_cartesian_plan_lines = show_cartesian_plan_lines
        self.screen = tk.Tk()
        self.screen.configure(width=self.width, height=self.height)

    def __build_cartesian_plan__(self, canvas: tkinter.Canvas) -> None:
        half_height = self.height / 2
        half_width = self.width / 2

        if self.show_cartesian_plan_lines:
            # draw axis lines and circle of center
            canvas.create_line((0, half_height), (self.width, half_height), width=1,
                               fill=Colors.BLACK_HEX)
            canvas.create_line((half_width, 0), (half_width, self.height), width=1,
                               fill=Colors.BLACK_HEX)
            canvas.create_oval((half_width, half_height), (half_width, half_height), width=3, fill=Colors.BLACK_HEX)

        if self.show_cartesian_plan_numbers:
            # draw x-axis positive and negative marks and numbers
            # -10 value was used into both numbers render, to fix number position
            for w in range(1, int(half_width)):
                if w % 25 == 0:
                    # positive x-axis
                    canvas.create_text(half_width + w, (half_height - 10), fill=Colors.BLACK_HEX,
                                       font=font.Font(family=Consts.DEFAULT_FONT_FAMILY,
                                                      size=Consts.DEFAULT_FONT_SIZE - 1), text=w)
                    canvas.create_line((half_width + w, (half_height - 3)), (half_width + w, half_height + 3))
                    # negative x-axis
                    canvas.create_text(half_width - w, (half_height - 10), fill=Colors.BLACK_HEX,
                                       font=font.Font(family=Consts.DEFAULT_FONT_FAMILY,
                                                      size=Consts.DEFAULT_FONT_SIZE - 1), text=w * -1)
                    canvas.create_line((half_width - w, (half_height - 3)), (half_width - w, half_height + 3))
            # draw y-axis positive and negative marks and numbers
            for h in range(1, int(half_height)):
                if h % 25 == 0:
                    # positive y-axis
                    canvas.create_text(half_width - 13, (half_height - h), fill=Colors.BLACK_HEX,
                                       font=font.Font(family=Consts.DEFAULT_FONT_FAMILY,
                                                      size=Consts.DEFAULT_FONT_SIZE - 1), text=h)
                    canvas.create_line(half_width - 3, (half_height - h), half_width + 3, half_height - h)
                    # negative y-axis
                    canvas.create_text(half_width - 13, (half_height + h), fill=Colors.BLACK_HEX,
                                       font=font.Font(family=Consts.DEFAULT_FONT_FAMILY,
                                                      size=Consts.DEFAULT_FONT_SIZE - 1), text=h * -1)
                    canvas.create_line(half_width - 3, (half_height + h), half_width + 3, half_height + h)

    def draw(self, shapes: list[Shape], screen=None, color=None,
             background_color=None, title="Canvas") -> None:

        self.screen = screen if screen is not None else self.screen
        _shapes = shapes if shapes is not None else []
        _color = Utils.rgb_to_hex(color[0], color[1], color[2]) if color is not None and len(color) >= 3 \
            else Colors.BLACK_HEX
        _background_color = Utils.rgb_to_hex(background_color[0], background_color[1], background_color[2]) \
            if background_color is not None and len(background_color) >= 3 else Colors.WHITE_HEX

        self.screen.title(title)
        self.screen.configure(background=_background_color)
        canvas = tk.Canvas(self.screen, width=self.width, height=self.height)

        if self.show_cartesian_plan:
            self.__build_cartesian_plan__(canvas)
            for shape in _shapes:
                for point in shape.points:
                    x = self.width / 2 + point.x
                    y = self.height - (self.height / 2 + point.y)
                    canvas.create_oval(x, y, x, y, width=0, fill=_color)
        else:
            for shape in shapes:
                for point in shape.points:
                    canvas.create_oval(point.x, self.height - point.y, point.x, self.height - point.y,
                                       width=0, fill=_color)
        canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.screen.mainloop()
