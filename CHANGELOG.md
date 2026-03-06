# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.3.0]

### Added

### Changed
- removed titles from clientele bar chart and development count vs. occupancy year to make card titles more consistent.

### Fixed

### Known Issues

### Reflection

## [0.2.0]

### Added
- Interactive map showing non-market housing developments as point markers.
- Total count of selected developments based on current filter selections.
- Accessibility pie chart to summarize accessible/adaptable design-related unit counts for the filtered set of developments.
- Clientele bar chart to compare unit totals by clientele group (Families, Seniors, Other).
- Occupancy year line chart to show development counts over time based on first occupancy year.
- Filters for Local Area, Operator, and Project Status to support interactive exploration across all dashboard components.

### Changed
- Reorganized the layout by moving all filters into a left-side sidebar to make the filtering workflow more consistent and easier to scan.
- Adjusted layout proportions by using a smaller map footprint to create space for additional charts and summaries without overcrowding the page.

  
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
