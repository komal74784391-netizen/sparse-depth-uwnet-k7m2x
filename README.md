# sparse-depth-uwnet

Code for **"Sparse Depth Completion for Underwater Inspection Robots"**
(ICRA 2025).

The repository implements the sonar-camera fusion network, the turbidity
augmentation pipeline and the field evaluation scripts.

## Layout

- `src/models/uwnet.py` - fusion network
- `src/data/sonar.py` - sonar/camera dataset utilities
- `scripts/train.py`, `scripts/eval.py` - training and evaluation
- `configs/icra.yaml` - configuration used for the paper
