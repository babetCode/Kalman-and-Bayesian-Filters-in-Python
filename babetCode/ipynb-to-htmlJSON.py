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

    return


@app.cell
def _():
    from nbconvert import HTMLExporter
    import nbformat

    def ipynb_to_html(notebook_path, dark=True):
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb_node = nbformat.read(f, as_version=4)

        nb_node.metadata.pop("widgets", None)

        html_exporter = (
            HTMLExporter(template_name="lab", theme="dark")
            if dark
            else HTMLExporter()
        )
        html_body, _ = html_exporter.from_notebook_node(nb_node)
        return html_body

    return (ipynb_to_html,)


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
def _(all_paths, ipynb_to_html):
    my_dict = {
        p.replace(".ipynb", ""): ipynb_to_html(p) for p in all_paths
    }
    return (my_dict,)


@app.cell
def _(my_dict):
    import json

    with open(r"C:\Users\goper\Files\vsCode\Kalman-and-Bayesian-Filters-in-Python\babetCode\chapters-html.json", "w") as f:
        json.dump(my_dict, f, indent=2)
    return


if __name__ == "__main__":
    app.run()
