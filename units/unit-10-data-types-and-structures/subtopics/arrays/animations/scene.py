"""
Manim scenes for: Arrays
Syllabus subtopic slug: arrays
Render: manim -pql animations/scene.py ArraysModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ArraysModuleOverview(Scene):
    def construct(self):
        title = Text("Arrays", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Terms: index, bounds; choose 1D/2D; pseudocode declarations and processing.", font_size=20, line_spacing=1.1)
        t1 = Text("Bubble sort; linear search.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
