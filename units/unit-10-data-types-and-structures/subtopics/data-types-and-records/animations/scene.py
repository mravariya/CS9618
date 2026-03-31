"""
Manim scenes for: Data Types and Records
Syllabus subtopic slug: data-types-and-records
Render: manim -pql animations/scene.py DataTypesAndRecordsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class DataTypesAndRecordsModuleOverview(Scene):
    def construct(self):
        title = Text("Data Types and Records", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Choose INTEGER, REAL, CHAR, STRING, BOOLEAN, DATE, ARRAY, FILE as appropriate.", font_size=20, line_spacing=1.1)
        t1 = Text("Purpose of records; pseudocode to define/read/write records.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
