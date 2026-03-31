"""
Manim scenes for: Program Development Life Cycle
Syllabus subtopic slug: program-development-lifecycle
Render: manim -pql animations/scene.py ProgramDevelopmentLifecycleModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ProgramDevelopmentLifecycleModuleOverview(Scene):
    def construct(self):
        title = Text("Program Development Life Cycle", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Purpose of life cycles; waterfall, iterative, RAD \u2014 principles, pros/cons.", font_size=20, line_spacing=1.1)
        t1 = Text("Analysis, design, coding, testing, maintenance stages.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
