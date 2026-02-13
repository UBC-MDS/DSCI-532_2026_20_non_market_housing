# Vancouver Non-Market Housing Dashboard Proposal - Group 20

## Motivation and Purpose

Vancouver is currently experiencing an affordable housing crisis, ranking as the **4th most unaffordable housing market in the world**. Non-market housing is an incredibly important strategy to ease the burden of this suffocating housing market on low- to moderate-income families and individuals. As such, the housing co-operatives, government agencies, and independent non-profit societies that fund and control the development of non-market housing need a tool to help examine the areas in which their current efforts are successful.
Such a tool would allow non-market housing planners to identify underserved local areas, target demographics, development status of the different projects in the city, along with several other summary statistics. This would ultimately inform planning and help to establish a fair and equitable network of non-market housing across the city.

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
| `Clientele- Families` | Number of units with 2+ bedrooms (family-oriented). | Filter option; aggregated into bar chart. |
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
| `URL` | Link to City webpage for the project. | displayed on map hover (clickable) |
| `Geom` | Spatial (point) representation of feature. | Used to plot project on map. |

We also plan on integrating the [City of Vancouver's Local Area Boundary Dataset](https://opendata.vancouver.ca/explore/dataset/local-area-boundary/information/?disjunctive.name) which contains the geometries of the major local areas in Vancouver. This will give users of our dashboard the ability to filter non-market housing developments by local area to examine those which are currently underserved. This dataset contains 22 rows (each representing a local area) and 3 columns which are summarized below:

| Feature | Description | Relevance |
| --- | --- | --- |
| `Name` | Official name of the local area. | Will be able to filter data by name of the local area. |
| `Geom` | Spatial representation of local area boundary. | Used to determine which local area each development falls within. |
| `geo_point_2d` | Spatial coordinate representing the center of the local area. | Will not be relevent to our dashboard. |

## Research Questions and Usage Scenarios

Detail how the audience will interact with the app.

- Persona: Brief description of a user.
Usage Scenario create a narrative describing user needs and context.
- User Stories / JTBD: Provide at least 3 User Stories or Job Stories that outline specific tasks the user needs to perform.
