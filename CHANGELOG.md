# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/).\

## [0.4.0] - 2026-03-17

### Added

- <!-- New features, components, tests - one line each. Reference PRs where relevant (e.g. #12). -->
- Added reset filters button (#125)
- Show neighbourhood polygons on the map (#113)
- Added filtering based on map lasso selection (#113)
- Add tests verifying logic of the dashboard (#117)

### Changed

- <!-- Spec or design deviations, and motivation. -->
- <!-- Feedback items you addressed: "Addressed: <item description> (#<prioritization issue>) via #<PR>" -->
- Changed data to lazy loading with parquet + DuckDB as outlined in the milestone (#104 via #120)

### Fixed

- Fixed accessibility pie chart tooltip bug where filtered dataframe with zero entries still displayed "Total Number of Units: 1" (#112 via #124).
- Fixed occupancy line chart bug where unnecessary trailing zeros appeared on y-axis when dataframe filtered for zero entries (#112 via #124).
- Fixed clientele bar chart bug where unnecessary trailing zeros appeared on y-axis when dataframe filtered for zero entries (#112 via #124). 
- Fix the querychat error message appearing on use (#119, #111, via #120)
- Fix points not rendering properly on the map (#115 via #113)

- **Feedback prioritization issue link:** https://github.com/UBC-MDS/DSCI-532_2026_20_non_market_housing/issues/107

### Known Issues

- <!-- Anything incomplete or broken TAs should be aware of (so it isn't mistaken for unfinished work). -->

### Release Highlight: Map Lasso Selection Feature

The dashboard was updated so that if the lasso tool was used to select a portion of the map, other outputs would be filtered according to the selection. This allows the user to create custom selections of areas of the map and view information about the area, rather than only being limited to local area in terms of spatial filtering.

- **Option chosen:** D
- **PR:** #113
- **Why this option over the others:** As discussed in the issue, the map is central to the workflow and making it interactive as an input lets users drill down spatially and see how the rest of the dashboard updates.
- **Feature prioritization issue link:** https://github.com/UBC-MDS/DSCI-532_2026_20_non_market_housing/issues/105

### Collaboration

<!-- Summary of workflow or collaboration improvements made since M3. -->

- **CONTRIBUTING.md:** https://github.com/UBC-MDS/DSCI-532_2026_20_non_market_housing/pull/127
- **M3 retrospective:** More efforts to limit the scope of our PRs.
- **M4:** We tried limiting the scope of our PRs by creating separate pull requests, though in some cases there was overlap that made it difficult to fully separate (for example, changing the type of our map along with other map updates).

### Reflection
Our non-market housing dashboard successfully displays important information about current non-market housing developments across Vancouver to planners and policymakers. It has an aesthetic layout displaying important attributes and information at the top of the dashboard and an interactive map at the bottom of the dashboard allowing for further exploration. This layout adheres to both DSCI 531 visualization and DSCI 542 communication best practices as the layout considers the user's tendency to read information from left to right and top to bottom. This allows for an easy-to-understand flow of information as the user reads it starting with summary statistics (like total development and unit count) in the top left, moving to descriptive plots in the tope right, and finally the map at the bottom. Furthermore, the filtering of the dashboard is quite intuitive. Combined with the above points, this provides an easy and accessible experience for the user. A current limitation of the dashboard includes a lack of guidance for the user, as while the dashboard is quite intuitive to use, it would be beneficial to have a "help" button that could describe some of its features if a user gets lost.

We aimed to categorize feedback concerning actual bugs (incorrect map rendering, incorrect information displayed in the tooltips, etc.) as critical, and those concerning general cosmetic changes as non-critical. These prioritizations are detailed in issue 107. 

In general, all the feedback was very helpful in informing our work on this milestone. Each piece of feedback from both peers and instructors provided us with features to add or improve that we would not have thought of otherwise. Getting new eyes on the dashboard was very useful. Furthermore, lectures 7 and 8 of this course were incredibly important in helping us implement both Parquet + DuckDB and our testing modules respectively. 

-   **Unit test: correct clientele totals are aggregated**

    -   This test checks that the clientele bar chart data is summed correctly for Families, Seniors, and Other. It matters because if the aggregation logic changes, the chart could show wrong totals and give users a misleading summary of the data.

-   **Unit test: missing or non-numeric values are handled safely**

    -   This test checks that blanks, text values, or invalid entries do not break the calculation. It is important because dashboard data is not always perfectly clean, and if this behavior changes, the chart could either crash or display incorrect numbers.

-   **Unit test: missing clientele columns fail safely**

    -   This test checks the fallback case where the expected clientele columns are not present in the input data. It matters because if the data structure changes in the future, the function should still return something safe instead of causing the dashboard to fail.

-   **Playwright test: default dashboard KPI matches the data**

    -   This test checks that the dashboard shows the correct default KPI value when the page first loads. It is important because if the default filtering logic changes, the number shown on the page may no longer match the actual dataset.

-   **Playwright test: local area filter updates total units correctly**

    -   This test checks that selecting a Local Area changes the Total Units value to the correct filtered result. It matters because users depend on the filters to explore the data, and if this breaks, the dashboard summaries would no longer reflect what users selected.

-   **Playwright test: edge-case filter can return zero projects without breaking**

    -   This test checks that the dashboard can handle a valid filter combination that returns no matching rows. It is important because empty subsets are a normal edge case, and if this behavior changes, the app could crash instead of handling zero results properly.


## [0.3.0]

### Added

-   Add LLM assistant chat page that can filter data for visuals on the page.
-   Table of data in the assistant page.
-   Download button for filtered data in the assistant page, with clickable URLs.
-   Tooltip functionality to the line and bar charts in the dashboard.
-   Added clientele bar chart and accessibility pie chart to the Assistant tab.

### Changed

-   removed titles from clientele bar chart and development count vs. occupancy year to make card titles more consistent.

### Fixed

### Known Issues

### Reflection

This week’s milestone focused on adding an AI-powered Assistant tab to the dashboard. The team implemented the querychat interface, connected it to a dataframe output showing the filtered results, added two visualizations that update based on the AI-filtered data, and included a download button so users can export the filtered dataframe. Compared with last week’s milestone, which mainly focused on building the core dashboard layout and implementing the initial visualizations using Shiny’s grid layout and reactive structure, this week emphasized integrating the LLM functionality into the app and ensuring the visual components respond dynamically to the querychat results. Instructor feedback also highlighted areas for further improvement, such as improving layout balance, refining CSS colors, making titles more consistent, and adding interactive features like hover effects to make the dashboard clearer and more polished.

## [0.2.0]

### Added

-   Interactive map showing non-market housing developments as point markers.
-   Total count of selected developments based on current filter selections.
-   Accessibility pie chart to summarize accessible/adaptable design-related unit counts for the filtered set of developments.
-   Clientele bar chart to compare unit totals by clientele group (Families, Seniors, Other).
-   Occupancy year line chart to show development counts over time based on first occupancy year.
-   Filters for Local Area, Operator, and Project Status to support interactive exploration across all dashboard components.

### Changed

-   Reorganized the layout by moving all filters into a left-side sidebar to make the filtering workflow more consistent and easier to scan.
-   Adjusted layout proportions by using a smaller map footprint to create space for additional charts and summaries without overcrowding the page.

## Milestone 2 Reflection

### Implementation Status

Every job story and their corresponding components have been implemented, as demonstrated in the section with all added elements.

### Deviations

The layout was reorganized so that the filter bar is in the left sidebar, making it easier to identify and use. The size of the map was also made smaller in order to avoid overcrowding and create more space for the other output.

### Known Issues

The map does not always show every project as a marker - we believe this to be an issue with ipyleaflet.

### Best Practices

### Self-Assessment

**Strengths:** The filtering pipeline is robust. All four filters compose correctly via a single reactive query, and every visualization updates in response. The interactive map provides an intuitive spatial entry point that was central to the M1 proposal.

**Limitations:** The dashboard currently lacks visual polish and the general performance of the app could be improved. The map does not yet support boundary polygons for local areas, which would strengthen the spatial equity story.

**Future improvements (M3+):** Improve performance, overlay local-area boundary polygons on the map and improve the visual design of the app.
