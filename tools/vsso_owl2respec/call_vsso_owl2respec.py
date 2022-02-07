import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

with open("./vsso_owl2respec.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

ep.preprocess(nb)


