# Non-market Housing Dashboard

This dashboard displays information regarding non-market housing projects in Vancouver. Non-market housing is often subsidized and intended for low and moderate income singles and families. In Vancouver, it exists in the forms of social, supportive, and co-op housing. The dashboard tracks information such as project status, location, clientele, and design in order to provide an view of the current state of non-market housing in the city. 

## Locally Running the Dashboard

### Cloning the Repository

Clone this GitHub repository and navigate to the project folder using the following commands:

```bash
git clone https://github.com/UBC-MDS/DSCI-532_2026_20_non_market_housing.git
cd DSCI-532_2026_20_non_market_housing
```

### Setting Up the Development Environment

Create and activate the development environment using the `environment.yml` file:

```bash
conda env create -f environment.yml
conda activate non-market-housing-dashboard
```

### Running the Dashboard

Run the dashboard using Shiny with the following command:

```bash
shiny run --reload --launch-browser src/app.py
```
