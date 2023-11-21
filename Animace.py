from manim import *;
import itertools;
import random;


class CreateCircle(Scene):
    def construct(self):
        N = 3
        
        colors = []
        numbersN = []
        circles = []

        for i in range(N):
            color = random_color_generator()
            colors.append(color)

        for i in range(N):
            numbersN.append(i)

        permutations = itertools.permutations(numbersN)

        for i in range(N):
            m_color=rgb_to_color(colors[i])
            circle = Circle(color=m_color)
            circle.set_fill(m_color, opacity=0.7)
            circles.append(circle)

        for circle in circles:
            self.play(Create(circle))

        for permutation in permutations:
            for i in range(N):
                self.play(circles[i].move_to([0, permutation[i]/N, 0]))


        #square = Square(color=RED).shift(LEFT * 2)
        # circleRed = Circle(color=RED).shift(LEFT * 4)
        # circleRed.set_fill(RED, opacity=0.7)

        # circleGreen = Circle(color=GREEN)
        # circleGreen.set_fill(GREEN, opacity=0.7)
        # circleGreen.next_to(circleRed, RIGHT, buff=1)

        # circleBlue = Circle(color=BLUE)
        # circleBlue.set_fill(BLUE, opacity=0.7)
        # circleBlue.next_to(circleGreen, RIGHT, buff=1)

        # circleYellow = Circle(color=YELLOW)
        # circleYellow.set_fill(YELLOW, opacity=0.7)
        # circleYellow.next_to(circleBlue, RIGHT, buff=1)

        # circles = {circleRed, circleGreen, circleBlue, circleYellow}
        # for circle in circles:
        #     self.play(Create(circle))
        # self.wait()
        # for circle1 in circles:
        #     for circle2 in circles:
        #         self.play(Swap(circle1, circle2), run_time = 0.5)

# napsaní čtverce a kruhu na scénu
#self.play(Write(square), Write(circle))

# schování čtverce a kruhu ze scény
#self.play(FadeOut(square), FadeOut(circle), run_time=2)

def random_color_generator():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)