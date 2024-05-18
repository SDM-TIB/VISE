import os
from rdflib import Graph
from TravSHACL import parse_heuristics, GraphTraversal, ShapeSchema


prio_target = 'TARGET'  # shapes with target definition are preferred, alternative value: ''
prio_degree = 'IN'  # shapes with a higher in-degree are prioritized, alternative value 'OUT'
prio_number = 'BIG'  # shapes with many constraints are evaluated first, alternative value 'SMALL'

schema_dir = './shapes/'
shapes_graph = Graph()
for shape_file in os.listdir(schema_dir):
    shapes_graph.parse(os.path.join(schema_dir, shape_file))  # reading all shape files into the shapes graph

shape_schema = ShapeSchema(
    schema_dir=shapes_graph,  # passing an RDFlib graph containing the shapes
    endpoint='http://localhost:9090/sparql/', #enter endpoint
    graph_traversal=GraphTraversal.DFS,
    heuristics=parse_heuristics(prio_target + ' ' + prio_degree + ' ' + prio_number),
    use_selective_queries=True,
    max_split_size=256,
    output_dir='./ECAI_result/',  # directory where the output files will be stored
    order_by_in_queries=False,  # sort the results of SPARQL queries in order to ensure the same order across several runs
    save_outputs=True  # save outputs to output_dir, alternative value: False
)

result = shape_schema.validate()  # validate the SHACL shape schema
print(result)