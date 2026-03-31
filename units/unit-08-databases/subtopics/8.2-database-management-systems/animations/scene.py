"""
Manim scenes for: Database Management Systems (DBMS)
Subtopic folder: 8.2-database-management-systems
Render: manim -pql animations/scene.py DatabaseManagementSystemsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class DatabaseManagementSystemsModuleOverview(Scene):
    def construct(self):
        title = Text("Database Management Systems (DBMS)", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("DBMS features vs file-based approach: dictionary, modelling, logical schema, integrity, security, ba", font_size=20, line_spacing=1.1)
        t1 = Text("Developer interface; query processor roles.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
