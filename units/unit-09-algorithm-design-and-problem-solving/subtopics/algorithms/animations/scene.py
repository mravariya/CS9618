"""
Manim scenes for: Algorithms
Syllabus subtopic slug: algorithms
Render: manim -pql animations/scene.py AlgorithmsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class AlgorithmsModuleOverview(Scene):
    def construct(self):
        title = Text("Algorithms", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Algorithms as defined steps; identifier tables; pseudocode with input\u2013process\u2013output.", font_size=20, line_spacing=1.1)
        t1 = Text("Sequence, selection, iteration; document with structured English, flowchart, or pseudocode.", font_size=20, line_spacing=1.1)
        t2 = Text("Translate between structured English, flowchart, and pseudocode; stepwise refinement; logic statemen", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
