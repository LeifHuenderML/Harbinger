# Harbinger: Deep Learning-Powered Valley Fever Prediction and Risk Assessment

![Harbinger Logo](harbinger-logo.jpg)

## Table of Contents
- [Project Overview](#project-overview)
- [Quick Links](#quick-links)
- [Research Team](#research-team)
- [Introduction to Valley Fever](#introduction-to-valley-fever)
- [Project Objectives](#project-objectives)
- [Methodology](#methodology)
- [Current Research Focus](#current-research-focus)
- [Future Directions](#future-directions)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Data Access](#data-access)
- [Published Research](#published-research)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Harbinger is a cutting-edge research initiative aimed at forecasting Coccidioidomycosis (Valley Fever) outbreaks using advanced deep learning techniques. The name "Harbinger" reflects our goal of signaling the approach of potential outbreaks, enabling proactive public health responses.

Our project leverages state-of-the-art machine learning models, particularly Long Short-Term Memory (LSTM) networks, to analyze complex environmental and meteorological data patterns associated with Valley Fever outbreaks. By incorporating diverse data sources and employing sophisticated analytical techniques, Harbinger aims to provide accurate, long-lead time predictions and comprehensive risk assessments.

## Quick Links

- [Data Access](#data-access)
- [Published Research](#published-research)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Research Team

- **Leif Huender** - Undergraduate Researcher
- **Dr. Mary Everett**
- **Sarah Davis** - PhD Student
- **Dr. John Shovic** 

Contact: Leif Huender (leifhuenderai@gmail.com)

## Introduction to Valley Fever

Valley Fever is a fungal respiratory infection caused by Coccidioides species, endemic to semi-arid regions of the southwestern United States and parts of Mexico. The disease is contracted by inhaling fungal spores present in soil and can lead to severe respiratory issues, especially in vulnerable populations.

Our research expands on previous work establishing correlations between temporal meteorological patterns and outbreak occurrences. We employ advanced LSTM models to capture complex, long-term dependencies in environmental data, aiming to predict outbreaks with significant lead time.

### Key Focus Areas:

- Leveraging deep learning for long-lead time predictions (up to 12 months in advance)
- Comprehensive risk assessment with significant lead time
- Enabling proactive public health measures through early warning systems
- Investigating the impact of climate change on Valley Fever incidence patterns

## Project Objectives

1. Enhance existing LSTM models for Valley Fever prediction, improving accuracy and lead time
2. Incorporate new features into our models, including air quality indices and smoke particulate matter data
3. Expand dataset coverage to include more counties in California and Arizona
4. Develop and compare various machine learning approaches (e.g., LSTM, Transformer, Mamba models)
5. Investigate the impact of environmental cycles (e.g., El Niño, Pacific Decadal Oscillation) on outbreak patterns
6. Develop sophisticated risk assessment models using Monte Carlo simulations and Markov chains
7. Enhance model explainability using techniques like SHAP values and Layer-wise Relevance Propagation

## Methodology

### 1. Data Collection and Curation

- Comprehensive dataset compilation from multiple sources:
  - Meteorological data (temperature, precipitation, wind patterns)
  - Soil moisture and composition data
  - Air quality indices
  - Smoke particulate matter concentrations
  - Historical Valley Fever case data
- Data preprocessing and quality assurance procedures
- See `data/README.md` for detailed information on data sources and processing

### 2. Exploratory Data Analysis

- Temporal and spatial pattern discovery in environmental and outbreak data
- Correlation analysis between environmental factors and Valley Fever incidence
- Feature importance ranking using statistical and machine learning techniques
- Visualization of key relationships and trends

### 3. LSTM Model Development

- Implementation of sliding window techniques for time series forecasting
- Hyperparameter optimization using Bayesian optimization
- Multi-step ahead prediction strategies
- Ensemble methods combining multiple LSTM models for improved robustness

### 4. Comparative Analysis

- Benchmarking LSTM models against traditional time series forecasting methods (e.g., ARIMA, Prophet)
- Evaluation of modern deep learning architectures (e.g., Transformer models, TCN)
- Performance comparison using metrics such as RMSE, MAE, and custom epidemiological metrics

### 5. Environmental Cycle Analysis

- Time series decomposition to isolate trend, seasonality, and cyclical components
- Spectral analysis using Fourier transforms to identify dominant frequencies
- Wavelet transforms for multi-scale analysis of environmental patterns
- Integration of cycle information into predictive models

### 6. Risk Assessment Modeling

- Monte Carlo simulations to quantify prediction uncertainties
- Markov chain models for probabilistic outbreak progression modeling
- Markov blanket analysis to identify key causal factors in outbreak dynamics
- Development of interpretable risk scores and confidence intervals

### 7. Explainable AI Approaches

- Implementation of SHAP (SHapley Additive exPlanations) values for feature importance
- Integrated Gradients for attribution of model predictions to input features
- Layer-wise Relevance Propagation (LRP) for visualizing decision processes in neural networks
- Development of interactive visualization tools for model interpretability

## Current Research Focus

1. Refinement of long-lead time prediction models, aiming for accurate 12-month forecasts
2. Development of a sophisticated risk assessment tool integrating multiple modeling approaches
3. In-depth analysis of environmental cycles and their correlation with Valley Fever incidence
4. Enhancement of model explainability to provide actionable insights for public health officials

## Future Directions

- Integration of high-resolution satellite imagery for improved environmental monitoring
- Exploration of collaborative filtering techniques for identifying outbreak patterns across regions
- Development of a real-time risk assessment dashboard for public health stakeholders
- Investigation of potential climate change impacts on future Valley Fever distribution and incidence

## Repository Structure

```
harbinger/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── models/
│   ├── lstm/
│   ├── comparative/
│   └── risk_assessment/
│
├── scripts/
│   ├── data_processing/
│   ├── model_training/
│   ├── evaluation/
│   └── visualization/
│
├── notebooks/
│   ├── exploratory_analysis/
│   ├── model_development/
│   └── results_analysis/
│
├── tests/
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

## Getting Started

To set up the Harbinger project environment and run key scripts, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-organization/harbinger.git
   cd harbinger
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the data directory (see `data/README.md` for detailed instructions on data acquisition)

5. Run key scripts:

   ```python
   # Data preprocessing
   python scripts/data_processing/preprocess_environmental_data.py

   # LSTM model training
   python scripts/model_training/train_lstm_model.py

   # Monte Carlo simulations for risk assessment
   python scripts/risk_assessment/monte_carlo_simulations.py

   # Markov chain analysis
   python scripts/risk_assessment/markov_chain_analysis.py

   # Generate visualizations
   python scripts/visualization/plot_predictions.py
   ```

For more detailed instructions and usage examples, refer to the documentation in the `docs/` directory.

## Data Access

Due to the sensitive nature of some of our data sources, access to the full dataset is restricted. Researchers interested in collaborating or accessing the data should contact Leif Huender (leifhuenderai@gmail.com) with a brief research proposal.

A subset of the public environmental data used in this project is available in the `data/public/` directory.

## Published Research

For a complete list of publications and preprints, please visit our [project website](https://www.harbinger-project.org/publications).

## Contributing

We welcome contributions from the scientific community! If you're interested in contributing to the Harbinger project, please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

For more information, visit our [project website](https://www.harbinger-project.org) or contact the research team at info@harbinger-project.org.