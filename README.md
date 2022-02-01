# VSSo: the Vehicle Signal Specification Ontology

This repository contains the standards work being carried out around the development, extension and usage of VSSo. VSSo is an ontology created from the [Vehicle Signal Specification (VSS)](https://github.com/covesa/vehicle_signal_specification/). It also relies on the [SOSA patterns for observations and actuations](https://www.w3.org/TR/vocab-ssn/).

VSSo began as a research project by EURECOM and BMW, EURECOM's parent organization Institut Mines-Télécom brought it to W3C for standardization consideration by making a [Member Submission](https://www.w3.org/Submission/2020/SUBM-vsso-20201026/) [comment](https://www.w3.org/Submission/2020/02/Comment/) 

## A quick start

The main branch of the repository is used for active development.The first version of VSSo based on [VSS v1.0](https://github.com/COVESA/vehicle_signal_specification/releases/tag/v1.0) can be found in [releases](https://github.com/w3c/vsso/releases).  

Since VSS v1.0 the specification evolved, which allows a different structure of VSSo.
The current goal is to create a core ontology defining the major concepts of VSS (e.g. Branch, Sensors, Actuators, etc.).
This core ontology is then used as reference, so that the definitions of VSS can be generated as VSSo conctepts through tooling.

We therefore propose three artifacts as part of VSSo, which are reflected in the structure of the repository:

* **[VSSo Primer](vsso-primer):** The primer includes the motivation, intended use cases and indications where to find further 
  information. [HTML view]{https://w3c.github.io/vsso/vsso-primer/}
* **[VSSo Core](vsso-core):** Core ontology of VSSo. Meant as a reference for automatic mapping from VSS into an ontology. [HTML view]{https://w3c.github.io/vsso/vsso-core/vsso-core-re.html}
* **[VSSo](vsso):** Structure for the documentation of the generated concepts from VSS. [HTML view]{https://w3c.github.io/vsso/vsso/vsso-re.html}


All documentation is generated using [WIDOCO](https://github.com/dgarijo/Widoco).

## Cite
If you use VSSo in a scientific publication, we would appreciate citations to the following paper:

```
@inproceedings{klotz2018vsso,
    author={Benjamin Klotz and Raphael Troncy and Daniel Wilms and Christian Bonnet},
    title={{VSSo - A vehicle signal and attribute ontology}},
    year={2018},
    booktitle={9th International Semantic Sensor Networks Workshop (SSN)}
}
```

### License
The code is licensed under the [Apache-2.0 License](https://www.apache.org/licenses/LICENSE-2.0). The VSSo ontology is licensed under the [CC 4.0 Licence](http://creativecommons.org/licenses/by/4.0/).
