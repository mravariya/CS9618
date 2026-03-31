"""
Manim scenes for: DDL and DML (SQL)
Subtopic folder: 8.3-ddl-and-dml
Render: manim -pql animations/scene.py DdlAndDmlModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class DdlAndDmlModuleOverview(Scene):
    def construct(self):
        title = Text("DDL and DML (SQL)", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("DDL vs DML; SQL as industry standard; read/write simple DDL/DML as per syllabus subset.", font_size=20, line_spacing=1.1)
        t1 = Text("CREATE DATABASE/TABLE with listed data types; ALTER; PRIMARY KEY; FOREIGN KEY.", font_size=20, line_spacing=1.1)
        t2 = Text("Queries on \u22642 tables: SELECT, WHERE, ORDER BY, GROUP BY, INNER JOIN, aggregates; INSERT/DELETE/UPDAT", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
