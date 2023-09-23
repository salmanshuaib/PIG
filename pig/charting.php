function mapLettersToColumns($group, $tableNumber) {
    // Define the column names for the tables, adjust as needed
    $columns = [
        1 => ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'],
        2 => ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'],
        3 => ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'],
        4 => ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'],
        5 => ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'],
    ];

    // Map the group to columns
    if (isset($columns[$tableNumber])) {
        $tableColumns = $columns[$tableNumber];
        $mappedColumns = [];
        foreach ($group as $index => $letter) {
            $columnIndex = $index % count($tableColumns);
            $columnName = $tableColumns[$columnIndex];
            $mappedColumns[$columnName] = $letter;
        }
        return $mappedColumns;
    }

    return [];
}
