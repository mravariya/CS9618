"""
Manim scenes for: Structured Programming
Subtopic folder: 11.3-structured-programming
Render: manim -pql animations/scene.py StructuredProgrammingModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class StructuredProgrammingModuleOverview(Scene):
    def construct(self):
        title = Text("Structured Programming", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Procedures and functions; parameters by value/reference; headers, interfaces, arguments, return valu", font_size=20, line_spacing=1.1)
        t1 = Text("When to use procedures vs functions; write efficient pseudocode.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
