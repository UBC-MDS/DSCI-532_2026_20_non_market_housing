## Reactivity Diagram

```mermaid
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

```python
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

