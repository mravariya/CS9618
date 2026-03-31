"""
Manim scenes for: Circuit Switching and Packet Switching
Subtopic folder: 14.2-circuit-switching-and-packet-switching
Render: manim -pql animations/scene.py CircuitSwitchingAndPacketSwitchingModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class CircuitSwitchingAndPacketSwitchingModuleOverview(Scene):
    def construct(self):
        title = Text("Circuit Switching and Packet Switching", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Circuit switching: benefits, drawbacks, where used.", font_size=20, line_spacing=1.1)
        t1 = Text("Packet switching: benefits, drawbacks; router role; message delivery across networks/internet.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
