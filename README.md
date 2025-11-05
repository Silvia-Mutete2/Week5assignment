# AI Workflow Assignment

## Overview

This repository implements a complete machine learning workflow, from data preprocessing to model deployment. It demonstrates best practices in ML project structure, including modular code organization, reproducible training pipelines, and API deployment.

## Features

- 🔄 Complete ML pipeline implementation
- 📊 Sample dataset for immediate experimentation
- 📓 Interactive Jupyter notebook for model training
- 🚀 FastAPI-based model deployment
- 🔧 Modular source code structure
- 📝 Comprehensive documentation
## Project Structure

```
ai-workflow-assignment/
│
├── data/                       # Data directory
│   └── sample_dataset.csv      # Sample training data
│
├── notebooks/                  # Jupyter notebooks
│   └── model_training.ipynb    # Training demonstration
│
├── src/                       # Source code
│   ├── preprocessing.py       # Data preprocessing utilities
│   ├── train_model.py        # Model training pipeline
│   ├── evaluate.py           # Model evaluation tools
│   └── deploy_api.py         # FastAPI deployment service
│
├── diagrams/                  # Documentation diagrams
│   └── workflow_diagram.png   # System architecture diagram
│
├── models/                    # Trained model artifacts
├── requirements.txt          # Project dependencies
└── README.md                 # This documentation
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Silvia-Mutete2/Week5assignment.git
   cd Week5assignment
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

1. Open and run the training notebook:
   ```bash
   jupyter notebook notebooks/model_training.ipynb
   ```
   
2. Follow the notebook cells to:
   - Load and preprocess the sample dataset
   - Train a classification model
   - Evaluate model performance
   - Save the trained model

### Deploying the Model API

1. Ensure you have a trained model in `models/model.joblib`

2. Start the FastAPI server:
   ```bash
   uvicorn src.deploy_api:app --reload
   ```

3. Access the API:
   - Swagger UI: http://127.0.0.1:8000/docs
   - Make predictions via POST request to `/predict`:
     ```bash
     curl -X POST "http://127.0.0.1:8000/predict" \
          -H "Content-Type: application/json" \
          -d '{"feature1": 5.1, "feature2": 3.5, "feature3": 1.4}'
     ```

## API Documentation

### POST /predict

Makes predictions using the trained model.

**Request Body:**
```json
{
    "feature1": float,
    "feature2": float,
    "feature3": float
}
```

**Response:**
```json
{
    "prediction": int
}
```

## Development

### Project Components

- **preprocessing.py**: Handles data loading and preprocessing
- **train_model.py**: Implements model training pipeline
- **evaluate.py**: Contains evaluation metrics and reporting
- **deploy_api.py**: Provides REST API for model serving

### Adding New Features

1. Create feature branch
2. Implement changes
3. Add tests if applicable
4. Submit pull request

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- scikit-learn for machine learning tools
- FastAPI for API framework
- Pandas for data manipulation

## Future Improvements

- [ ] Add comprehensive unit tests
- [ ] Implement CI/CD pipeline
- [ ] Add data validation
- [ ] Enhance API documentation
- [ ] Add model versioning
- [ ] Implement monitoring

