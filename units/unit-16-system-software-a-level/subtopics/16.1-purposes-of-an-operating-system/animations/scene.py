"""
Manim scenes for: Purposes of an Operating System
Subtopic folder: 16.1-purposes-of-an-operating-system
Render: manim -pql animations/scene.py PurposesOfAnOperatingSystemModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class PurposesOfAnOperatingSystemModuleOverview(Scene):
    def construct(self):
        title = Text("Purposes of an Operating System", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("OS maximising resource use; UI hiding hardware complexity.", font_size=20, line_spacing=1.1)
        t1 = Text("Processes: multitasking, states (running, ready, blocked), scheduling algorithms.", font_size=20, line_spacing=1.1)
        t2 = Text("Kernel, interrupts, low-level scheduling; virtual memory, paging, segmentation, page replacement, th", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
