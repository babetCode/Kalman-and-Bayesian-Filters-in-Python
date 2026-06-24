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

    return io, mo, redirect_stdout


@app.cell
def _(io, mo, redirect_stdout):
    class UserEditor:
        def __init__(self, code="print('hi')", exec_func=lambda x: x):
            self.editor = mo.ui.code_editor(value=code)
            self.run = mo.ui.run_button(label="\>")

        def display(self):
            buf = io.StringIO()
            try:
                with redirect_stdout(buf):
                    exec(self.editor.value, {})
                output = buf.getvalue()
            except Exception as e:
                output = e
            return mo.vstack([self.run, self.editor, output])

    return (UserEditor,)


@app.cell
def _(UserEditor):
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
