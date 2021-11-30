# VSSo: the Vehicle Signal Specification Ontology

This repository contains the standards work being carried out around the development, extension and usage of VSSo. VSSo is an ontology created from the [Vehicle Signal Specification](https://github.com/covesa/vehicle_signal_specification/). It also relies on the [SOSA patterns for observations and actuations](https://www.w3.org/TR/vocab-ssn/).

VSSo began as a research project by EURECOM and BMW, EURECOM's parent organization Institut Mines-Télécom brought it to W3C for standardization consideration by making a [Member Submission](https://www.w3.org/Submission/2020/SUBM-vsso-20201026/) [comment](https://www.w3.org/Submission/2020/02/Comment/) 

More precisely, the VSSo ontology is available in [Turtle](vsso.ttl) and corresponds to the [release 1.0 of VSS](https://github.com/covesa/vehicle_signal_specification/releases/tag/v1.0)

## A quick start
The repository is structured as follows:

 * [docs](docs): This folder contains the html documentation of VSSo, automatically generated using [WIDOCO](https://github.com/dgarijo/Widoco). The rendered page is also available at http://automotive.eurecom.fr/vsso
 *  [rdf-generation](rdf-generation): This folder contains the script for generating VSSo but also extending it according to the priciple of private branches described in the vehicle signal specification

We provide [a list of competency question](competency-questions.md) that served to evaluate VSSo. These competency questions are expressed when possible as SPARQL queries that can be executed on any datasets using the VSSo ontology, such as http://automotive.eurecom.fr/simulator/query

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
