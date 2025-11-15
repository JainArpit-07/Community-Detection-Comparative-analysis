# Community Detection: Comparison of CDNMF and CI-GCL

This repository contains all the code and scripts used to perform a comparative analysis of two community detection techniques: CDNMF (Community Detection via Nonnegative Matrix Factorization) and CI-GCL (Community-Inspired Graph Contrastive Learning). The experiments are carried out on three datasets: the Cora citation network, the Citeseer citation network, and synthetic graphs generated using the LFR benchmark model.

All scripts required to reproduce the experimental pipeline are included. The project supports generation of synthetic LFR networks, running both algorithms on all datasets, clustering graph embeddings (in the case of CI-GCL), collecting evaluation metrics, and producing final comparative visualizations and tables that can be included directly in academic reports. The pipeline is fully automated through a single shell script, and individual Python scripts allow running components separately if needed.

The datasets used include Cora (2,708 nodes, 7 communities), Citeseer (3,327 nodes, 6 communities), and LFR benchmarks with configurable parameters such as mixing coefficient and community size distribution. The LFR generator produces data formats compatible with both algorithms. The evaluation relies on commonly used clustering metrics including Accuracy, Normalized Mutual Information (NMI), and Adjusted Rand Index (ARI). All results are exported as CSV files, and the plotting script generates clean PNG figures and LaTeX-ready tables.

To run the full experiment pipeline, install dependencies using `pip install -r requirements.txt` and then execute `bash run_experiments.sh`. This will generate LFR graphs, run CDNMF, run CI-GCL, cluster embeddings, compute metrics, and output results, plots, and tables automatically. Individual components can also be run manually using the provided Python scripts (`generate_lfr.py`, `wrapper_cdnmf.py`, `wrapper_cigcl.py`, and `collect_and_plot.py`). The generated outputs include accuracy/NMI/ARI comparison charts, mixed bar-line graphs, and CSV/LaTeX tables summarizing all model performances.

If PyTorch Geometric is required, it can be installed using wheels from https://data.pyg.org. CDNMF may require correct repository cloning depending on your system, and CI-GCL can be forced into CPU mode by adding `--device cpu` inside the wrapper if GPU is unavailable.

This project is intended for academic and research purposes. The included scripts can be reused, modified, or extended for further exploration of community detection on graph datasets. Citations for the two baseline methods are included below if needed:

CDNMF (2018)  
CI-GCL (2022)
