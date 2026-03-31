"""
Manim scenes for: Files
Syllabus subtopic slug: files
Render: manim -pql animations/scene.py FilesModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class FilesModuleOverview(Scene):
    def construct(self):
        title = Text("Files", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Why files exist; pseudocode for text files with one or more lines.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
