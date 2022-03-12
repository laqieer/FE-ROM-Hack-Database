var filtersConfig = {
  // instruct TableFilter location to import ressources from
  base_path: 'https://unpkg.com/tablefilter@latest/dist/tablefilter/',
  col_2: 'select',
  col_3: 'select',
  col_4: 'select',
  col_5: 'select',
  alternate_rows: true,
  rows_counter: true,
  btn_reset: true,
  loader: true,
  mark_active_columns: true,
  highlight_keywords: true,
  no_results_message: true,
  col_types: [
    'number', 'string', 'string', 'string', 'string', 'string', 'string', 'string'
  ],
  extensions: [{
    name: 'sort',
    images_path: 'https://unpkg.com/tablefilter@latest/dist/tablefilter/style/themes/'
  }]
};

var tf = new TableFilter('roms', filtersConfig);
tf.init();