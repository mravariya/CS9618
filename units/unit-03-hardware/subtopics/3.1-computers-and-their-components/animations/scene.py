"""
Manim scenes for: Computers and Their Components
Subtopic folder: 3.1-computers-and-their-components
Render: manim -pql animations/scene.py ComputersAndTheirComponentsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ComputersAndTheirComponentsModuleOverview(Scene):
    def construct(self):
        title = Text("Computers and Their Components", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Need for input, output, primary memory, secondary/removable storage; embedded systems pros/cons.", font_size=20, line_spacing=1.1)
        t1 = Text("Principal operations of listed devices (e.g. laser/3D printer, mic, speakers, HDD, SSD, optical, tou", font_size=20, line_spacing=1.1)
        t2 = Text("Buffers; RAM vs ROM; SRAM vs DRAM; PROM, EPROM, EEPROM.", font_size=20, line_spacing=1.1)
        t3 = Text("Monitoring vs control; sensors and actuators; feedback.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2, t3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
