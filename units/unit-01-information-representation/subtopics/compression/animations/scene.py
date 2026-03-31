"""
Manim scenes for: Compression
Syllabus subtopic slug: compression
Render: manim -pql animations/scene.py CompressionModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class CompressionModuleOverview(Scene):
    def construct(self):
        title = Text("Compression", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Explain why compression is needed; give examples of use.", font_size=20, line_spacing=1.1)
        t1 = Text("Compare lossy vs lossless; justify a method for a situation.", font_size=20, line_spacing=1.1)
        t2 = Text("Describe how text, bitmap, vector, and sound may be compressed, including run-length encoding (RLE).", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
