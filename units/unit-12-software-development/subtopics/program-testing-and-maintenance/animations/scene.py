"""
Manim scenes for: Program Testing and Maintenance
Syllabus subtopic slug: program-testing-and-maintenance
Render: manim -pql animations/scene.py ProgramTestingAndMaintenanceModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ProgramTestingAndMaintenanceModuleOverview(Scene):
    def construct(self):
        title = Text("Program Testing and Maintenance", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Syntax, logic, runtime errors; locate and correct.", font_size=20, line_spacing=1.1)
        t1 = Text("Testing methods: dry run, walkthrough, white/black box, integration, alpha, beta, acceptance, stubs.", font_size=20, line_spacing=1.1)
        t2 = Text("Test strategy/plan; normal, abnormal, boundary data.", font_size=20, line_spacing=1.1)
        t3 = Text("Maintenance types: perfective, adaptive, corrective; enhance given programs.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2, t3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
