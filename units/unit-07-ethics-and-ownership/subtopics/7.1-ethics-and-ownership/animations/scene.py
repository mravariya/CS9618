"""
Manim scenes for: Ethics and Ownership
Subtopic folder: 7.1-ethics-and-ownership
Render: manim -pql animations/scene.py EthicsAndOwnershipModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class EthicsAndOwnershipModuleOverview(Scene):
    def construct(self):
        title = Text("Ethics and Ownership", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Need/purpose of ethics for computing professionals; professional bodies (e.g. BCS, IEEE).", font_size=20, line_spacing=1.1)
        t1 = Text("Ethical vs unethical impact in scenarios; copyright; licence types and justification (FSF, OSI, shar", font_size=20, line_spacing=1.1)
        t2 = Text("AI: social, economic, environmental impact; applications of AI.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
