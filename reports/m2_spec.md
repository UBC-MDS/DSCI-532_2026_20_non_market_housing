## Reactivity Diagram

```mermaid
flowchart TD
  A[/input_local_area/] --> F{{filtered_df}}
  B[/input_clientele/] --> F
  C[/input_operator/] --> F
  D[/input_design/] --> F
  E[/input_status/] --> F

  F --> M([filtered_map])
  F --> BC([clientele_bar_chart])
  F --> LC([occupancy_year_line_chart])
  F --> CV([count_total_filtered])
```

`filtered_df` is a `@reactive.calc` that calls the following function:

```python
def filter_data():
    return clean_df.query(
        "`Local Area` in input.input_local_area() & "
        "`Project Status` in input.input_status() & "
        "Operator in input.input_operator() & "
        "Clientele in input.input_clientele() & "
        "Design in input.input_design()"
    )
```
