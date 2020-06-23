#
# Makefile to generate specifications
#

.PHONY: clean all ttl

all: clean ttl

ttl:
	python vspec2ttl.py -i:../../vehicle_signal_specification/spec/VehicleSignalSpecification.id:1 -I ../../vehicle_signal_specification/spec ../../vehicle_signal_specification/spec/VehicleSignalSpecification.vspec vsso.ttl

clean:
	rm -f vsso.ttl vsso-extension.ttl
