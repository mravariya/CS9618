"""
Manim scenes for: Protocols
Subtopic folder: 14.1-protocols
Render: manim -pql animations/scene.py ProtocolsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ProtocolsModuleOverview(Scene):
    def construct(self):
        title = Text("Protocols", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Why protocols matter; layered stacks and responsibilities.", font_size=20, line_spacing=1.1)
        t1 = Text("TCP/IP four layers; message path between hosts.", font_size=20, line_spacing=1.1)
        t2 = Text("HTTP, FTP, POP3, IMAP, SMTP, BitTorrent purposes.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
