"""
Manim scenes for: Programming Paradigms
Syllabus subtopic slug: programming-paradigms
Render: manim -pql animations/scene.py ProgrammingParadigmsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ProgrammingParadigmsModuleOverview(Scene):
    def construct(self):
        title = Text("Programming Paradigms", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Meaning of paradigm; characteristics of low-level, imperative/procedural, OOP, declarative.", font_size=20, line_spacing=1.1)
        t1 = Text("Low-level: addressing modes; procedural: variables, constructs, subprograms; OOP: classes, inheritan", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
