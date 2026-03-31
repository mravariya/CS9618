"""
Manim scenes for: Data Integrity
Syllabus subtopic slug: data-integrity
Render: manim -pql animations/scene.py DataIntegrityModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class DataIntegrityModuleOverview(Scene):
    def construct(self):
        title = Text("Data Integrity", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("How validation and verification support integrity.", font_size=20, line_spacing=1.1)
        t1 = Text("Validation: range, format, length, presence, existence, limit, check digit.", font_size=20, line_spacing=1.1)
        t2 = Text("Verification on entry (visual, double entry) and transfer (parity byte/block, checksum).", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
