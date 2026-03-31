"""
Manim scenes for: User-defined Data Types
Syllabus subtopic slug: user-defined-data-types
Render: manim -pql animations/scene.py UserDefinedDataTypesModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class UserDefinedDataTypesModuleOverview(Scene):
    def construct(self):
        title = Text("User-defined Data Types", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Why user-defined types are needed; enumerated, pointer; set, record, class/object; design for proble", font_size=20, line_spacing=1.1)
        grp = VGroup(t0).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
