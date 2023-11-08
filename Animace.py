from manim import *;


class CreateCircle(Scene):
    def construct(self):
        #square = Square(color=RED).shift(LEFT * 2)
        circleBlue = Circle(color=BLUE).shift(RIGHT * 2)
        circleBlue.set_fill(BLUE, opacity=1)
        circleRed = Circle(color=RED).shift(RIGHT * 1)
        circleRed.set_fill(RED, opacity=1)
        self.play(Write(circleRed), Write(circleBlue))

# napsaní čtverce a kruhu na scénu
#self.play(Write(square), Write(circle))

# schování čtverce a kruhu ze scény
#self.play(FadeOut(square), FadeOut(circle), run_time=2)
