[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
# VISE:  Validated and Invalidated Symbolic Explanations for Knowledge Graph Integrity

VISE represents a novel hybrid strategy that integrates symbolic learning, 
constraint validation, and numerical learning approaches. VISE employs KGE 
to capture implicit information and represent negation in KGs, thereby 
enhancing the prediction performance of numerical models. The experimental 
results demonstrate the efficacy of this hybrid technique, which effectively 
integrates the strengths of symbolic, numerical, and constraint validation 
paradigms.

![VISE Design Pattern](https://raw.githubusercontent.com/SDM-TIB/VISE/main/images/VISE-updated.png "VISE Design Pattern")

## Getting started 
Clone the repository
```git
git clone git@github.com:SDM-TIB/VISE.git
```


# Executing scripts to reproduce Symbolic Learning, Constraint Validation and Transformation navigate to `Symbolic Learning` folder

Step 1: Provide configuration for executing in `input.json` file
```json
 {
  "KG": "SynLC",
  "prefix": "http://synthetic-LC.org/lungCancer",
  "rules_file": "synLC_1000.csv",
  "rdf_file": "SynthLC_1000.nt",
  "constraints_folder": "SynLC"
}
```
The user must provide the cconfiguration details in `input.json` file
`KG` corresponds to the folder of Knowledge Graph user wants to utilize.
`prefix` refers to the prefix utilized in the KG (.NT file)
`rules_file` contains the symbolic learning rules user want to use in .CSV format
`rdf_file` is the name of the KG (.NT file) in the KG folder
`constraints_folder` refers to the folder where the SHACL constraint defined based on the domain knowledge.

Step 2: Execute `Symbolic_predictions.py`

```python
python Symbolic_predictions.py
```
The symbolic learning predictions are saved under the folder `Symbolic Learning/Predictions`. The `Predictions` folder contains two sub-folders
1) predictions generated per predicate in the head of the rule
2) The enriched KG, i.e., the original KG with enrichment performed by symbolic learning predictions
Lastly, `Tranformed_{KG_name}` containts the KG after the tranformation process.

# Executing scripts to reproduce KGE results by choosing ``Baseline`` or ``VISE`` folders and navigating to appropriate path.

Step 1: Provide configuration for executing
```json
{
  "Type": "Baseline",
  "KG": "baseline1.tsv",
  "model": ["TransE", "TransH","TransD","RotatE"],
  "path_to_results": "./Results/Baseline1/"
}
```
The user must provide a few options in the above JSON file to select the type of approach that has to be executed with added configuration details. <br>
The parameter ``Type`` corresponds to the type of execution, i.e., ```Baseline``` or ```VISE```.<br>
Secondly, parameter ``KG`` is the type of knowledge graph, i.e., ```KG 1``` or ```KG 2``` or ```KG 3```.<br>
Nextly,```model```parameter is used for training the KGE model to generate results for readability.<br>
Lastly, ```path_to_results``` is parameter given by user to store the trained model results.

Step 2: Execute `kge_vise.py`
```python
python kge_vise.py 
```
`Note: KGE models are trained in Python 3.9 and executed in a virtual machine on Google Colab with 40 GiB VRAM and 1
GPU NVIDIA A100 SMX-4, with CUDA Version 12.2 (Driver 525.104.05) and PyTorch (v2.0.1).`

