# Vancouver Non-Market Housing Dashboard App Specification - Group 20

## Updated Job Stories

| \# | Job Story | Status | Notes |
| ---------------: | --------------------- | ---------------- | -------------------- |
| 1 | When I am a city housing planner doing a quick scan of non-market housing coverage, I want to narrow developments by local area, operator, and project status, so I can clearly see which projects fall into my selected scope and confirm the total number of developments included in that selection for planning and funding discussions. | 🔄 Revised | Updates the old spatial story from “projects and units per local area” to the implemented workflow: filtering and confirming the total selected developments for the chosen subset. |
| 2 | When I am a policy analyst preparing a progress update, I want to look at changes in housing delivery across occupancy years while applying the same filters (local area, operator, project status), so I can compare delivery patterns between neighbourhoods and project stages and identify periods where delivery accelerates or slows down. | 🔄 Revised | Adds an explicit time-based delivery view that was not captured in the old stories. Shifts from a static neighbourhood comparison to a trend-focused analysis that still supports equity questions. |
| 3 | When I am a non-profit housing provider advocating for inclusive and needs-aligned housing, I want to examine accessibility coverage and the clientele mix for any filtered subset (local area, operator, project status), so I can identify gaps (e.g., low accessible/adaptable supply or limited seniors/family focus) and justify where a new proposal or partnership should be prioritized. | 🔄 Revised | Merges the old demographic and accessibility stories into one equity decision workflow. |

## Component Inventory

| ID | Type | Shiny widget / renderer | Depends on | Job story |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| `input_local_area` | Input | `ui.input_selectize` | \- | 1, 2, 3 |
| `input_operator` | Input | `ui.input_selectize` | \- | 1, 2, 3 |
| `input_status` | Input | `ui.input_checkbox` | \- | 1, 2, 3 |
| `input_year` | Input | `ui.input_slider` | \- | 1, 2, 3 |
| `filtered_df` | Reactive Calc | `@reactive.calc` | `input_local_area`, `input_operator`, `input_project_status`, `input_year` | 1, 2, 3 |
| `filtered_map` | Output | `@render_widget` | `filtered_df` | 1 |
| `count_total_filtered` | Output | `ui.value_box` | `filtered_df` | 1 |
| `clientele_bar_chart` | Output | `@render_widget` | `filtered_df` | 3 |
| `occupancy_year_line_chart` | Output | `@render_widget` | `filtered_df` | 2 |
| `design_pie_chart` | Output | `@render_widget` | `filtered_df` | 3 |

## Reactivity Diagram

``` mermaid
flowchart TD
  A[/input_local_area/] --> F{{filtered_df}}
  B[/input_operator/] --> F
  C[/input_year/] --> F
  D[/input_status/] --> F

  F --> M([filtered_map])
  F --> BC([clientele_bar_chart])
  F --> LC([occupancy_year_line_chart])
  F --> CV([count_total_filtered])
  F --> DS([design_pie_chart])
```

`filtered_df` is a `@reactive.calc` that calls the following function:

``` python
def filter_data():
    return clean_df.query(
        "`Local Area` in input.input_local_area() & "
        "Operator in input.input_operator() & "
        "`Occupancy Year` in input.input_year() & "
        "`Project Status` in input.input_status() & "
    )
```

## Calculation Details

### `filtered_df`

The `@reactive.calc` `filtered_df` depends on the following inputs:

- `input_local_area`
- `input_operator`
- `input_year`
- `input_status`

It filters rows in the dataframe to the selected local area, operator, year of occupancy, and status.

It is consumed by the following outputs:

- `filtered_map`
- `clientele_bar_chart`
- `occupancy_year_line_chart`
- `count_total_filtered`
- `design_pie_chart`
- `filtered_map`
- `clientele_bar_chart`
- `occupancy_year_line_chart`
- `count_total_filtered`
- `design_pie_chart`
