import marimo

__generated_with = "0.23.10"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    # Added manually for import path functionality
    import sys
    from pathlib import Path
    parent_dir = Path(__file__).resolve().parent.parent.parent
    sys.path.append(str(parent_dir))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    [Table of Contents](./table_of_contents.ipynb)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Analytic Evaluation of Performance
    """)
    return


@app.cell
def _():
    #format the book
    # '%matplotlib inline' command supported automatically in marimo
    from book_format import load_style
    load_style()
    return


if __name__ == "__main__":
    app.run()
