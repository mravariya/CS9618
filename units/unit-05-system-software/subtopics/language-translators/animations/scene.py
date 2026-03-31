"""
Manim scenes for: Language Translators
Syllabus subtopic slug: language-translators
Render: manim -pql animations/scene.py LanguageTranslatorsModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class LanguageTranslatorsModuleOverview(Scene):
    def construct(self):
        title = Text("Language Translators", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Need for assembler, compiler, interpreter; benefits/drawbacks; justify choice.", font_size=20, line_spacing=1.1)
        t1 = Text("Awareness of hybrid compile/interpret (e.g. Java console mode).", font_size=20, line_spacing=1.1)
        t2 = Text("Typical IDE features: coding aids, syntax checks, pretty-print, debugging (step, breakpoints, watch)", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
