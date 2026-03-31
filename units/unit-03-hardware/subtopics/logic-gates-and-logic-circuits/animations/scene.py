"""
Manim scenes for: Logic Gates and Logic Circuits
Syllabus subtopic slug: logic-gates-and-logic-circuits
Render: manim -pql animations/scene.py LogicGatesAndLogicCircuitsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class LogicGatesAndLogicCircuitsModuleOverview(Scene):
    def construct(self):
        title = Text("Logic Gates and Logic Circuits", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Use symbols for NOT, AND, OR, NAND, NOR, XOR; two inputs except NOT.", font_size=20, line_spacing=1.1)
        t1 = Text("Truth tables for each gate; build circuit from statement, expression, or table (and reverse).", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
