"""
Manim scenes for: Artificial Intelligence
Syllabus subtopic slug: artificial-intelligence
Render: manim -pql animations/scene.py ArtificialIntelligenceModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class ArtificialIntelligenceModuleOverview(Scene):
    def construct(self):
        title = Text("Artificial Intelligence", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Graphs for AI: structure; A* and Dijkstra (interpret given algorithms, not write graph setup).", font_size=20, line_spacing=1.1)
        t1 = Text("Neural networks and machine learning; deep, reinforcement learning; supervised vs unsupervised.", font_size=20, line_spacing=1.1)
        t2 = Text("Back propagation and regression (conceptual).", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
