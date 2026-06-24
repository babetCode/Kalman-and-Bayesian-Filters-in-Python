# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App(width="full")

with app.setup:
    import marimo as mo
    from chap_note_utils import UserEditor


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Algorithm
    """)
    return


@app.cell(hide_code=True)
def _():
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
def _():
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
def _(algoritm_exercise):
    ue = UserEditor(code=algoritm_exercise, exec_func=lambda x: x+"\n\nprint('foobar')")
    run = ue.run
    return run, ue


@app.cell
def _(run, ue):
    _ = run
    ue.display()
    return


if __name__ == "__main__":
    app.run()
