import dendropy
import os

trees_folder = "./trees_iqtree"
output_file = "all_trees.tree"

genomes = ["YALI", "DEHA", "SAKL", "KLTH", "KLLA", "ERGO", "ZYRO", "SACE", "CAGL"]

# Mapping tree leaf labels to genome labels
def map_labels_to_genomes(tree):
    leaves_to_remove = []
    for leaf in tree.leaf_node_iter():
        genome_label = leaf.taxon.label[:4]
        if genome_label in genomes:
            leaf.taxon.label = genome_label  

tree_files = []

for file in os.listdir(trees_folder):
    if file.endswith(".treefile"):
        tree_files.append(os.path.join(trees_folder, file))
tree_files.sort()

all_trees = []

for tree_file in tree_files:
    tree = dendropy.Tree.get(path=tree_file, schema="newick", preserve_underscores=True)
    map_labels_to_genomes(tree)
    all_trees.append(tree)  

# Saving all trees to a single file
with open(output_file, "w") as f:
    for tree in all_trees:
        f.write(tree.as_string(schema="newick"))
        f.write("\n")

print(f"Saved {len(all_trees)} trees to {output_file}")

# Saving rooted reference tree
reference_newick = "(YALI,(DEHA,(((SAKL,KLTH),(KLLA,ERGO)),(ZYRO,(SACE,CAGL)))));"
reference_tree = dendropy.Tree.get(data=reference_newick, schema="newick")
reference_tree.write(path="reference.tree", schema="newick")

print(f"Saved refence tree to reference.tree")
