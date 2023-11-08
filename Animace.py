from manim import *;


class CreateCircle(Scene):
    def construct(self):
        square = Square(color=RED).shift(LEFT * 2)
        circle = Circle(color=BLUE).shift(RIGHT * 2)
        self.play(Write(square), Write(circle))

# napsaní čtverce a kruhu na scénu
#self.play(Write(square), Write(circle))

# schování čtverce a kruhu ze scény
#self.play(FadeOut(square), FadeOut(circle), run_time=2)
