# Vancouver Non-Market Housing Dashboard App Specification - Group 20

## Updated Job Stories

| \# | Job Story | Status | Notes |
|---------------:|---------------------|----------------|--------------------|
| 1 | When I am a city housing planner doing a quick scan of non-market housing coverage, I want to narrow developments by local area, operator, and project status, so I can clearly see which projects fall into my selected scope and confirm the total number of developments included in that selection for planning and funding discussions. | 🔄 Revised | Updates the old spatial story from “projects and units per local area” to the implemented workflow: filtering and confirming the total selected developments for the chosen subset. |
| 2 | When I am a policy analyst preparing a progress update, I want to look at changes in housing delivery across occupancy years while applying the same filters (local area, operator, project status), so I can compare delivery patterns between neighbourhoods and project stages and identify periods where delivery accelerates or slows down. | 🔄 Revised | Adds an explicit time-based delivery view that was not captured in the old stories. Shifts from a static neighbourhood comparison to a trend-focused analysis that still supports equity questions. |
| 3 | When I am a non-profit housing provider advocating for inclusive and needs-aligned housing, I want to examine accessibility coverage and the clientele mix for any filtered subset (local area, operator, project status), so I can identify gaps (e.g., low accessible/adaptable supply or limited seniors/family focus) and justify where a new proposal or partnership should be prioritized. | 🔄 Revised | Merges the old demographic and accessibility stories into one equity decision workflow. |

## Component Inventory

| ID | Type | Shiny widget / renderer | Depends on | Job story |
|---------------|---------------|---------------|---------------|---------------|
| `input_local_area` | Input | `ui.input_selectize` | \- | 1, 2, 3 |
| `input_operator` | Input | `ui.input_selectize` | \- | 1, 2, 3 |
| `input_status` | Input | `ui.input_checkbox_group` | \- | 1, 2, 3 |
| `input_occupied` | Input | `ui.input_checkbox` | \- | 1, 2, 3 |
| `input_year` | Input | `ui.input_slider` | \- | 1, 2, 3 |
| `reset_filters` | Input | `ui.input_action_button` | \- | \- |
| `filtered_df` | Reactive Calc | `@reactive.calc` | `input_local_area`, `input_operator`, `input_status`, `input_year`, `input_occupied` | 1, 2, 3 |
| `display_df` | Reactive Calc | `@reactive.calc` | `filtered_df` | \- |
| `filtered_map` | Output | `@render_widget` | `filtered_df` | 1 |
| `count_total_filtered` | Output | `ui.value_box` | `display_df` | 1 |
| `count_total_units` | Output | `ui.value_box` | `display_df` | \- |
| `clientele_bar_chart` | Output | `@render_widget` | `display_df` | 3 |
| `occupancy_year_line_chart` | Output | `@render_widget` | `display_df` | 2 |
| `design_pie_chart` | Output | `@render_widget` | `display_df` | 3 |

## Reactivity Diagram

``` mermaid
flowchart TD
  A[/input_local_area/] --> F{{filtered_df}}
  B[/input_operator/] --> F
  C[/input_occupied/] --> F
  D[/input_year/] --> F
  E[/input_status/] --> F

  F --> G([display_df])

  F --> M([filtered_map])
  G --> BC([clientele_bar_chart])
  G --> LC([occupancy_year_line_chart])
  G --> CV([count_total_filtered])
  G --> CU([count_total_units])
  G --> DS([design_pie_chart])
```

`filtered_df` is a `@reactive.calc` that calls the following function:

```python
def filtered_df():
    local_area = input.input_local_area()
    operator = input.input_operator()
    occupied = input.input_occupied()
    year_min, year_max = input.input_year()
    status = input.input_status()

    if not local_area:
        local_area = local_areas
    if not operator:
        operator = list(operator_choices.keys())
    if not status:
        status = list(status_choices.keys())

    filtered = clean_df.query(
        "`Local Area` in @local_area & "
        "`Operator` in @operator & "
        "`Project Status` in @status"
    )

    if occupied:
        year_mask = (
            filtered["`Occupancy Year`"].isna() |
            (filtered["Occupancy Year"].between(year_min, year_max))
        )
    else:
        year_mask = filtered["Occupancy Year"].between(year_min, year_max)

    return filtered[year_mask]
```

`display_df` is a `@reactive.calc` that filters `filtered_df` by the projects selected using the map's lasso tool if it is currently active.

## Calculation Details

### `filtered_df`

The `@reactive.calc` `filtered_df` depends on the following inputs:

-   `input_local_area`
-   `input_operator`
-   `input_occupied`
-   `input_year`
-   `input_status`

It filters rows in the dataframe to the selected local area, operator, whether the project is occupied, year of occupancy, and status.

It is consumed by the following outputs:

-   `filtered_map`

It is also consumed by the `@reactive.calc` `display_df`, which filters the dataframe if the lasso tool is active. This, in turn, is consumed by the following outputs:

-   `clientele_bar_chart`
-   `occupancy_year_line_chart`
-   `count_total_filtered`
- `count_total_units`
-   `design_pie_chart`
