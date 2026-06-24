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
    return all_paths, chapter_paths


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
def _(all_paths, ipynb_to_iframe, mo):
    chap_tabs = mo.ui.tabs({
        f'{nb_path.replace(".ipynb", "")}': ipynb_to_iframe(nb_path)
        for nb_path in all_paths[:2]
    })
    chap_tabs
    return


@app.cell
def _(chapter_paths, ipynb_to_iframe, mo, render_home):
    nav_tabs = mo.ui.tabs(
        {
            "Home": render_home(),
            # "Chapters": {
            #     f'#/{nb_path.replace(".ipynb", "")}': f'{nb_path.replace(".ipynb", "")}'
            #     for nb_path in all_paths
            # },
            "Test":ipynb_to_iframe(chapter_paths[0])
        },
        # orientation="vertical",
    )

    nav_tabs
    return


@app.cell
def _(page):
    page.text
    return


@app.cell(column=1)
def _():
    from nbconvert import HTMLExporter
    import nbformat
    from bs4 import BeautifulSoup

    def ipynb_to_html(notebook_path):
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb_node = nbformat.read(f, as_version=4)

        exporter = HTMLExporter()
        html_doc, _ = exporter.from_notebook_node(nb_node)

        soup = BeautifulSoup(html_doc, "html.parser")

        styles = "".join(str(tag) for tag in soup.find_all("style"))
        content = str(soup.find("body"))

        return f"""
            {styles}
            <style>
            .embedded-notebook {{
                background: white;
                padding: 1rem;
            }}
            </style>
            <div class="embedded-notebook">
            {content}
            </div>
            """
        # return f"{styles}\n{content}"
    return HTMLExporter, ipynb_to_html, nbformat


@app.cell
def _(HTMLExporter, mo, nbformat):
    def ipynb_to_iframe(notebook_path):

        # Load the file structural data
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb_node = nbformat.read(f, as_version=4)

        # Instantiate the exporter without the execution preprocessor
        html_exporter = HTMLExporter()
        html_body, _ = html_exporter.from_notebook_node(nb_node)

        # Wrap the generated HTML inside marimo's HTML rendering object
        return mo.iframe(html_body)

    return (ipynb_to_iframe,)


@app.cell
def _(chapter_paths, ipynb_to_html, mo):
    mo.Html(ipynb_to_html(chapter_paths[0]))
    return


@app.cell
def _(chapter_paths, ipynb_to_html, mo, render_home):
    home_routes = {
        "#/": render_home,
        "#/test": lambda: "foobar",
        mo.routes.CATCH_ALL: render_home
    }

    page_routes = {
        # f'#/{nb_path.replace(".ipynb", "")}': lambda: mo.Html(ipynb_to_html(nb_path))
        # for nb_path in all_paths
        "#/test": lambda: mo.Html(ipynb_to_html(chapter_paths[0]))
    }

    page = mo.routes(
        home_routes | page_routes
    )

    page
    return (page,)


if __name__ == "__main__":
    app.run()
