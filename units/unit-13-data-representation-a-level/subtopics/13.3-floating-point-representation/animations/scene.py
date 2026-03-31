"""
Manim scenes for: Floating-point Representation and Manipulation
Subtopic folder: 13.3-floating-point-representation
Render: manim -pql animations/scene.py FloatingPointRepresentationModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class FloatingPointRepresentationModuleOverview(Scene):
    def construct(self):
        title = Text("Floating-point Representation and Manipulation", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Binary floating-point format; two\u2019s complement; mantissa/exponent trade-offs; denary conversion.", font_size=20, line_spacing=1.1)
        t1 = Text("Normalisation; approximation, rounding error; underflow/overflow.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
