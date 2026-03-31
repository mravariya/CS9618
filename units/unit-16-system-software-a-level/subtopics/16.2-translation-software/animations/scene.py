"""
Manim scenes for: Translation Software
Subtopic folder: 16.2-translation-software
Render: manim -pql animations/scene.py TranslationSoftwareModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class TranslationSoftwareModuleOverview(Scene):
    def construct(self):
        title = Text("Translation Software", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Interpreter execution without full translated program; compiler stages: lexical/syntax analysis, cod", font_size=20, line_spacing=1.1)
        t1 = Text("Syntax diagrams or BNF; Reverse Polish Notation evaluation.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
