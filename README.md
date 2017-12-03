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
