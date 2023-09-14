node_1 = {'type':'Concept','name':'human'}
node_2 = {'type':'Concept','name':'monkey'}
node_3 = {'type':'Concept','name':'chimp'}
node_4 = {'type':'Concept','name':'snake'}
node_5 = {'type':'Concept','name':'earthworm'}
node_6 = {'type':'Concept','name':'rhino'}
node_7 = {'type':'Concept','name':'triceratops'}
node_8 = {'type':'Concept','name':'vine'}
node_9 = {'type':'Concept','name':'ent'}
node_10 = {'type':'Concept','name':'mammal'}
node_11 = {'type':'Concept','name':'animal'}
node_12 = {'type':'Concept','name':'reptile'}
node_13 = {'type':'Concept','name':'dinosaur'}
node_14 = {'type':'Concept','name':'plant'}

link_1 = {'type': 'Similarity', 'targets': [node_1, node_2]}
link_2 = {'type': 'Similarity', 'targets': [node_1, node_3]}
link_3 = {'type': 'Similarity', 'targets': [node_3, node_2]}
link_4 = {'type': 'Similarity', 'targets': [node_4, node_5]}
link_5 = {'type': 'Similarity', 'targets': [node_6, node_7]}
link_6 = {'type': 'Similarity', 'targets': [node_4, node_8]}
link_7 = {'type': 'Similarity', 'targets': [node_1, node_9]}
link_8 = {'type': 'Inheritance', 'targets': [node_1, node_10]}
link_9 = {'type': 'Inheritance', 'targets': [node_2, node_10]}
link_10 = {'type': 'Inheritance', 'targets': [node_3, node_10]}
link_11 = {'type': 'Inheritance', 'targets': [node_10, node_11]}
link_12 = {'type': 'Inheritance', 'targets': [node_12, node_11]}
link_13 = {'type': 'Inheritance', 'targets': [node_4, node_12]}
link_14 = {'type': 'Inheritance', 'targets': [node_13, node_12]}
link_15 = {'type': 'Inheritance', 'targets': [node_7, node_13]}
link_16 = {'type': 'Inheritance', 'targets': [node_5, node_11]}
link_17 = {'type': 'Inheritance', 'targets': [node_6, node_10]}
link_18 = {'type': 'Inheritance', 'targets': [node_8, node_14]}
link_19 = {'type': 'Inheritance', 'targets': [node_9, node_14]}
link_20 = {'type': 'Similarity', 'targets': [node_2, node_1]}
link_21 = {'type': 'Similarity', 'targets': [node_3, node_1]}
link_22 = {'type': 'Similarity', 'targets': [node_2, node_3]}
link_23 = {'type': 'Similarity', 'targets': [node_5, node_4]}
link_24 = {'type': 'Similarity', 'targets': [node_7, node_6]}
link_25 = {'type': 'Similarity', 'targets': [node_8, node_4]}
link_26 = {'type': 'Similarity', 'targets': [node_9, node_1]}

all_nodes = [node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10, node_11, node_12, node_13, node_14]
all_links = [link_1, link_2, link_3, link_4, link_5, link_6, link_7, link_8, link_9, link_10, link_11, link_12,    link_13,    link_14,    link_15,    link_16,    link_17,    link_18,    link_19,    link_20,    link_21,    link_22,    link_23,    link_24,    link_25,    link_26]

