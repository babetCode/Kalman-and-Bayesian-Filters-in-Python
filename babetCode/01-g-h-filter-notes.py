# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App(width="full")

with app.setup:
    import marimo as mo
    import utils


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # \(\alpha\)-\(\beta\) filter
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Description
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    The alpha-beta filter (aka g-h filter) is a simple signal filter.

    The filter uses a prediction (\(x'\)) and a measurement (\(z\)) to estimate a state (\(x\)). The gain (\(g\)) determines whether the measurement or the estimate is weighted more heavily:
    \[\text{estimate(}x\text{)} = \text{prediction(}x'\text{)} + \text{gain(}g\text{)} \cdot (\text{measurement(}z\text{)} - \text{prediction(}x'\text{)}).\]

    The difference \((\text{measurement}-\text{prediction})\) is called the residual (\(y\)), giving
    \[x = x' + g \cdot y.\]

    ---

    The implementation is as follows:

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
    ue = utils.UserEditor(code=algoritm_exercise, exec_func=lambda x: x+"\n\nprint('foobar')")
    run = ue.run
    return run, ue


@app.cell
def _(run, ue):
    _ = run
    ue.display()
    return


@app.cell
def _():
    mo.md("""
    /// details | Solution
        type: info
    ```py
    def g_h_filter(data, x0, dx, g, h, dt=1.):
        "\""
        Performs g-h filter on 1 state variable with a fixed g and h.
        'data' contains the data to be filtered.
        'x0' is the initial value for our state variable
        'dx' is the initial change rate for our state variable
        'g' is the g-h's g scale factor
        'h' is the g-h's h scale factor
        'dt' is the length of the time step
        "\""
        x_est = x0
        results = []
        for z in data:
            # prediction step
            x_pred = x_est + (dx*dt)
            dx = dx

            # update step
            residual = z - x_pred
            dx = dx + h * (residual) / dt
            x_est = x_pred + g * residual
            results.append(x_est)
        return np.array(results)
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
