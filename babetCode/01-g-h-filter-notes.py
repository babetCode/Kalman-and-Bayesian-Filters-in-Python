# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import io
    from contextlib import redirect_stdout

    class UserEditor:
        """
        Creates an editor for the user to run code in.
        Example
        **cell 1**
        ``ue = UserEditor()
        run = ue.run``
        **cell 2**
        ``_ = run
        ue.display()``
        """
        def __init__(self, code="print('hi')", exec_func=lambda x: x):
            self.editor = mo.ui.code_editor(value=code)
            self.run = mo.ui.run_button(label="\>")
            self.exec_func = exec_func

        def display(self):
            buf = io.StringIO()
            code = self.exec_func(self.editor.value)
            print(code)
            try:
                with redirect_stdout(buf):
                    exec(code, {})
                output = buf.getvalue()
            except Exception as e:
                output = e
            return mo.vstack([self.run, self.editor, output])

    return UserEditor, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Alogithm
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Initialization**
    1. Initialize the state of the filter
    2. Initialize our belief in the state

    **Predict**
    1. Use system behavior to predict state at the next time step
    2. Adjust belief to account for the uncertainty in prediction

    **Update**
    1. Get a measurement and associated belief about its accuracy
    2. Compute residual between estimated state and measurement
    3. New estimate is somewhere on the residual line
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise: Write generic algorithm
    """)
    return


@app.cell
def _():
    algoritm_exercise = '''def g_h_filter(data, x0, dx, g, h, dt):
        """
        Performs g-h filter on 1 state variable with a fixed g and h.

        'data' contains the data to be filtered.
        'x0' is the initial value for our state variable
        'dx' is the initial change rate for our state variable
        'g' is the g-h's g scale factor
        'h' is the g-h's h scale factor
        'dt' is the length of the time step 
        """'''
    return (algoritm_exercise,)


@app.cell
def _(UserEditor, algoritm_exercise):
    ue = UserEditor(code=algoritm_exercise, exec_func=lambda x: x+r"\n\nprint(foobar)")
    run = ue.run
    return run, ue


@app.cell
def _(run, ue):
    _ = run
    ue.display()
    return


if __name__ == "__main__":
    app.run()
