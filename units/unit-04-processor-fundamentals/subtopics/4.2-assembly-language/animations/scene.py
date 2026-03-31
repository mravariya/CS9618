"""
Manim scenes for: Assembly Language
Subtopic folder: 4.2-assembly-language
Render: manim -pql animations/scene.py AssemblyLanguageModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class AssemblyLanguageModuleOverview(Scene):
    def construct(self):
        title = Text("Assembly Language", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Assembly vs machine code; two-pass assembler stages; trace simple programs.", font_size=20, line_spacing=1.1)
        t1 = Text("Instruction groups: data movement, I/O, arithmetic, unconditional/conditional, compare.", font_size=20, line_spacing=1.1)
        t2 = Text("Addressing modes: immediate, direct, indirect, indexed, relative; use syllabus instruction set.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
