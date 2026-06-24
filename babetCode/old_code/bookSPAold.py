import marimo

__generated_with = "0.23.10"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from pathlib import Path

    base = Path(__file__).resolve().parent.parent
    chapter_paths = [
        "00-Preface.ipynb",
        "01-g-h-filter.ipynb",
        "02-Discrete-Bayes.ipynb",
        "03-Gaussians.ipynb",
        "04-One-Dimensional-Kalman-Filters.ipynb",
        "05-Multivariate-Gaussians.ipynb",
        "06-Multivariate-Kalman-Filters.ipynb",
        "07-Kalman-Filter-Math.ipynb",
        "08-Designing-Kalman-Filters.ipynb",
        "09-Nonlinear-Filtering.ipynb",
        "10-Unscented-Kalman-Filter.ipynb",
        "11-Extended-Kalman-Filters.ipynb",
        "12-Particle-Filters.ipynb",
        "13-Smoothing.ipynb",
        "14-Adaptive-Filtering.ipynb",
    ]
    appendix_paths = [
        "Appendix-A-Installation.ipynb",
        "Appendix-B-Symbols-and-Notations.ipynb",
        "Appendix-D-HInfinity-Filters.ipynb",
        "Appendix-E-Ensemble-Kalman-Filters.ipynb",
        "Appendix-G-Designing-Nonlinear-Kalman-Filters.ipynb",
        "Appendix-H-Least-Squares-Filters.ipynb",
        "Appendix-I-Analytic-Evaluation-of-Performance.ipynb",
    ]
    all_paths = chapter_paths + appendix_paths
    return (all_paths,)


@app.cell
def _(all_paths, mo):
    def render_home():
        return mo.md(
            "\n\n".join(
                [s.replace(".ipynb", "") for s in all_paths]
            )
        )


    # def render_content():
    #     return mo.md("# Content")


    # def render_blog():
    #     return mo.md("# Blog")
    return (render_home,)


@app.cell
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "#/": "Home",
            # "Chapters": {
            #     f'#/{nb_path.replace(".ipynb", "")}': f'{nb_path.replace(".ipynb", "")}'
            #     for nb_path in all_paths
            # },
            "#/test": "test"
        },
        orientation="vertical",
    )

    mo.sidebar([nav_menu])
    return


@app.cell(column=1)
def _(mo):
    from nbconvert import HTMLExporter
    import nbformat

    def ipynb_to_iframe(notebook_path):

        # Load the file structural data
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb_node = nbformat.read(f, as_version=4)

        # Instantiate the exporter without the execution preprocessor
        html_exporter = HTMLExporter()
        html_body, _ = html_exporter.from_notebook_node(nb_node)

        # Wrap the generated HTML inside marimo's HTML rendering object
        return mo.iframe(html_body)

    return


@app.cell(hide_code=True)
def _():
    # from nbconvert import HTMLExporter
    # import nbformat

    # notebook_path = r"C:\Users\goper\files\vscode\Kalman-and-Bayesian-Filters-in-Python\01-g-h-filter.ipynb"

    # # Load the file structural data
    # with open(notebook_path, "r", encoding="utf-8") as f:
    #     nb_node = nbformat.read(f, as_version=4)

    # # Instantiate the exporter without the execution preprocessor
    # html_exporter = HTMLExporter()
    # html_body, _ = html_exporter.from_notebook_node(nb_node)

    # # Wrap the generated HTML inside marimo's HTML rendering object
    # mo.iframe(html_body)
    return


@app.cell
def _(mo, render_home):
    home_routes = {
        "#/": render_home,
        "#/test": lambda: "foobar",
        mo.routes.CATCH_ALL: render_home
    }

    page_routes = {
        # f'#/{nb_path.replace(".ipynb", "")}': (lambda: ipynb_to_iframe(nb_path))
        # for nb_path in all_paths
        "#/test": lambda: "foobar"
    }

    page = mo.routes(
        home_routes | page_routes
    )

    page
    return


if __name__ == "__main__":
    app.run()
