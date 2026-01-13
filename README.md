# Phylogenetic Tree Comparison Project: Genolevures Consensus Tree Analysis

This repository contains the scripts and results for a comparative bioinformatics analysis, focusing on reconstructing consensus phylogenetic trees from gene families of nine yeast species from the Genolevures project. The project involves multiple sequence alignment, individual tree reconstruction, consensus tree generation, and comparison with a reference topology.

## Step-by-Step Analysis
Follow these steps in order to reproduce the consensus tree analysis:

### Step 1: Gene Family Alignment and Tree Reconstruction
The `1_aligment_and_trees.sh` script processes gene families from the input directory, performs multiple sequence alignment using MAFFT, and reconstructs phylogenetic trees using IQ-TREE2. It processes files in parallel (8 jobs simultaneously).

    bash 1_aligment_and_trees.sh

### Step 2: Tree Collection and Reference Tree Creation
The `2_before_consensus.py` Python script collects all generated tree files, standardizes leaf labels to genome identifiers, and saves them in a single file. It also creates a reference tree based on established Genolevures phylogeny.

    python3 2_before_consensus.py

### Step 3: Consensus Tree Generation
The `3_iqtree_consensus.sh` script uses IQ-TREE2 to generate a consensus tree from the 500 individual trees using the bootstrap consensus method with 500 replicates.

    bash 3_iqtree_consensus.sh

### Step 4: Tree Rooting
The `4_consensus_rooting.py` script roots the consensus tree at the YALI (Yarrowia lipolytica) branch for comparison with the rooted reference tree.

    python3 4_consensus_rooting.py

### Step 5: Visualization and Distance Calculation
The `5_consenus_visualization.Rmd` R Markdown script visualizes both trees using a tanglegram plot and calculates the normalized Robinson-Foulds distance to quantify topological differences.

## Installation
To successfully run the analysis scripts, the following software and libraries must be installed and accessible from your system's PATH.

### Bioinformatics Software Tools
These external command-line tools are required for alignment and tree building:

- MAFFT: Required for Multiple Sequence Alignment (MSA) (Step 1)
- IQ-TREE2: Essential for Maximum Likelihood (ML) tree inference (Step 1, Step 3)

### Programming Environments & Libraries

- Python 3: Required for .py scripts
- Dendropy: Necessary Python library for handling tree files
- R and RStudio: Required for running the analysis and visualization script (5_consenus_visualization.Rmd)
    - Required R packages: ape, TreeDist, phytools

### Installation

    pip install dendropy
    brew install mafft
    brew install iqtree2

## Repository Installation

    git clone https://github.com/barbarapawlowskaa/genolevures_consensus
    cd genolevures_consensus
