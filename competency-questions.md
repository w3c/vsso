# Competency Questions for Assessing VSSo

## Car Attributes
### What are the attributes of this car and what do they express?
```SPARQL
SELECT ?attribute ?branch ?value
WHERE { ?attribute  rdfs:subPropertyOf  vsso:attribute.
?branch ?attribute ?value.}
```
### How many attributes does this car have?
```SPARQL
SELECT (count(distinct ?attribute) as ?nbAttribute)
WHERE{?attribute  rdfs:subPropertyOf  vsso:attribute.}
GROUP BY ?x
```
### What is the model of this car?
```SPARQL
SELECT ?model
WHERE { ?branch vsso:model ?model.}
```
### What is the brand of this car?
```SPARQL
SELECT ?brand
WHERE { ?branch vsso:brand ?brand.}
```
### What is the VIN of this car?
```SPARQL
SELECT ?vin
WHERE { ?branch vsso:vin ?vin.}
```
### How old is this car?
```SPARQL
SELECT ?age
WHERE { ?branch vsso:year ?year.
BIND((2018-?year) AS ?age)}
```
### What are the dimensions of this car?
```SPARQL
SELECT ?length ?width ?height
WHERE { ?branch vsso:length ?length;
	vsso:width ?width;
	vsso:height ?height.}
```
### What are the characteristics of this car's chassis?
```SPARQL
SELECT ?attribute ?value
WHERE { ?attribute  rdfs:subPropertyOf  vsso:attribute.
?chassis a vsso:Chassis;
  ?attribute ?value.}
```
### What type of fuel does this car need?
```SPARQL
SELECT ?fueltype
WHERE {?branch vsso:fuelType ?fuelType.}
```
### What type of transmission does this car have?
```SPARQL
SELECT ?type
WHERE { ?branch vsso:transmissionType ?type.}
```
### What are the characteristics of this engine?
```SPARQL
SELECT ?engine ?attribute ?value
WHERE { ?attribute  rdfs:subPropertyOf  vsso:attribute.
?engine a vsso:InternalCombustionEngine;
  ?attribute ?value.}
```
### How many doors does this car contain?
```SPARQL
SELECT ?nbDoor
WHERE { ?branch vsso:doorCount ?nbDoor.}
```
### How many seats do I have this my car?
```SPARQL
SELECT ?nbSeats ?nbRows
WHERE { ?seats a vsso:Seat;
	vsso:rowCount ?nbRows;
	vsso:row1PosCount ?row1Count;
	vsso:row2PosCount ?row2Count;
	vsso:row3PosCount ?row3Count;
	vsso:row4PosCount ?row4Count;
vsso:row5PosCount ?row5Count.
BIND((?row1Count + ?row2Count + ?row3Count + ?row4Count + ?row5Count) AS ?nbSeats)}

```
### On which side is located the steering wheel?
```SPARQL
SELECT ?steeringWheelSide
WHERE { ?wheel a vsso:SteeringWheel;
vsso:steeringWheelSide ?steeringWheelSide.}
```

## Static Signals
### Is there a signal measuring the steering wheel angle?
```SPARQL
SELECT ?signal
WHERE { ?signal a vsso:SteeringWheelAngle.}
```
### Which signals are controllable?
```SPARQL
SELECT ?signal ?actuator
WHERE { ?actuator  vsso:consumes ?signal.
  ?signal a vsso:ActuatableSignal.}
```
### Which signals are both observable and actuatable?
```SPARQL
SELECT ?signal ?sensor ?actuator
WHERE { ?actuator  vsso:consumes ?signal.
?sensor sosa:observes ?signal.
?signal a vsso:ActuatableSignal, vsso:ObservableSignal.}
```
### How many sensors does this car contain?
```SPARQL
SELECT (count(distinct ?sensor) as ?nbSensor)
WHERE { ?sensor sosa:observes ?signal.
	?signal a vsso:ObservableSignal.}
```
### How many different speedometers does this car contain?
```SPARQL
SELECT (count(distinct ?sensor) as ?nbSpeedSensors)
WHERE { ?sensor a vsso:Speedometer.}
```
### In which part of this car is produced the signal vsso:LongitudinalAcceleration?
```SPARQL
SELECT ?branch ?branchType
WHERE { ?branch  a  ?branchType;
	vsso:hasSignal ?signal.
?signal a vsso:LongitudinalAcceleration.
}
```
### Which signals measure a temperature, and in which part of this car?
```SPARQL
SELECT ?signal ?branch
WHERE { ?branch vsso:hasSignal ?signal.
?signal a vsso:AmbientAirTemperature.
}
```
### What unit type does the signals of type vsso:VehicleYaw use?
```SPARQL
SELECT ?signal ?unitsystem
WHERE { ?signal  a vsso:VehicleYaw;
qudt:unit ?unitsystem.}
```
### What are the characteristics of the sensor producing the signal “TravelledDistance” in the OBD branch?
```SPARQL
SELECT ?sensor ?p ?o
WHERE { ?sensor  a ?sensor;
  vsso:observes ?signal;
  ?p ?o.
?signal a vsso:TravelledDistance.}
```
### What are the maximum values allowed for all signals from car part “Vehicle”?
```SPARQL
```

## Dynamic signals
### What is the current gear?
```SPARQL
SELECT ?signal ?result ?time
WHERE {?signal a vsso:CurrentGear.
?obs a sosa:Observation;
	sosa:observedProperty ?signal;
	sosa:hasSimpleResult ?result;
	sosa:phenomenonTime ?time.
}
ORDER BY DESC(?time)
LIMIT 1
```
### What are the values of all signals representing the speed of this car now?
```SPARQL
SELECT ?signal ?result ?time
WHERE {?signal a vsso:VehicleSpeed.
?obs a sosa:Observation;
	sosa:observedProperty ?signal;
	sosa:hasSimpleResult ?result;
	sosa:phenomenonTime ?time.
}
ORDER BY DESC(?time)
```
### Which windows are currently open?
```SPARQL
SELECT ?position ?value ?time
WHERE {?signal a vsso:WindowPosition.
?window vsso:hasSignal ?signal.
?obs a sosa:Observation;
	sosa:observedProperty ?signal;
	sosa:hasSimpleResult ?value;
	sosa:phenomenonTime ?time.
?window vsso:position ?position.
}
ORDER BY DESC(?time)
```
### What is the local current temperature on the driver side?
```SPARQL
SELECT DISTINCT ?localTemperature ?value ?position ?time
WHERE { ?wheel a vsso:SteeringWheel;
vsso:steeringWheelSide ?steeringWheelSide.
?branch a vsso:LocalHVAC;
vsso:position ?position;
vsso:hasSignal ?localTemperature.
?localTemperature a vsso:LocalTemperature.
FILTER regex(str(?steeringWheelSide),str(?position))

?obs a sosa:Observation;
	sosa:observedProperty ?localTemperature;
	sosa:hasSimpleResult ?value;
	sosa:phenomenonTime ?time.
}
ORDER BY DESC(?time)
LIMIT 1
```