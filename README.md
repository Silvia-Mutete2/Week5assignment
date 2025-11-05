# Week5assignment
This repository contains a starter AI workflow for Week 5 assignment. It includes a small sample dataset, a notebook demonstrating training, simple source modules for preprocessing/training/evaluation, and a minimal FastAPI deployment example.
Repository structure
--------------------
ai-workflow-assignment/
│
├── data/
│   └── sample_dataset.csv        # small CSV for quick experiments
│
├── notebooks/
│   └── model_training.ipynb     # demo notebook: load data, train a model
│
├── src/
│   ├── preprocessing.py         # load and preprocess utilities
│   ├── train_model.py           # training helper that saves model
│   ├── evaluate.py              # evaluation helpers
│   └── deploy_api.py            # FastAPI app for predictions
│
├── diagrams/
│   └── workflow_diagram.png     # placeholder for architecture diagram
│
├── models/                      # models saved at runtime
├── README.md
└── requirements.txt

Quick start
-----------

1. Install dependencies (prefer a virtualenv):

	pip install -r requirements.txt

2. Run the notebook to train a quick model (or run the training script manually):

	- Open `notebooks/model_training.ipynb` in Jupyter and run cells.

3. Start the API (after training and saving a model to `models/model.joblib`):

	uvicorn src.deploy_api:app --reload

Notes and next steps
--------------------

- Replace `diagrams/workflow_diagram.png` with a proper diagram (PNG/SVG).
- Improve preprocessing, add feature engineering and unit tests.
- Add CI to run linting/tests and model validation steps.

If you want, I can also add a tiny test harness or CLI script to train and evaluate the model automatically.
# Week5assignment
