## Create Respec from `VSSo(-core)`

This folder contains a tool to create the specification
of the core ontology of VSSo and the vocabulary generated
from the [Vehicle Signal Specification (VSS)](https://https://github.com/COVESA/vehicle_signal_specification)

### Usage

#### Setup

The tool uses [pipenv](https://pipenv.pypa.io/en/latest/).
Please follow their instructions for installation.

After pipenv is installed, run:

```bash
pipenv install
``` 

This creates a virtual environment, with the necessary dependencies.

#### Run

The [jupyter notebook](./vsso_owl2respec.ipynb) contains the code and 
documentation. A [python script](./call_vsso_owl2respec.py) can be used to execute the notebook
from command line.

```bash
pipenv run python call_vsso_owl2respec.py
```

#### Configuration

The environment variable `VSSO_TARGET` can be set to decide, which respec documentation shall be created:

**VSSo Core**  
```bash
export VSSO_TARGET=vsso-core
```

**VSSo**  
```bash
export VSSO_TARGET=vsso
```