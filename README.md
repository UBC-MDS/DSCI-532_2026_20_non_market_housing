# Non-market Housing Dashboard

## Motivation and Purpose

This dashboard displays information regarding non-market housing projects in Vancouver. Non-market housing is often subsidized and intended for low and moderate income singles and families. In Vancouver, it exists in the forms of social, supportive, and co-op housing. Non-market housing initiatives are incredibly import for easing the burden of the affordability crisis on low- to moderate- income individuals. This dashboard serves as a tool to assist those in charge of planning, proposing, and developing non-market housing in identifying areas where the current landscape can be improved. The dashboard tracks information such as project status, location, clientele, and design in order to provide an view of the current state of non-market housing in the city.

![Dashboard Demo](./img/dashboard_demo.gif)

## Deployments

The dashboard is hosted on Posit Connect. Use the links below to access the live versions:

- [Production (for users)](https://019c962d-6a7d-25ba-ce46-92dc73941290.share.connect.posit.cloud)
- [Development (for contributers)](https://019c962d-fcf5-2985-c4d8-d90446aff53c.share.connect.posit.cloud)

## How to Contribute

Please find details on how to contribute in [CONTRIBUTING.md](CONTRIBUTING.md)

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
shiny run --reload --launch-browser src.app:app
```

### Assistant Chat (LLM)

The Assistant tab uses an LLM for conversational help. To enable it:

1. Copy `.env.example` to `.env`
2. Add your API key for one provider:
   - **Anthropic (Claude)**: `ANTHROPIC_API_KEY` from [console.anthropic.com](https://console.anthropic.com/account/keys)
   - **OpenAI (GPT)**: `OPENAI_API_KEY` from [platform.openai.com](https://platform.openai.com/api-keys)
   - **Google (Gemini)**: `GOOGLE_API_KEY` from [aistudio.google.com](https://aistudio.google.com/app/apikey)
   - **GitHub PAT** (free): `GITHUB_TOKEN` from [github.com/settings/tokens](https://github.com/settings/tokens) with the "models" scope. Sign up at [github.com/marketplace/models](https://github.com/marketplace/models) for access.
3. Restart the app
