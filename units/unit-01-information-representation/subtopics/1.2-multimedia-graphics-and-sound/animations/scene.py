"""
Manim scenes for: Multimedia — Graphics and Sound
Subtopic folder: 1.2-multimedia-graphics-and-sound
Render: manim -pql animations/scene.py MultimediaGraphicsAndSoundModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class MultimediaGraphicsAndSoundModuleOverview(Scene):
    def construct(self):
        title = Text("Multimedia \u2014 Graphics and Sound", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Bitmaps: pixels, header, image/screen resolution, colour depth; estimate file size; effects on quali", font_size=20, line_spacing=1.1)
        t1 = Text("Vectors: drawing objects, properties, drawing list; choose bitmap vs vector with justification.", font_size=20, line_spacing=1.1)
        t2 = Text("Sound: sampling, sampling rate, resolution, analogue vs digital; impact on file size and accuracy.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
