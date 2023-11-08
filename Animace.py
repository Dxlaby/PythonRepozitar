from manim import *;



class CreateCircle(Scene):
    def construct(self):
        #square = Square(color=RED).shift(LEFT * 2)
        circleRed = Circle(color=RED).shift(LEFT * 3)
        circleRed.set_fill(RED, opacity=0.7)

        circleGreen = Circle(color=GREEN)
        circleGreen.set_fill(GREEN, opacity=0.7)
        circleGreen.next_to(circleRed, RIGHT, buff=1)

        circleBlue = Circle(color=BLUE)
        circleBlue.set_fill(BLUE, opacity=0.7)
        circleBlue.next_to(circleGreen, RIGHT, buff=1)

        circles = {circleRed, circleBlue, circleGreen}
        for circle in circles:
            self.play(Create(circle))
        self.wait()
        for circle1 in circles:
            for circle2 in circles:
                self.play(Swap(circle1, circle2), run_time = 0.5)

# napsaní čtverce a kruhu na scénu
#self.play(Write(square), Write(circle))

# schování čtverce a kruhu ze scény
#self.play(FadeOut(square), FadeOut(circle), run_time=2)
