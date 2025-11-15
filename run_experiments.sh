#!/bin/bash
python generate_lfr.py
python wrapper_cdnmf.py
python wrapper_cigcl.py
python collect_and_plot.py
