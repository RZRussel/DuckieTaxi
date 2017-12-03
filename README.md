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
