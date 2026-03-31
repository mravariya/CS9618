"""
Manim scenes for: Operating Systems
Syllabus subtopic slug: operating-systems
Render: manim -pql animations/scene.py OperatingSystemsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class OperatingSystemsModuleOverview(Scene):
    def construct(self):
        title = Text("Operating Systems", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Why an OS is needed; key tasks: memory, file, security, hardware/peripheral, process management.", font_size=20, line_spacing=1.1)
        t1 = Text("Utility software (formatter, antivirus, defrag, disk tools, compression, backup).", font_size=20, line_spacing=1.1)
        t2 = Text("Program libraries; benefits of library/DLL code in development.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
