# from manim import *

# class Exercise(Scene):
#     def construct(self):
#         # Set background color and camera frame size
#         self.camera.background_color = WHITE
#         self.camera.frame_width = 9  # 1080x1920 aspect ratio
#         self.camera.frame_height = 16

#         # Define colors
#         text_color = BLACK
#         formula_color = "#0000FF"
#         brace_color = "#FF0000"

#         # Title using MathTex for LaTeX rendering
#         title = VGroup(
#             Text("Integration - Exercise 3", color=text_color).scale(0.7),
#             MathTex(r"\int \frac{1}{1 + x^3} \, dx", color=text_color).scale(0.7)
#         ).arrange(DOWN, buff=0.5).to_edge(UP, buff=1)
#         self.play(Write(title), run_time=2)
#         self.wait(1)
#         self.play(title.animate.shift(UP * 4.5)) #Adjusted shift
#         MathTex(r"", "")

#         # Define steps
#         steps = [
#             (r"\frac{1}{1 + x^3} = \frac{A}{1 - x} + \frac{B x + C}{1 + x + x^2}", "Use Partial Fractions"),
#             (r"1 = A(1 + x + x^2) + (B x + C)(1 - x)", "Solve for A, B, C"),
#             (r"""1 = &A + A x + A x^2 + B x \\
#                 &- B x^2 + C - C x""", "Expand the equation"),
#             (r"""1 = &(A + C) + (A + B - C)x\\
#                 &+ (A - B)x^2""", "Collect like terms"),
#             (r"""A + C = 1, A + B - C = 0 \\
#               A - B = 0""", "Solve the system"),
#             (r"A = \frac{1}{3}, \quad B = \frac{1}{3}, \quad C = \frac{2}{3}", "Find values of A, B, C"),
#             (r"\frac{1}{1 + x^3} = \frac{\frac{1}{3}}{1 - x} + \frac{\frac{1}{3} x + \frac{2}{3}}{1 + x + x^2}", "Rewrite the fraction"),
#             (r"\int \frac{1/3}{1 - x} \,dx + \int \frac{(1/3)x + (2/3)}{1 + x + x^2} \,dx", "Integrate separately"),
#             (r"""-\frac{1}{3} \ln |1 - x| + \frac{1}{3} \int \frac{x}{1 + x + x^2} \,dx + \\
#                 \frac{2}{3} \int \frac{1}{1 + x + x^2} \,dx""", "Compute integrals"),
#             (r"1 + x + x^2 = (x + \frac{1}{2})^2 + \frac{3}{4}", "Complete the square"),
#             (r"x + \frac{1}{2} = \frac{\sqrt{3}}{2} \tan \theta", "Use trigonometric substitution"),
#             (r"\frac{2}{\sqrt{3}} \tan^{-1} \left( \frac{2(x + 1/2)}{\sqrt{3}} \right)", "Solve the integral"),
#             (r"""-\frac{1}{3} \ln |1 - x| + \frac{1}{6} \ln |1 + x + x^2| + \\
#                 \frac{4}{3\sqrt{3}} \tan^{-1} \left( \frac{2(x + 1/2)}{\sqrt{3}} \right) + C""", "Final Expression")
#         ]

#         # Group to manage visible steps
#         step_group = VGroup()
#         max_visible_steps = 4
        # step_spacing = 4 if "\\" in step_group else 3
#         start_y = 4.5

#         for i, (formula, description) in enumerate(steps):
#             # Create step text and formula
#             step_text = Text(description, color=text_color).scale(0.5)
#             step_formula = MathTex(formula, color=formula_color)

#             step = VGroup(step_text, step_formula)
#             step_formula.next_to(step_text, buff=0.4, direction=DOWN) # correct usage of next_to.
#             step.move_to(UP * (start_y - len(step_group) * step_spacing))

#             # Check if we need to scroll
#             if len(step_group) >= max_visible_steps:
#                 self.play(*[mob.animate.shift(UP * step_spacing) for mob in step_group], run_time=1)
#                 self.play(FadeOut(step_group[0]), run_time=0.8)
#                 step_group.remove(step_group[0])

#             self.play(Write(step_text), Write(step_formula), run_time=1.5)
#             self.wait(0.8)
#             step_group.add(step)

#         # Box final answer
#         box = SurroundingRectangle(step_group[-1], color=brace_color, buff=0.2)
#         self.play(Create(box))
#         self.wait(2)

#         # Clear screen and replay step-by-step
#         self.play(FadeOut(step_group, box))
#         self.wait(1)

        # # Replay process step-by-step
        # for i, (formula, description) in enumerate(steps):
        #     replay_text = Text(description, color=text_color).scale(0.5).to_edge(UP)
        #     replay_formula = MathTex(formula, color=formula_color).next_to(replay_text, DOWN, buff=0.3)

        #     self.play(FadeIn(replay_text, replay_formula), run_time=1.5)
        #     self.wait(1.5)
        #     self.play(FadeOut(replay_text, replay_formula))

        # self.wait(2)

# from manim import *

# class CustomStepSpacing(Scene):
#     def construct(self):
#         self.camera.background_color = WHITE
#         self.camera.frame_width = 9  # 1080x1920 aspect ratio
#         self.camera.frame_height = 16

#         # Define colors
#         text_color = BLACK
#         formula_color = "#0000FF"
#         brace_color = "#FF0000"

#         step1 = MathTex("a + b = 2")
#         step2 = MathTex("a^2 - b")
#         step3 = MathTex("b = 4")

#         # Positioning manually
#         step1.to_edge(UP, buff=1)  # Place step1 closer to the top
#         step2.next_to(step1, DOWN, buff=0.5)  # Smaller space after step1
#         step3.next_to(step2, DOWN, buff=1.5)  # Larger space after step2

#         self.play(Write(step1))
#         self.wait(1)
#         self.play(Write(step2))
#         self.wait(1)
#         self.play(Write(step3))
#         self.wait(1)


from manim import *

class Exercise(Scene):
    def construct(self):
        # Set background color and camera frame size
        self.camera.background_color = WHITE
        self.camera.frame_width = 9  # 1080x1920 aspect ratio
        self.camera.frame_height = 16

        # Define colors
        text_color = BLACK
        formula_color = "#0000FF"
        brace_color = "#FF0000"

        # Title using MathTex for LaTeX rendering
        title = VGroup(
            Text("Integration - Exercise 3", color=text_color).scale(0.7),
            MathTex(r"\int \frac{1}{1 + x^3} \, dx", color=text_color).scale(0.7)
        ).arrange(DOWN, buff=0.5).to_edge(UP, buff=1)
        
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.shift(UP * 4.5)) #Adjusted shift

        # Define steps
        steps = [
            (r"\frac{1}{1 + x^3} = \frac{A}{1 - x} + \frac{B x + C}{1 + x + x^2}", "Use Partial Fractions"),
            (r"1 = A(1 + x + x^2) + (B x + C)(1 - x)", "Solve for A, B, C"),
            (r"1 = A + A x + A x^2 + B x - B x^2 + C - C x", "Expand the equation"),
            (r"1 = (A + C) + (A + B - C)x + (A - B)x^2", "Collect like terms"),
            (r"""A + C = 1, \\A + B - C = 0, \\A - B = 0""", "Solve the system"),
            (r"A = \frac{1}{3}, B = \frac{1}{3}, C = \frac{2}{3}", "Find values of A, B, C"),
            (r"\frac{1}{1 + x^3} = \frac{\frac{1}{3}}{1 - x} + \frac{\frac{1}{3} x + \frac{2}{3}}{1 + x + x^2}", "Rewrite the fraction"),
            (r"\int \frac{1/3}{1 - x} \,dx + \int \frac{(1/3)x + (2/3)}{1 + x + x^2} \,dx", "Integrate separately"),
            (r"""-\frac{1}{3} \ln |1 - x| + \frac{1}{3} \int \frac{x}{1 + x + x^2} \,dx \\+ \frac{2}{3} \int \frac{1}{1 + x + x^2} \,dx""", "Compute integrals"),
            (r"1 + x + x^2 = (x + \frac{1}{2})^2 + \frac{3}{4}", "Complete the square"),
            (r"x + \frac{1}{2} = \frac{\sqrt{3}}{2} \tan \theta", "Use trigonometric substitution"),
            (r"\frac{2}{\sqrt{3}} \tan^{-1} \left( \frac{2(x + 1/2)}{\sqrt{3}} \right)", "Solve the integral"),
            (r"""-\frac{1}{3} \ln |1 - x| + \frac{1}{6} \ln |1 + x + x^2| \\+ \frac{4}{3\sqrt{3}} \tan^{-1} \left( \frac{2(x + 1/2)}{\sqrt{3}} \right) + C""", "Final Expression")
        ]
        
        # Title fades out when steps start moving up
        self.wait(1)
        self.play(FadeOut(title), run_time=1.5)
        
        # Group to manage visible steps
        step_group = VGroup()
        max_visible_steps = 5
        step_spacing = 2.5 if "\\" in steps[0] else 2.25        
        bottom_padding = -3  # Ensuring padding from the bottom

        for i, (formula, description) in enumerate(steps):
            step_text = Text(description, color=text_color).scale(0.5)
            step_formula = MathTex(formula, color=formula_color).scale(0.8)
            step = VGroup(step_text, step_formula).arrange(DOWN, buff = 0.3)
            
            # Positioning the step properly with padding
            step.move_to(UP * (2 - len(step_group) * step_spacing) + DOWN * bottom_padding)

            # If max steps reached, move others up and fade out the first one
            if len(step_group) >= max_visible_steps:
                self.play(*[mob.animate.shift(UP * step_spacing) for mob in step_group], run_time=1)
                self.play(FadeOut(step_group[0]), run_time=0.8)
                step_group.remove(step_group[0])
            
            self.play(Write(step_text), Write(step_formula), run_time=1.5)
            self.wait(0.8)
            step_group.add(step)

        # Box final answer
        box = SurroundingRectangle(step_group[-1], color=brace_color, buff=0.2)
        self.play(Create(box))
        self.wait(2)

        # Clear screen and replay step-by-step
        self.play(FadeOut(step_group, box))
        self.wait(1)
