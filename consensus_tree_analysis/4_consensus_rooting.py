import dendropy

# Loading the consensus tree 
consensus_tree = dendropy.Tree.get(path="consensus.contree", schema="newick")

# Finding the leaf corresponding to the genome YALI
yali_leaf = consensus_tree.find_node_with_taxon_label("YALI")

# Rerooting the tree to the YALI leaf
consensus_tree.reroot_at_edge(yali_leaf.edge, update_bipartitions=False)

consensus_tree.write(path="consensus_rooted.tree", schema="newick")

print("Consensus tree rerooted at YALI saved as 'consensus_rooted.tree'")
