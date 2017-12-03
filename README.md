# Description
Project designed to allow model construction for Duckietown bot either to navigate through grid based map or using sequence of 
april tags. Moreover there is an opportunities to check correctness of properties in Temporal logic notation using PRISM model
checker and generate properties from the bot's log. The project is implemented as part of the smart city system 
proptotype that allows taxi service ordering through Ethereum smartcontract with automatic validation of liability performance.

# Installation

Be sure that you have installed Python 3.x.

Install project requirements:

```pip install -r requirements.pip```

Download and install PRISM model checker from the official [website](http://www.prismmodelchecker.org).

# Usage

There are 3 scripts of interests that allows: model construction from the template and order (```taxi.py```), 
property generation from the log (```log2prop.py```) and 
validation of the fact that log corresponds to the constructed model (```validate.py```).

*** 1. Model construction ***

Usually multi-agent systems are parametrized and symbolic representation of the actions is infeasible to provide by hand 
in model checker language. To attack the problem the model construction component is designed that is able to build final 
model from template and parameters. Template is represented by valid code in PRISM model checker language but parameters and 
complex actions are replaced with tags (valid identifier surrounded with ```@``` symbold, e.g. ```@moved@```). Parameters in 
case of taxi service is order from the user (source and destination in case of grid map and sequence of ids in case of tags map) and a map of the town (grid or tags based). Valid templates both for grid and tag maps can be found in ```resources``` directory.

Example of model construction:

```python3 taxi.py -m resources/grid_based/town -s resources/grid_based/order -t resources/grid_based/taxi.prism```

In result, ```out_taxi.prism``` file is created where each tag replaced with corresponding expression that depends on parameters.

Other features can be found using help flag ```-h```.

*** 2. Property generation ***

When the service is completed Duckie bot creates a log in csv format where each component of a row correponds to the variable in the model. Thus, we process the log and generate a property to verify using PRISM. Currently, there are 2 types of properties: weak and strong. Strong properties insist that neighbor rows in the log correspond to the neighbor states in the automata of the model. From the other hand, weak property just insures if we took neighbor rows in the log than there is a path between corresponding states in the automata of the model.

Example of property generation:

```python3 log2prop.py -l resources/grid_based/service.log -p resources/grid_based/service.prop --weak```

In result, ```service.prop``` file containing the property will be generated.

The property can be verified manually by [running](http://www.prismmodelchecker.org/manual/RunningPRISM/StartingPRISM) PRISM model checker with model and property files as input.

Other features can be found using help flag ```-h```.

*** 3. Validation ***

However, if there is a model and a log than correspondance can be checked without running model checker explicitly:

```python3 validate.py -m resources/grid_based/service.prism -l resources/grid_based/service.log```

Make sure that model checker's executable file is reachable from the command line simply by name ```prism``` in other case use ```-p``` flag to provide path to it.

Other features can be found using help flag ```-h```.
