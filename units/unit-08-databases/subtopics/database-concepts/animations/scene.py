"""
Manim scenes for: Database Concepts
Syllabus subtopic slug: database-concepts
Render: manim -pql animations/scene.py DatabaseConceptsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class DatabaseConceptsModuleOverview(Scene):
    def construct(self):
        title = Text("Database Concepts", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Limitations of file-based storage/retrieval vs relational model features.", font_size=20, line_spacing=1.1)
        t1 = Text("Relational terminology: entity, table, record, field, tuple, attribute, keys, relationships, referen", font_size=20, line_spacing=1.1)
        t2 = Text("E\u2013R diagrams; normalisation to 1NF, 2NF, 3NF; explain/produce normalised designs.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
