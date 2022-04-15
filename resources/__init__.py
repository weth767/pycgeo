import abc
import sys
from tkinter import font
import pygame
import tkinter as tk
from core import Point
from shapes import Shape
from utils import Consts, Colors


class Canvas:
    def __init__(self, width: int, height: int, start: Point, tag: str, shapes: list[Shape], show_cp=False,
                 show_cpn=True, show_cpl=True, show_border=True):
        self.width = width
        self.height = height
        self.start = start
        self.shapes = shapes
        self.tag = tag
        self.show_cp = show_cp
        self.show_cpn = show_cpn
        self.show_cpl = show_cpl
        self.show_border = show_border


class Screen(metaclass=abc.ABCMeta):
    surfaces: {}

    @abc.abstractmethod
    def __init__(self):
        pass

    """
    Method to configure screen
    """

    @abc.abstractmethod
    def configure(self, canvas_list: list[Canvas]) -> None:
        pass

    """
    Method to reset configs of screen
    """

    @abc.abstractmethod
    def reset(self) -> None:
        pass

    """
    Method to build cartesian plan inside a surface
    """

    @abc.abstractmethod
    def _build_cp(self, canvas: Canvas):
        pass

    """
    Method to draw at each canvas instance of screen
    """

    @abc.abstractmethod
    def _draw_at_canvas(self, canvas: Canvas):
        pass

    """
    Method to draw objects listed on list of canvas by tags received
        :param canvas
    """

    @abc.abstractmethod
    def draw(self) -> None:
        pass


class PygameScreen(Screen):
    surfaces = {}

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(Consts.DEFAULT_FONT_FAMILY, Consts.DEFAULT_FONT_SIZE)
        info = pygame.display.Info()
        width = info.current_w
        height = info.current_h
        self.screen = pygame.display.set_mode((width, height * 0.95))
        self.screen.fill(Colors.WHITE)
        self.canvas_list: list[Canvas] = []

    def configure(self, canvas_list: list[Canvas]):
        self.canvas_list = canvas_list
        for canvas in canvas_list:
            surface: pygame.Surface = pygame.Surface([canvas.width, canvas.height])
            surface.fill(Colors.WHITE)
            self.surfaces[canvas.tag] = surface

    def reset(self):
        pass

    def _build_cp(self, canvas: Canvas):
        surface: pygame.surface = self.surfaces[canvas.tag]
        if surface is None:
            return
        half_height = canvas.height / 2
        half_width = canvas.width / 2
        # draw axis lines and circle of center
        if canvas.show_cp:
            pygame.draw.line(surface, Colors.BLACK, (0, half_height), (canvas.width, half_height))
            pygame.draw.line(surface, Colors.BLACK, (half_width, 0), (half_width, canvas.height))
            pygame.draw.circle(surface, Colors.BLACK, (half_width, half_height), 2, 0)

        if canvas.show_cpn:
            # draw x-axis positive and negative marks and numbers
            # -5 value was used into both numbers render, to fix number position
            # -20 have same purpose
            for w in range(1, int(half_width)):
                if w % 25 == 0:
                    # positive x-axis
                    text_x_axis_positive = self.font.render(str(w), False, Colors.BLACK)
                    surface.blit(text_x_axis_positive, (half_width + w - 5, (half_height - 20)))
                    pygame.draw.line(surface, Colors.BLACK, (half_width + w, (half_height - 3)),
                                     (half_width + w, half_height + 3))
                    # negative x-axis
                    text_x_axis_negative = self.font.render(f'-{str(w)}', False, Colors.BLACK)

                    surface.blit(text_x_axis_negative, (half_width - 5 - w, (half_height - 20)))
                    pygame.draw.line(surface, Colors.BLACK, (half_width - w, (half_height - 3)),
                                     (half_width - w, half_height + 3))

            # draw y-axis positive and negative marks and numbers
            for h in range(1, int(half_height)):
                if h % 25 == 0:
                    # positive y-axis
                    text_y_axis_positive = self.font.render(str(h), False, Colors.BLACK)
                    surface.blit(text_y_axis_positive, (half_width - 20, (half_height - h - 5)))
                    pygame.draw.line(surface, Colors.BLACK, (half_width - 3, (half_height - h)),
                                     (half_width + 3, half_height - h))
                    # negative y-axis
                    text_y_axis_negative = self.font.render(f'-{str(h)}', False, Colors.BLACK)
                    surface.blit(text_y_axis_negative, (half_width - 20, (half_height + h - 5)))
                    pygame.draw.line(surface, Colors.BLACK, (half_width - 3, (half_height + h)),
                                     (half_width + 3, half_height + h))

    def _draw_at_canvas(self, canvas: Canvas):
        surface = self.surfaces[canvas.tag]
        if surface is None:
            return
        color = Colors.BLACK
        background_color = Colors.WHITE
        self.screen.fill(background_color)
        if canvas.show_cp:
            self._build_cp(canvas)
            for shape in canvas.shapes:
                for point in shape.points:
                    x = canvas.width / 2 + point.x
                    y = canvas.height - (canvas.height / 2 + point.y)
                    pygame.draw.circle(surface, color, (x, y), 1, 1)
        else:
            for shape in canvas.shapes:
                for point in shape.points:
                    pygame.draw.circle(surface, color, (abs(point.x), abs(canvas.height - point.y)), 1, 1)
        self.screen.blit(surface, (canvas.start.x, canvas.start.y))

    def draw(self):
        running = True
        while running:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                for canvas in self.canvas_list:
                    self._draw_at_canvas(canvas)
                pygame.display.flip()

            except KeyboardInterrupt:
                pass


class TkinterScreen(Screen):
    surfaces = {}

    def __init__(self):
        self.screen = tk.Tk()
        width = self.screen.winfo_screenwidth()
        height = self.screen.winfo_screenheight()
        self.screen.configure(width=width, height=height)
        self.screen.configure(background=Colors.WHITE_HEX)
        self.canvas_list: list[Canvas] = []

    def configure(self, canvas_list: list[Canvas]):
        self.canvas_list = canvas_list
        for canvas in canvas_list:
            surface = tk.Canvas(self.screen, width=canvas.width, height=canvas.height)
            surface.place(relx=canvas.start.x, rely=canvas.start.y)
            self.surfaces[canvas.tag] = surface

    def reset(self):
        pass

    def _build_cp(self, canvas: Canvas):
        surface: tk.Canvas = self.surfaces[canvas.tag]
        if surface is None:
            return
        half_height = canvas.height / 2
        half_width = canvas.width / 2
        if canvas.show_cpl:
            # draw axis lines and circle of center
            surface.create_line((0, half_height), (canvas.width, half_height), width=1,
                                fill=Colors.BLACK_HEX)
            surface.create_line((half_width, 0), (half_width, canvas.height), width=1,
                                fill=Colors.BLACK_HEX)
            surface.create_oval((half_width, half_height), (half_width, half_height), width=3, fill=Colors.BLACK_HEX)
        if canvas.show_cpn:
            # draw x-axis positive and negative marks and numbers
            # -10 value was used into both numbers render, to fix number position
            for w in range(1, int(half_width)):
                if w % 25 == 0:
                    # positive x-axis
                    surface.create_text(half_width + w, (half_height - 10), fill=Colors.BLACK_HEX,
                                        font=font.Font(family=Consts.DEFAULT_FONT_FAMILY,
                                                       size=Consts.DEFAULT_FONT_SIZE - 1), text=w)
                    surface.create_line((half_width + w, (half_height - 3)), (half_width + w, half_height + 3))
                    # negative x-axis
                    surface.create_text(half_width - w, (half_height - 10), fill=Colors.BLACK_HEX,
                                        font=font.Font(family=Consts.DEFAULT_FONT_FAMILY,
                                                       size=Consts.DEFAULT_FONT_SIZE - 1), text=w * -1)
                    surface.create_line((half_width - w, (half_height - 3)), (half_width - w, half_height + 3))
            # draw y-axis positive and negative marks and numbers
            for h in range(1, int(half_height)):
                if h % 25 == 0:
                    # positive y-axis
                    surface.create_text(half_width - 13, (half_height - h), fill=Colors.BLACK_HEX,
                                        font=font.Font(family=Consts.DEFAULT_FONT_FAMILY,
                                                       size=Consts.DEFAULT_FONT_SIZE - 1), text=h)
                    surface.create_line(half_width - 3, (half_height - h), half_width + 3, half_height - h)
                    # negative y-axis
                    surface.create_text(half_width - 13, (half_height + h), fill=Colors.BLACK_HEX,
                                        font=font.Font(family=Consts.DEFAULT_FONT_FAMILY,
                                                       size=Consts.DEFAULT_FONT_SIZE - 1), text=h * -1)
                    surface.create_line(half_width - 3, (half_height + h), half_width + 3, half_height + h)

    def _draw_at_canvas(self, canvas: Canvas):
        surface: tk.Canvas = self.surfaces[canvas.tag]
        if surface is None:
            return
        color = Colors.BLACK_HEX
        # draw borders
        if canvas.show_border:
            # bottom
            surface.create_line(0, canvas.height, canvas.width, canvas.height)
            # top
            surface.create_line(0, 2, canvas.width, 2)
            # right
            surface.create_line(canvas.width, 0, canvas.width, canvas.height)
            # left
            surface.create_line(2, canvas.height, 2, 0)
        if canvas.show_cp:
            self._build_cp(canvas)
            for shape in canvas.shapes:
                for point in shape.points:
                    x = canvas.width / 2 + point.x
                    y = canvas.height - (canvas.height / 2 + point.y)
                    surface.create_oval(x, y, x, y, width=0, fill=color)
        else:
            for shape in canvas.shapes:
                for point in shape.points:
                    surface.create_oval(point.x, canvas.height - point.y, point.x, canvas.height - point.y,
                                        width=0, fill=color)
        # surface.pack(expand=tk.YES, fill=tk.BOTH)
        surface.pack(fill=tk.BOTH)

    def draw(self):
        for canvas in self.canvas_list:
            self._draw_at_canvas(canvas)
        try:
            self.screen.mainloop()
        except KeyboardInterrupt:
            pass


class Board:
    def __init__(self, screen: Screen):
        self._screen = screen

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, screen: Screen):
        self._screen = screen

    def draw_at(self):
        self.screen.draw()
