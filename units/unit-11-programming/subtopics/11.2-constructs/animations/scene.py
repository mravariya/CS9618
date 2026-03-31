"""
Manim scenes for: Constructs
Subtopic folder: 11.2-constructs
Render: manim -pql animations/scene.py ConstructsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ConstructsModuleOverview(Scene):
    def construct(self):
        title = Text("Constructs", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("IF/ELSE (nested), CASE; count-controlled, post-condition, pre-condition loops; justify loop choice.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
