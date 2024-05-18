[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
# VISE:  Validated and Invalidated Symbolic Explanations for Knowledge Graph Integrity

VISE represents a novel hybrid strategy that integrates symbolic learning, 
constraint validation, and numerical learning approaches. VISE employs KGE 
to capture implicit information and represent negation in KGs, thereby 
enhancing the prediction performance of numerical models. The experimental 
results demonstrate the efficacy of this hybrid technique, which effectively 
integrates the strengths of symbolic, numerical, and constraint validation 
paradigms.

![VISE Design Pattern](https://raw.githubusercontent.com/SDM-TIB/VISE/main/images/VISE.png "VISE Design Pattern")

## Getting started 
Clone the repository
```git
git clone git@github.com:SDM-TIB/VISE.git
```

Executing scripts to reproduce KGE results by choosing ``Baseline`` or ``VISE`` folders and navigating to appropriate path.

Provide configuration for executing
```json
{
  "Type": "Baseline",
  "KG": "frenchRoyalty.tsv",
  "model": ["TransE", "TransH","TransD","RotatE"],
  "path_to_results": "./Results/FrenchRoyalty/"
}
```
The user must provide a few options in the above JSON file to select the type of approach that has to be executed with added configuration details. <br>
The parameter ``Type`` corresponds to the type of execution, i.e., ```Baseline``` or ```SPaRKLE```.<br>
Secondly, parameter ``KG`` is the type of knowledge graph, i.e., ```FrenchRoyalty``` or ```Family``` or ```YAGO3-10```.<br>
Nextly,```model```parameter is used for training the KGE model to generate results for readability.<br>
Lastly, ```path_to_results``` is parameter given by user to store the trained model results.

```python
python kge_vise.py 
```
`Note: KGE models are trained in Python 3.9 and executed in a virtual machine on Google Colab with 16 GiB VRAM and 1
GPU NVIDIA Tesla 𝑇 4, with CUDA Version 12.0 (Driver 525.105.17) and PyTorch (v2.0.1).`

