"""
Manim scenes for: Encryption, Protocols and Digital Certificates
Syllabus subtopic slug: encryption-and-digital-certificates
Render: manim -pql animations/scene.py EncryptionAndDigitalCertificatesModuleOverview
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class EncryptionAndDigitalCertificatesModuleOverview(Scene):
    def construct(self):
        title = Text("Encryption, Protocols and Digital Certificates", font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
        t0 = Text("Symmetric vs asymmetric; keys, plaintext/ciphertext; private messaging and verified public messages.", font_size=20, line_spacing=1.1)
        t1 = Text("Quantum cryptography awareness; SSL/TLS purpose and use cases.", font_size=20, line_spacing=1.1)
        t2 = Text("Digital certificates and digital signatures.", font_size=20, line_spacing=1.1)
        grp = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
