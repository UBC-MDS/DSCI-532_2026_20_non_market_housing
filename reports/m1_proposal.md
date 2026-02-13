# Vancouver Non-Market Housing Dashboard Proposal - Group 20

## Motivation and Purpose

Vancouver is currently experiencing an affordable housing crisis, ranking as the **4th most unaffordable housing market in the world**. Non-market housing is an incredibly important strategy to ease the burden of this suffocating housing market on low- to moderate-income families and individuals. As such, the housing co-operatives, government agencies, and independent non-profit societies that fund and control the development of non-market housing need a tool to help examine the areas in which their current efforts are successful.
Such a tool would allow non-market housing planners to identify underserved local areas, target demographics, development status of the different projects in the city, along with several other summary statistics. This would ultimately inform planning and help to establish a fair and equitable network of non-market housing across the city.

## Description of the Data

The [City of Vancouver's Non-Market Housing Dataset](https://opendata.vancouver.ca/explore/dataset/non-market-housing/information/) contains 641 rows (each representing a unique non-market housing development) and 27 columns (attributes describing project characteristics). The attributes in each column will either be used to filter data or be visualized in some way on our dashboard to assist non-market housing planners in making decisions. The relevance of each attribute is summarized below:

| Feature | Description | Relevance |
| --- | --- | --- |
| `Index Number` | Unique identifier within the City Non-Market Housing Inventory. | Will not be relevant to our dashboard. |
| `Name` | Name of the specified housing project. | Will be displayed when hovering over the associated point on the map of our dashboard. |
| `Address` | Street address of the specified housing project in Vancouver. | Will be displayed when hovering over the associated point on the map of our dashboard. |
| `Project Status` | Current development status of project: Completed, Under Construction, Approved, and Proposed | A bar chart will display the number of each category for the desired filter selection. |
| `Occupancy Year` | Year when the specified housing project was initially occupied. | A slider will be used to filter developments by occupancy year. Will also display a line chart showing the trend of project counts over time. |
| `Operator` | Operator of the specified housing project. | A search bar will be used to filter the data for a specific operator. A table will display the project count for each operator. |
| `Clientele- Families` | Number of units that have two or more bedrooms. | A bar chart will display total number of each category for the desired filter selection. Will also use clientele as a filter. |
| `Clientele - Seniors` | Number of units for individuals typically over age 55. | A bar chart will display total number of each category for the desired filter selection. Will also use clientele as a filter. |
| `Clientele - Other` | Number of units for single non-seniors. | A bar chart will display total number of each category for the desired filter selection. Will also use clientele as a filter. |
| `Design - Accessible 1BR` | Number of one-bedroom units designed for a person with disabilities to be able to, without assistance, approach, enter, pass to and from, and make use of an area and its facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Accessible 2BR` | Number of two-bedroom units that that are designed for a person with disabilities to be able to, without assistance, approach, enter, pass to and from, and make use of an area and its facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Accessible 3BR` | Number of three-bedroom units that that are designed for a person with disabilities to be able to, without assistance, approach, enter, pass to and from, and make use of an area and its facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Accessible 4BR` | Number of four-bedroom units that that are designed for a person with disabilities to be able to, without assistance, approach, enter, pass to and from, and make use of an area and its facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Accessible Studio` | Number of studio units that that are designed for a person with disabilities to be able to, without assistance, approach, enter, pass to and from, and make use of an area and its facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Accessible Room` | Number of housekeeping or sleeping units that that are designed for a person with disabilities to be able to, without assistance, approach, enter, pass to and from, and make use of an area and its facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Adaptable 1BR` | Number of one-bedroom units that are designed to be able to be modified to meet the changing accessibility needs of residents. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Adaptable 2BR` | Number of two-bedroom units that are designed to be able to be modified to meet the changing accessibility needs of residents. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Adaptable 3BR` | Number of three-bedroom units that are designed to be able to be modified to meet the changing accessibility needs of residents. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Adaptable 4BR` | Number of four-bedroom units that are designed to be able to be modified to meet the changing accessibility needs of residents. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Standard 1BR` | Number of one-bedroom units designed for a typical standard of liveability which includes sleeping and cooking facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Standard 2BR` | Number of two-bedroom units designed for a typical standard of liveability which includes sleeping and cooking facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Standard 3BR` | Number of three-bedroom units designed for a typical standard of liveability which includes sleeping and cooking facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Standard 4BR` | Number of four-bedroom units designed for a typical standard of liveability which includes sleeping and cooking facilities. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Standard Studio` | Number of studio units units designed for a typical standard of liveability which includes sleeping and cooking facilities. A studio, also known as bachelor unit, combines bedroom, living room, and kitchen into a single unit. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `Design - Standard Room` | Number of housekeeping or sleeping units designed for a typical standard of liveability which includes sleeping and cooking facilities. A studio, also known as bachelor unit, combines bedroom, living room, and kitchen into a single unit. | A bar chart will display total number of each category for the desired filter selection. Will also use design as a checkbox filter. |
| `URL` | City's webpage address of the specified housing project. | The contents of the url will be displayed when the user hovers over the related point on the map. |
| `Geom` | Spatial (point) representation of feature. | The geometry will be used to display the location of each non-market housing development on the map. |

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
