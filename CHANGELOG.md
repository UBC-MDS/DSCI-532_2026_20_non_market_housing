# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

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
