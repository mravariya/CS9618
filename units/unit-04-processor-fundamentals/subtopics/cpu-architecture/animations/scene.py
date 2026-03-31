"""
Manim scenes for: Central Processing Unit (CPU) Architecture
Syllabus subtopic slug: cpu-architecture
Render: manim -pql animations/scene.py CpuArchitectureModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class CpuArchitectureModuleOverview(Scene):
    def construct(self):
        title = Text("Central Processing Unit (CPU) Architecture", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Von Neumann model; stored program; registers (general vs special: PC, MDR, MAR, ACC, IX, CIR, Status", font_size=20, line_spacing=1.1)
        t1 = Text("ALU, CU, clock, IAS; buses (address, data, control); performance factors (cores, bus width, clock, c", font_size=20, line_spacing=1.1)
        t2 = Text("Ports (USB, HDMI, VGA); fetch\u2013execute cycle with register transfer notation.", font_size=20, line_spacing=1.1)
        t3 = Text("Interrupts: causes, uses, ISR, timing within F\u2013E cycle.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2, t3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
