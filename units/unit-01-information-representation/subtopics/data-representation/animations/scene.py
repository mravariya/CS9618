"""
CS9618 — Section 1.1 Data Representation
Manim Community scenes (3Blue1Brown-style pedagogy).

Render examples:
    manim -pql animations/scene.py Topic11TitleCard
    manim -pql animations/scene.py WhyBinaryScene
"""
from manim import BLUE, DOWN, GREEN, LEFT, ORANGE, RIGHT, UP, FadeIn, FadeOut, Scene, Text, VGroup


class Topic11TitleCard(Scene):
    def construct(self):
        t1 = Text("Cambridge 9618 — 1.1", font_size=36)
        t2 = Text("Data Representation", font_size=52)
        sub = Text("Bits, bases, prefixes, signed integers, characters", font_size=22)
        grp = VGroup(t1, t2, sub).arrange(DOWN, buff=0.35)
        self.play(FadeIn(grp, shift=0.2 * DOWN))
        self.wait(2.5)
        self.play(FadeOut(grp))


class WhyBinaryScene(Scene):
    def construct(self):
        title = Text("Why binary?", font_size=40).to_edge(UP)
        self.play(FadeIn(title))
        hi = Text("HIGH", font_size=32, color=GREEN)
        lo = Text("LOW", font_size=32, color=BLUE)
        lo.shift(2 * LEFT)
        hi.shift(2 * RIGHT)
        gap = Text("clear gap → reliable detection", font_size=22).next_to(VGroup(lo, hi), DOWN, buff=0.8)
        self.play(FadeIn(lo), FadeIn(hi))
        self.play(FadeIn(gap))
        self.wait(2)
        bridge = Text("Two states → one bit (0 or 1)", font_size=28).next_to(gap, DOWN, buff=0.6)
        self.play(FadeIn(bridge))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, lo, hi, gap, bridge)))


class PowersOfTwoNumberLine(Scene):
    def construct(self):
        title = Text("Place value: powers of two (8 bits)", font_size=32).to_edge(UP)
        self.play(FadeIn(title))
        labels = []
        for i in range(8):
            val = 2 ** (7 - i)
            bit_pos = f"bit{7 - i}"
            labels.append(Text(f"{bit_pos}: 2^{7 - i} = {val}", font_size=20))
        col = VGroup(*labels).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        col.next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=0.3)
        self.play(FadeIn(col, lag_ratio=0.15))
        self.wait(2)
        hint = Text("Add selected powers → unsigned denary value", font_size=22, color=ORANGE)
        hint.next_to(col, DOWN, buff=0.5)
        self.play(FadeIn(hint))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, col, hint)))


class KibiVsKiloComparison(Scene):
    def construct(self):
        title = Text("Kibi vs kilo (know both stories)", font_size=34).to_edge(UP)
        self.play(FadeIn(title))
        left = VGroup(
            Text("IEC binary", font_size=28),
            Text("1 KiB = 1024 B", font_size=24),
            Text("1 MiB = 1024 KiB", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT).shift(2.2 * LEFT)
        right = VGroup(
            Text("SI / decimal", font_size=28),
            Text("1 kB = 1000 B", font_size=24),
            Text("(when used that way)", font_size=20, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT).shift(2.2 * RIGHT)
        self.play(FadeIn(left), FadeIn(right))
        mid = Text("Close words, different counts", font_size=26).next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(mid))
        self.wait(2.5)
        exam = Text("Examiners reward precise terminology", font_size=22).to_edge(DOWN)
        self.play(FadeIn(exam))
        self.wait(2)
        self.play(FadeOut(VGroup(title, left, right, mid, exam)))


class HexNibbleBridge(Scene):
    def construct(self):
        title = Text("One byte ↔ two hex digits", font_size=34).to_edge(UP)
        self.play(FadeIn(title))
        byte_txt = Text("11001101", font_size=36)
        n1 = Text("1100", font_size=32, color=BLUE).next_to(byte_txt, UP, buff=0.8)
        n2 = Text("1101", font_size=32, color=GREEN).next_to(byte_txt, UP, buff=0.8)
        # position nibbles above left/right halves — simplified layout
        n1.shift(1.8 * LEFT)
        n2.shift(1.8 * RIGHT)
        h1 = Text("C", font_size=40, color=BLUE).next_to(n1, UP, buff=0.3)
        h2 = Text("D", font_size=40, color=GREEN).next_to(n2, UP, buff=0.3)
        self.play(FadeIn(byte_txt))
        self.play(FadeIn(VGroup(n1, n2)))
        self.play(FadeIn(VGroup(h1, h2)))
        arrow = Text("4 bits = 1 hex digit (nibble)", font_size=22).to_edge(DOWN)
        self.play(FadeIn(arrow))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, byte_txt, n1, n2, h1, h2, arrow)))


class TwosComplementStory(Scene):
    def construct(self):
        title = Text("Two's complement (8-bit sketch)", font_size=32).to_edge(UP)
        self.play(FadeIn(title))
        p = Text("+42  →  00101010", font_size=28)
        inv = Text("invert → 11010101", font_size=26, color=ORANGE)
        add1 = Text("+1   →  11010110   (= −42)", font_size=28, color=GREEN)
        grp = VGroup(p, inv, add1).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.3)
        self.play(FadeIn(p))
        self.play(FadeIn(inv))
        self.play(FadeIn(add1))
        note = Text("Same adder hardware; MSB is sign bit", font_size=22).next_to(grp, DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(3)
        self.play(FadeOut(VGroup(title, grp, note)))


class UnicodeMosaic(Scene):
    def construct(self):
        title = Text("Characters need agreed standards", font_size=32).to_edge(UP)
        self.play(FadeIn(title))
        samples = VGroup(
            Text("ASCII — foundational English/control", font_size=22),
            Text("Extended ASCII — code pages (limited)", font_size=22),
            Text("Unicode — universal repertoire + UTF-8/16…", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        samples.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.3)
        self.play(FadeIn(samples, lag_ratio=0.2))
        tail = Text("Syllabus: concepts, not memorising code tables", font_size=22, color=ORANGE).to_edge(DOWN)
        self.play(FadeIn(tail))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, samples, tail)))
