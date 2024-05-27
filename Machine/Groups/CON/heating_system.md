# CON: Heating system for vacuum chambers bake-out

## Introduction

In order to achieve pressure lower than 1e-11 mbar on Sirius storage ring, distributed pumping is mandatory. Vacuum chambers are NEG-coated and they can be activated through a heating process which takes over 48h hours.

Sirius heating process occurs in-situ and the technique was developed in colaboration with Vacuum, Controls and Magnets Groups.


## Heating Elements

### Heating tapes

They will cover up around 80% of SR circumference, mainly designed for 26mm-diameter cylindrical copper vacuum chambers and a very limited gap.
Once they are all made of copper, temperature control will be based on reading tape's resistance, once it is temperature dependant. No temperature sensor will be attached to heating tapes.


### Heating jackets

They will be on the other 20%, designed for regions with more space and special geometries, such as BPMs, bellows, etc.
Each jacket will have a Pt100 temperature sensor in order to have its temperature controlled.

## Baking Crate

The baking crate core is a Beaglebone Black single board computer, adjusting power supplies voltage output and getting feedback about electrical parameters.

[[File:BakingCrate.jpg|500px|thumb|right|Baking crate topology]]

|![](/img/groups/con/heating_system/BakingCrate.jpg)|
|-|
|**Figure 1**: Baking crate topology.|

## Control Software
