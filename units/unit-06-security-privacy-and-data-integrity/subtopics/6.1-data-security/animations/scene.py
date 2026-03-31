"""
Manim scenes for: Data Security
Subtopic folder: 6.1-data-security
Render: manim -pql animations/scene.py DataSecurityModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class DataSecurityModuleOverview(Scene):
    def construct(self):
        title = Text("Data Security", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Define security, privacy, integrity; need to protect data and systems.", font_size=20, line_spacing=1.1)
        t1 = Text("Security measures from standalone PC to networks (accounts, passwords, biometrics, firewall, AV, enc", font_size=20, line_spacing=1.1)
        t2 = Text("Threats: malware, hackers, phishing, pharming; mitigation methods; access rights.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
