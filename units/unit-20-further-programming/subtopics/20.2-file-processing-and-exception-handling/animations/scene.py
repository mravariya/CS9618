"""
Manim scenes for: File Processing and Exception Handling
Subtopic folder: 20.2-file-processing-and-exception-handling
Render: manim -pql animations/scene.py FileProcessingAndExceptionHandlingModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class FileProcessingAndExceptionHandlingModuleOverview(Scene):
    def construct(self):
        title = Text("File Processing and Exception Handling", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Open/close files (read, write, append); read/write records; serial, sequential, random processing.", font_size=20, line_spacing=1.1)
        t1 = Text("Exceptions: importance, when to handle; write exception handling code.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
