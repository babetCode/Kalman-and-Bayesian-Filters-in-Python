# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App(width="full")

with app.setup:
    import marimo as mo

    import io
    from contextlib import redirect_stdout

    import inspect
    from hypothesis import find, strategies as st, settings, Phase
    from hypothesis.errors import NoSuchExample

    FAST_SETTINGS = settings(
        max_examples=100,       # Hypothesis default (thorough enough for ~100% confidence)
        database=None,          # CRITICAL: Prevents slow SQLite disk writes in Marimo
        phases=[Phase.generate, Phase.shrink]  # Skip explicit reuse phases to save time
    )


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## exec() testing
    """)
    return


@app.cell
def _():
    _bg_globals = {
        "inspect": inspect,
        "find": find, "st": st, "settings": settings, "Phase": Phase, # from hypothesis module
        "NoSuchExample": NoSuchExample, # from hypothesis.errors
        "x": 5
    }

    _output_locals = {}

    _code = """
    import os                  # An import inside the block
    y = x + 5                  # A variable creation
    def greet(): return "Hi"   # A function creation
    """

    exec(_code, _bg_globals, _output_locals)

    print(_output_locals.keys())
    print(_output_locals["y"]) 
    return


@app.cell(hide_code=True)
def _():
    import math

    # Create an environment and pass the math module and a variable into it
    my_env = {
        "math": math,
        "radius": 5
    }

    # The code string uses both 'math' and 'radius'
    _code = "area = math.pi * (radius ** 2)"

    exec(_code, my_env)

    # The result is saved back into the environment dictionary
    print(my_env["area"])  # Output: 78.53981633974483
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## is_equivalent
    """)
    return


@app.function
def is_equivalent(func1, func2) -> bool:
    """
    Uses hypothesis to test function equivalence.
    If functions are equivalent, returns True.
    """
    # 2. Match parameter lengths instantly to avoid slow engine startups
    sig1 = inspect.signature(func1)
    sig2 = inspect.signature(func2)
    if len(sig1.parameters) != len(sig2.parameters):
        return False

    # 3. Dynamically build strict strategies using type hints
    argument_strategies = []
    for param in sig1.parameters.values():
        hint = param.annotation

        # Fallback to integer if the student didn't type-hint
        if hint == inspect.Parameter.empty:
            hint = int

        # st.from_type natively handles int, float, str, bool, List[int], etc.
        # We filter out infinite/NaN floats as they ruin simple == assertions
        if hint is float:
            strategy = st.floats(allow_nan=False, allow_infinity=False)
        else:
            strategy = st.from_type(hint)

        argument_strategies.append(strategy)

    # 4. Define the falsification condition
    def is_different(args):
        try:
            return func1(*args) != func2(*args)
        except Exception:
            # If the student's code crashes on a valid input, it's an error
            return True

    # 5. Execute using find() wrapped in our fast settings profile
    try:
        find(
            st.tuples(*argument_strategies), 
            is_different, 
            settings=FAST_SETTINGS
        )
        return False  # Counterexample found! Functions are NOT equivalent.
    except NoSuchExample:
        return True


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### test is_equivalent()
    """)
    return


@app.cell
def _():
    import numpy as np

    def py_square(x):
        return x**2

    def mu_square(x):
        y = x
        return x*y

    is_equivalent(py_square, mu_square)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## UserEditor
    """)
    return


@app.class_definition
class UserEditor:
    """
    Lets the user write code and run it.
    Example use:
    **Cell 1**
    ``ue_example = UserEditor()
    run_example = ue.run_button``
    **Cell 2**
    ``_ = run_example
    ue_example.display()``
    """
    def __init__(self, code="print('hello')"):
        self.editor = mo.ui.code_editor(value=code)
        self.run_button = mo.ui.run_button(label="run")

    def display(self, sandbox_globals={}):
        buf = io.StringIO()
        sandbox_locals={}
        try:
            with redirect_stdout(buf):
                exec(self.editor.value, sandbox_globals, sandbox_locals)
            output = buf.getvalue()
        except Exception as e:
            output = e
        return sandbox_locals, self.editor, self.run_button, output

    # def is_func_equiv(self, func_input_name:str, func_solution_name:str, func_solution:str)->bool:
    #     bg_globals = {
    #         "inspect": inspect,
    #         "find": find, "st": st, "settings": settings, "Phase": Phase, # from hypothesis module
    #         "NoSuchExample": NoSuchExample, # from hypothesis.errors
    #         "x": 5
    #     }

    #     output_locals = {}

    #     buf = io.StringIO()
    #     try:
    #         with redirect_stdout(buf):
    #             exec(code, {})
    #         output = buf.getvalue()
    #     except Exception as e:
    #         output = e
    #     return output


@app.cell
def _():
    ue = UserEditor()
    run = ue.run_button
    return run, ue


@app.cell
def _(run, ue):
    _ = run
    ue.display()
    return


if __name__ == "__main__":
    app.run()
