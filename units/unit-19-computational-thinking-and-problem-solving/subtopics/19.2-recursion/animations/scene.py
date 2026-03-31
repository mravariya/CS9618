"""
Manim scenes for: Recursion
Subtopic folder: 19.2-recursion
Render: manim -pql animations/scene.py RecursionModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class RecursionModuleOverview(Scene):
    def construct(self):
        title = Text("Recursion", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Essential features; expression in a HLL; write and trace recursive algorithms.", font_size=20, line_spacing=1.1)
        t1 = Text("When recursion helps; compiler work (stacks, unwinding) \u2014 awareness.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
