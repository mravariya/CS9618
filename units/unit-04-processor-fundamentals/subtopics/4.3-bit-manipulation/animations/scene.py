"""
Manim scenes for: Bit Manipulation
Subtopic folder: 4.3-bit-manipulation
Render: manim -pql animations/scene.py BitManipulationModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class BitManipulationModuleOverview(Scene):
    def construct(self):
        title = Text("Bit Manipulation", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Logical, arithmetic, cyclic shifts (left/right).", font_size=20, line_spacing=1.1)
        t1 = Text("Bit masking to test/set bits; device monitor/control applications.", font_size=20, line_spacing=1.1)
        t2 = Text("AND, OR, XOR, LSL, LSR on ACC per syllabus.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
