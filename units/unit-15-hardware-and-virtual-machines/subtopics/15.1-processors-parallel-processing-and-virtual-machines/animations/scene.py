"""
Manim scenes for: Processors, Parallel Processing and Virtual Machines
Subtopic folder: 15.1-processors-parallel-processing-and-virtual-machines
Render: manim -pql animations/scene.py ProcessorsParallelProcessingAndVirtualMachinesModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ProcessorsParallelProcessingAndVirtualMachinesModuleOverview(Scene):
    def construct(self):
        title = Text("Processors, Parallel Processing and Virtual Machines", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("RISC vs CISC; interrupts on both; pipelining/registers in RISC.", font_size=20, line_spacing=1.1)
        t1 = Text("Flynn: SISD, SIMD, MISD, MIMD; massively parallel systems.", font_size=20, line_spacing=1.1)
        t2 = Text("Virtual machines: concept, examples, benefits, limitations.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
