## Calculation Details

### `filtered_df`

The `@reactive.calc` `filtered_df` depends on the following inputs:

- `input_local_area`
- `input_clientele`
- `input_operator`
- `input_design`
- `input_status`

It filters rows in the dataframe to the selected local area, clientele, operator, design, and status.

It is consumed by the following outputs:

- `filtered_map`
- `clientele_bar_chart`
- `occupancy_year_line_chart`
- `count_total_filtered`

