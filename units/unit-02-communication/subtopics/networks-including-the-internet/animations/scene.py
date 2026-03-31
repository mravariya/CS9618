"""
Manim scenes for: Networks Including the Internet
Syllabus subtopic slug: networks-including-the-internet
Render: manim -pql animations/scene.py NetworksIncludingTheInternetModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class NetworksIncludingTheInternetModuleOverview(Scene):
    def construct(self):
        title = Text("Networks Including the Internet", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Purpose/benefits of network devices; LAN vs WAN; client\u2013server vs peer-to-peer (roles, pros/cons, ju", font_size=20, line_spacing=1.1)
        t1 = Text("Thin vs thick client; bus, star, mesh, hybrid topologies; packet paths; justify topology.", font_size=20, line_spacing=1.1)
        t2 = Text("Cloud computing (public/private), benefits/drawbacks; wired vs wireless; media characteristics.", font_size=20, line_spacing=1.1)
        t3 = Text("LAN hardware: switch, server, NIC/WNIC, WAP, cables, bridge, repeater; router role.", font_size=20, line_spacing=1.1)
        t4 = Text("Ethernet, CSMA/CD; bit streaming (real-time vs on-demand) and bit rates.", font_size=20, line_spacing=1.1)
        t5 = Text("WWW vs internet; internet hardware (modem, PSTN, dedicated lines, cellular).", font_size=20, line_spacing=1.1)
        t6 = Text("IPv4/IPv6 format, subnetting, static vs dynamic, public vs private IPs; DNS and URLs.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2, t3, t4, t5, t6).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
