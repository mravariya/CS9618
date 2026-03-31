"""
Manim scenes for: Algorithms and Abstract Data Types
Syllabus subtopic slug: algorithms-and-adts
Render: manim -pql animations/scene.py AlgorithmsAndAdtsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class AlgorithmsAndAdtsModuleOverview(Scene):
    def construct(self):
        title = Text("Algorithms and Abstract Data Types", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Linear vs binary search \u2014 write, conditions for binary, performance vs size.", font_size=20, line_spacing=1.1)
        t1 = Text("Insertion sort and bubble sort \u2014 write; performance depends on order and n.", font_size=20, line_spacing=1.1)
        t2 = Text("ADT operations: search/insert/delete on linked list, binary tree; stack, queue, linked list algorith", font_size=20, line_spacing=1.1)
        t3 = Text("Graph as ADT; implementing ADTs from built-ins or other ADTs; dictionary, binary tree.", font_size=20, line_spacing=1.1)
        t4 = Text("Compare algorithms; Big O for time and space.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2, t3, t4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
