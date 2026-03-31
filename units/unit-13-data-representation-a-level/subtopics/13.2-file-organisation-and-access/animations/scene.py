"""
Manim scenes for: File Organisation and Access
Subtopic folder: 13.2-file-organisation-and-access
Render: manim -pql animations/scene.py FileOrganisationAndAccessModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class FileOrganisationAndAccessModuleOverview(Scene):
    def construct(self):
        title = Text("File Organisation and Access", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Serial, sequential (key), random (record key); appropriate organisation/access.", font_size=20, line_spacing=1.1)
        t1 = Text("Sequential vs direct access; hashing to read/write random/sequential files.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
