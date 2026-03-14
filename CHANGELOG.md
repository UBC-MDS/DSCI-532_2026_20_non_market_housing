# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/).\

## [0.4.0] - 2026-03-17

### Added

- <!-- New features, components, tests - one line each. Reference PRs where relevant (e.g. #12). -->

### Changed

- <!-- Spec or design deviations, and motivation. -->
- <!-- Feedback items you addressed: "Addressed: <item description> (#<prioritization issue>) via #<PR>" -->
- Changed data to lazy loading with parquet + DuckDB as outlined in the milestone.

### Fixed

- Fixed accessibility pie chart tooltip bug where filtered dataframe with zero entries still displayed "Total Number of Units: 1".
- Fixed occupancy line chart bug where unnecessary trailing zeros appeared on y-axis when dataframe filtered for zero entries.
- Fixed clientele bar chart bug where unnecessary trailing zeros appeared on y-axis when dataframe filtered for zero entries.

- **Feedback prioritization issue link:** #...

### Known Issues

- <!-- Anything incomplete or broken TAs should be aware of (so it isn't mistaken for unfinished work). -->

### Release Highlight: [Name of your advanced feature]

<!-- One short paragraph describing what you built and what it does for the user. -->

- **Option chosen:** A / B / C / D
- **PR:** #...
- **Why this option over the others:** <!-- 1–2 sentences; link to your feature prioritization issue -->
- **Feature prioritization issue link:** #...

### Collaboration

<!-- Summary of workflow or collaboration improvements made since M3. -->

- **CONTRIBUTING.md:** <!-- Link to the PR that updated it with your M3 retrospective and M4 norms. -->
- **M3 retrospective:** <!-- What changed in your workflow after M3 collaboration feedback. -->
- **M4:** <!-- What you tried or improved this milestone. -->

### Reflection

<!-- Standard (see General Guidelines): what the dashboard does well, current limitations,
     any intentional deviations from DSCI 531 visualization best practices. -->

<!-- Trade-offs: one sentence on feedback prioritization - full rationale is in #<issue> and ### Changed above. -->

<!-- Most useful: which lecture, material, or feedback shaped your work most this milestone,
     and anything you wish had been covered. -->

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

TODO

### Deviations

TODO

### Known Issues

### Best Practices

### Self-Assessment

**Strengths:** The filtering pipeline is robust. All four filters compose correctly via a single reactive query, and every visualization updates in response. The interactive map provides an intuitive spatial entry point that was central to the M1 proposal.

**Limitations:** The dashboard currently lacks visual polish and the general performance of the app could be improved. The map does not yet support boundary polygons for local areas, which would strengthen the spatial equity story.

**Future improvements (M3+):** Improve performance, overlay local-area boundary polygons on the map and improve the visual design of the app.
