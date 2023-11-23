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

        permutations = all_permutations(numbersN)
       
        for i in range(N):
            m_color=rgb_to_color(colors[i])
            circle = Circle(color=m_color)
            circle.set_fill(m_color, opacity=0.7)
            circles.append(circle)

        
        tgt_point = ORIGIN
        for permutation in permutations:
            animations = []
            for i in range(N):
                circle = circles[i]
                end_point = (10*(permutation[i]/N-1/2+0.5/N), 0, 0)
                animation = ApplyMethod(circle.move_to, end_point)
                animations.append(animation)
                
            for animation in animations:
                self.play(animation)

            self.wait(1)
                
def random_color_generator():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def all_permutations(initialList):
    finalList = list(list())
    for initial in initialList:
        finalList.append([initial])
    for i in range(len(initialList)-1):
        finalList = add_one_item(finalList, initialList)

    return finalList



def add_one_item(itemListOfLists, initialList):
    finalList = list(list())
    for itemList in itemListOfLists:
        for initial in initialList:
            if(not (initial in itemList)):
                newList = itemList.copy()
                newList.append(initial)
                finalList.append(newList)
                

    return finalList
                

