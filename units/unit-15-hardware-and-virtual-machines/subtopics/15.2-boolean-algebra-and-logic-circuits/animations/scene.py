"""
Manim scenes for: Boolean Algebra and Logic Circuits
Subtopic folder: 15.2-boolean-algebra-and-logic-circuits
Render: manim -pql animations/scene.py BooleanAlgebraAndLogicCircuitsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class BooleanAlgebraAndLogicCircuitsModuleOverview(Scene):
    def construct(self):
        title = Text("Boolean Algebra and Logic Circuits", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Truth tables including half/full adders; multi-input gates possible.", font_size=20, line_spacing=1.1)
        t1 = Text("SR/JK flip-flops: circuit, table, storage role.", font_size=20, line_spacing=1.1)
        t2 = Text("Boolean algebra, De Morgan\u2019s laws, simplification; Karnaugh maps: benefits and use.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
