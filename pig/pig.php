function enqueue_plugin_script() {
    // Enqueue the JavaScript file for your plugin
    wp_enqueue_script('plugin-script', plugin_dir_url(__FILE__) . 'plugin-script.js', array('jquery'), '1.0.0', true);
}

add_action('admin_enqueue_scripts', 'enqueue_plugin_script');


function pig_activate() {
    global $wpdb;

    // Create tables as before

    // Sample data for demonstration
    $sampleInput = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // Replace with your input data

    // Group letters by resolute
    $letterGroups = groupLettersByResolute($sampleInput);

    // Map and insert letter groups into the tables
    foreach ($letterGroups as $resolute => $group) {
        // Adjust table number based on your requirements
        $tableNumber = $resolute % 5 + 1; // Assuming 5 tables numbered from 1 to 5

        $table = $wpdb->prefix . 'table_' . $tableNumber;

        $columnsData = mapLettersToColumns($group, $tableNumber);

        if (!empty($columnsData)) {
            $wpdb->insert($table, $columnsData);
        }
    }
}

register_activation_hook(__FILE__, 'pig_activate');
