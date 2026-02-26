# Vancouver Non-Market Housing Dashboard App Specification - Group 20

## Component Inventory

| ID | Type | Shiny widget / renderer | Depends on | Job story |
| --- | --- | --- | --- | --- |
| `input_local_area` | Input | `ui.input_selectize` | - | 2, 3 |
| `input_operator` | Input | `ui.input_selectize` | - | 2, 3 |
| `input_status` | Input | `ui.input_checkbox` | - | 2, 3 |
| `input_year` | Input | `ui.input_slider` | - | 2, 3 |
| `filtered_df` | Reactive Calc | `@reactive.calc` | `input_local_area`, `input_operator`, `input_project_status`, `input_year` | 1, 2, 3 |
| `filtered_map` | Output | `@render_widget` | `filtered_df` | 1 |
| `count_total_filtered` | Output | `@render.text` | `filtered_df` | 1 |
| `clientele_bar_chart` | Output | `@render_widget` | `filtered_df` | 3 |
| `occupancy_year_line_chart` | Output | `@render_widget` | `filtered_df` | 2 |
| `design_pie_chart` | Output | `@render_widget` | `filtered_df` | 3 |
