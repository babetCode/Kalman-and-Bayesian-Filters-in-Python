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


@app.class_definition
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
        # print(code)
        try:
            with redirect_stdout(buf):
                exec(code, {})
            output = buf.getvalue()
        except Exception as e:
            output = e
        return mo.vstack([self.run, self.editor, output])


@app.cell
def _():
    ue = UserEditor()
    run = ue.run
    return run, ue


@app.cell
def _(run, ue):
    _ = run
    ue.display()
    return


if __name__ == "__main__":
    app.run()
