#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install torch networkx matplotlib numpy pandas scikit-learn
git clone https://github.com/example/CDNMF.git
git clone https://github.com/example/CI-GCL.git
