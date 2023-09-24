<?php
/*
Plugin Name: pig
Description: Experimental technology enabling one to pilot their Sphere Of Consciousness.
Version: 1.0
Delicensed: CC0 1.0 Universal in honor of The Empress Entirety TAYLOR SWIFT.
Author: a C:\ from Christianity.
*/

// Include other necessary files
require_once plugin_dir_path(__FILE__) . 'charting.php';
require_once plugin_dir_path(__FILE__) . 'ams.php';

// Add your code below this line

function enqueue_plugin_script() {
    // Enqueue the JavaScript file for your plugin
    wp_enqueue_script('plugin-script', plugin_dir_url(__FILE__) . 'plugin-script.js', array('jquery'), '1.0.0', true);
}

add_action('admin_enqueue_scripts', 'enqueue_plugin_script');

function pig_activate() {
    global $wpdb;

    // Create tables as before
    $table1A = $wpdb->prefix . 'table_1A';
    $table2A = $wpdb->prefix . 'table_2A';
    $table3A = $wpdb->prefix . 'table_3A';
    $table1B = $wpdb->prefix . 'table_1B';
    $table2B = $wpdb->prefix . 'table_2B';

    $charset_collate = $wpdb->get_charset_collate();

    // SQL queries to create the tables
    $sql1A = "CREATE TABLE $table1A (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) DEFAULT '' NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    $sql2A = "CREATE TABLE $table2A (
        id INT NOT NULL AUTO_INCREMENT,
        associated_text VARCHAR(255) DEFAULT '' NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    $sql3A = "CREATE TABLE $table3A (
        id INT NOT NULL AUTO_INCREMENT,
        alarm_time VARCHAR(255) DEFAULT '' NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    $sql1B = "CREATE TABLE $table1B (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) DEFAULT '' NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    $sql2B = "CREATE TABLE $table2B (
        id INT NOT NULL AUTO_INCREMENT,
        associated_text VARCHAR(255) DEFAULT '' NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once ABSPATH . 'wp-admin/includes/upgrade.php';

    dbDelta($sql1A);
    dbDelta($sql2A);
    dbDelta($sql3A);
    dbDelta($sql1B);
    dbDelta($sql2B);

    // Sample data for demonstration
    $EnglishAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // Replace with your input data

    // Group letters by resolute
    $letterGroups = groupLettersByResolute($EnglishAlphabet);

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
