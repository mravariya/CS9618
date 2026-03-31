"""
Manim scenes for: Program Design
Syllabus subtopic slug: program-design
Render: manim -pql animations/scene.py ProgramDesignModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ProgramDesignModuleOverview(Scene):
    def construct(self):
        title = Text("Program Design", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Structure charts: decomposition, parameters between modules; purpose; derive pseudocode.", font_size=20, line_spacing=1.1)
        t1 = Text("State-transition diagrams: purpose in documenting algorithms.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
