# Vancouver Non-Market Housing Dashboard Proposal - Group 20

## Motivation and Purpose

Vancouver is currently experiencing an affordable housing crisis and ranks as the **4th most unaffordable housing market in the world**. Non-market housing is an incredibly important strategy to ease the burden of this suffocating housing market on low- to moderate-income families and individuals. As such, the housing co-operatives, government agencies, and independent non-profit societies that fund and control the development of non-market housing need a tool to help examine the areas in which their current efforts are successful.
Such a tool would allow non-market housing planners to identify underserved local areas, target demographics, and development status of the different projects in the city. This would ultimately inform planning and help to establish a fair and equitable network of non-market housing across the city.

### Target Audience

The primary audience for this dashboard includes:

- Housing planners affiliated with the City of Vancouver
- Non-profit housing providers
- Housing co-operatives
- Government housing agencies (e.g., BC Housing)
- Urban researchers and policy analysts

These stakeholders require clear, spatially informed, and demographic-specific insights to guide equitable housing development.

## Research Questions

Our dashboard will asist our stakeholders in addressing research questions related to equity and developmental trends:

1. Spatial Equity
    - Which local areas in Vacnouver have the lowest concentration of non-market housing developments?
    - Are certain neighbourhoods underserved relative to others?
2. Demographic Equity
    - Are sufficient units being developed for families, seniors, or other residents?
    - Which local areas lack family-oriented or senior-focused housing?
3. Equitable Accessibility
    - How many units are accessible or adaptable for residents with disabilities?
    - Which local areas lack accessible developments?
4. Developmental Trends
    - How has the rate of non-market housing development changed over time?
    - Which organizations (operators) contribute to the most projects?
    - Do certain organizations prioritize different clientele (family, senior, disabled, etc.)?

## Description of the Data

The [City of Vancouver's Non-Market Housing Dataset](https://opendata.vancouver.ca/explore/dataset/non-market-housing/information/) contains 641 rows (each representing a unique non-market housing development) and 27 columns (attributes describing project characteristics). The attributes in each column will either be used to filter data or be visualized in some way on our dashboard to assist non-market housing planners in making decisions. The relevance of each attribute is summarized below:

| Feature | Description | Relevance |
| --- | --- | --- |
| `Index Number` | Internal unique project identifier. | Not used in dashboard. |
| `Name` | Name of housing project. | Displayed on map hover. |
| `Address` | Street address of project. | Displayed on map hover. |
| `Project Status` | Development stage (Completed, Under Construction, Approved, Proposed). | Visualized as bar chart; filterable category. |
| `Occupancy Year` | Year first occupied. | Year slider filter; line chart showing development trends over time. |
| `Operator` | Organization managing the housing project. | Searchable filter; summary table of project counts by operator. |
| `Clientele - Families` | Number of units with 2+ bedrooms (family-oriented). | Filter option; aggregated into bar chart. |
| `Clientele - Seniors` | Number of units intended for residents typically 55+. | Filter option; aggregated into bar chart. |
| `Clientele - Other` | Number of units for single non-seniors. | Filter option; aggregated into bar chart. |
| `Design - Accessible 1BR` | Number of one-bedroom units designed to be accessible for a person with disabilities without assistance. | Filter option; aggregated into bar chart. |
| `Design - Accessible 2BR` | Number of two-bedroom units designed to be accessible for a person with disabilities without assistance. | Filter option; aggregated into bar chart. |
| `Design - Accessible 3BR` | Number of three-bedroom units designed to be accessible for a person with disabilities without assistance. | Filter option; aggregated into bar chart. |
| `Design - Accessible 4BR` | Number of four-bedroom units designed to be accessible for a person with disabilities without assistance. | Filter option; aggregated into bar chart. |
| `Design - Accessible Studio` | Number of studio units designed to be accessible for a person with disabilities without assistance. | Filter option; aggregated into bar chart. |
| `Design - Accessible Room` | Number of housekeeping or sleeping units designed to be accessible for a person with disabilities without assistance. | Filter option; aggregated into bar chart. |
| `Design - Adaptable 1BR` | Number of one-bedroom units that are designed to be able to be modified to meet the changing accessibility needs of residents. | Filter option; aggregated into bar chart. |
| `Design - Adaptable 2BR` | Number of two-bedroom units that are designed to be able to be modified to meet the changing accessibility needs of residents. | Filter option; aggregated into bar chart. |
| `Design - Adaptable 3BR` | Number of three-bedroom units that are designed to be able to be modified to meet the changing accessibility needs of residents. | Filter option; aggregated into bar chart. |
| `Design - Adaptable 4BR` | Number of four-bedroom units that are designed to be able to be modified to meet the changing accessibility needs of residents. | Filter option; aggregated into bar chart. |
| `Design - Standard 1BR` | Number of one-bedroom units designed for a typical standard of liveability. | Filter option; aggregated into bar chart. |
| `Design - Standard 2BR` | Number of two-bedroom units designed for a typical standard of liveability. | Filter option; aggregated into bar chart. |
| `Design - Standard 3BR` | Number of three-bedroom units designed for a typical standard of liveability. | Filter option; aggregated into bar chart. |
| `Design - Standard 4BR` | Number of four-bedroom units designed for a typical standard of liveability. | Filter option; aggregated into bar chart. |
| `Design - Standard Studio` | Number of studio units units designed for a typical standard of liveability. | Filter option; aggregated into bar chart. |
| `Design - Standard Room` | Number of housekeeping or sleeping units designed for a typical standard of liveability. | Filter option; aggregated into bar chart. |
| `URL` | Link to City webpage for the project. | displayed on map hover (clickable). |
| `Geom` | Spatial (point) representation of feature. | Used to plot project on map. |

We also plan on integrating the [City of Vancouver's Local Area Boundary Dataset](https://opendata.vancouver.ca/explore/dataset/local-area-boundary/information/?disjunctive.name) which contains the geometries of the major local areas in Vancouver. This will give users of our dashboard the ability to filter non-market housing developments by local area to examine those which are currently underserved. This dataset contains 22 rows (each representing a local area) and 3 columns which are summarized below:

| Feature | Description | Relevance |
| --- | --- | --- |
| `Name` | Official name of the local area. | Will be able to filter data by name of the local area. |
| `Geom` | Spatial representation of local area boundary. | Used to determine which local area each development falls within. |
| `geo_point_2d` | Spatial coordinate representing the center of the local area. | Will not be relevent to our dashboard. |

## Usage Scenarios

### Persona

**Name**: Elise Moraes
**Role**: Non-Market Housing Planner - BC Housing
**Experience**: 6 years in urban planning and affordable housing policy

Elise is responsible for evaluating development proposals and identifying underserved areas in Vancouver. Her decisions play an essential role in determining where BC Housing allocates their funds for the development of non-market housing. She frequently reports these decisions to city council and must justify them using spatial and demographic data. She needs a centralized tool that allows her to quickly filter, compare, and visualize non-market housing developments across the city.

### Usage Scenario

Elise has been tasked with preparing a presentation for city council on whether family-oriented non-market housing is equitably distributed across Vancouver's local areas.

Using the dashboard, she:

1. Filters by **Clientele - Families** to view developments with 2+ bedroom units.
2. Uses the **Local Area Filter** to compare areas.
3. Observes the **bar chart** summarizing family-unit totals compared to other unit types.
4. Adjusts the **Occupancy Year slider** to analyze projects completed in the past 10 years.
5. Reviews the **Project Status chart** to determine how many new family-oriented developments are still proposed or under construction.

She can then identify the local areas with relatively low family-unit availability despite high overall non-market housing density. She exports summary statistics and includes map visuals in her council presentation to support targeted funding recommendations.

Without a dashboard this process would require manual data cleaning, spatial joins, and repeated analysis.

Detail how the audience will interact with the app.

### User Stories / JTBD

1. Spatial Equity Analysis
    - **User Story**: A housing planner wants to filter developments by local area so that they can identify neighbourhoods that are underserved by non-market housing.
    - **JTBD**: When evaluating city-wide distribution, they want to see the number of projects and units per local area so they can recommend geographically equitable funding allocations.
2. Demographic Equity Analysis
    - **User Story**: A policy analyst wants to filter by clientele type (families, seniors, other) so they can determine whether developments align with demographic needs.
    - **JTBD**: When reviewing housing policies, the policy analyst wants to compare family and senior unit counts across neighbourhoods so they can prioritize appropriate housing types.
3. Equitable Accessibility Analysis
    - **User Story**: A member of a non-profit housing provider for people with disabilites wants to view accessible and adaptable unit counts in different neighbourhoods so they can determine where to propose a new development.
    - **JTBD**: When assessing equity goals, they want to quickly visualize accessible units by area and over time so they can identify gaps in inclusive design.
