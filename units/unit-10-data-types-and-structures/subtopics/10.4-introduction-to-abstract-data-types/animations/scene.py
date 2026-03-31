"""
Manim scenes for: Introduction to Abstract Data Types (ADT)
Subtopic folder: 10.4-introduction-to-abstract-data-types
Render: manim -pql animations/scene.py IntroductionToAbstractDataTypesModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class IntroductionToAbstractDataTypesModuleOverview(Scene):
    def construct(self):
        title = Text("Introduction to Abstract Data Types (ADT)", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("ADT = data + operations; stack, queue, linked list \u2014 features and justification.", font_size=20, line_spacing=1.1)
        t1 = Text("Manipulate data in these structures (no pseudocode for structure ops at AS intro).", font_size=20, line_spacing=1.1)
        t2 = Text("Implement stack, queue, linked list using arrays.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
