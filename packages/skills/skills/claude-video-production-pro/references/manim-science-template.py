from manim import *

# Pin the font in the project manifest and test actual shaping in a rendered frame.
AR_FONT = "Noto Naskh Arabic"

class ArabicPythagoreanScene(Scene):
    def construct(self):
        title = Text("نظرية فيثاغورس", font=AR_FONT, font_size=44)
        title.to_edge(UP)
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=58)
        formula.next_to(title, DOWN, buff=0.45)
        triangle = Polygon(ORIGIN, RIGHT * 3, RIGHT * 3 + UP * 2, color=TEAL)
        triangle.shift(DOWN * 0.8)
        labels = VGroup(
            Text("a", font=AR_FONT, font_size=30).next_to(triangle.get_left(), LEFT),
            Text("b", font=AR_FONT, font_size=30).next_to(triangle.get_right(), RIGHT),
            Text("c", font=AR_FONT, font_size=30).next_to(triangle.get_top(), UP),
        )
        self.play(Write(title), Write(formula))
        self.play(Create(triangle), FadeIn(labels))
        self.wait(1)
