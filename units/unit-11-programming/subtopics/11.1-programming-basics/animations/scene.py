"""
Manim scenes for: Programming Basics
Subtopic folder: 11.1-programming-basics
Render: manim -pql animations/scene.py ProgrammingBasicsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ProgrammingBasicsModuleOverview(Scene):
    def construct(self):
        title = Text("Programming Basics", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Implement pseudocode from flowchart/structured English.", font_size=20, line_spacing=1.1)
        t1 = Text("Declarations, assignment, expressions, console I/O; built-in/library routines as provided in exam.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
