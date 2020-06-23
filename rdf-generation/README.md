# Generation of VSSo and of any private extensions

## Setup
Put the vehicle signal specification and this repository in a common folder. 

### Get the vehicle signal specification
```shell
git clone https://github.com/GENIVI/vehicle_signal_specification
```
### Get the VSSo repo
```shell
git clone https://github.com/w3c/vsso
cd rdf-generation
```

## Build

```shell
make
```
The Makefile will call the generation script, which will generate both `vsso.ttl` and possibly an extension named `vsso-extension.ttl`.

VSS comes with an extension mechnism, where new private concepts are included in the "Private" repository. This methods has the benefit of separating the core model from the private concepts. The script `vspec2ttl.py` will generate an extension `vsso-extension.ttl` if the private branch is included. See https://github.com/GENIVI/vehicle_signal_specification for more details. Another possible solution consists in modifying directly VSS concepts. It is however not recommended.