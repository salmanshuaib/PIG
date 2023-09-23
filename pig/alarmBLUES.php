**4. Time-Based Notifications for BLUE Team (PHP):**
```php
// Example code to check and trigger notifications for BLUE Team members
$current_time = date("h:i A");
$sql = "SELECT * FROM blue_team WHERE alarm_time = '$current_time'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        // Trigger notifications for BLUE Team members
        echo "Notification for: " . $row["name"] . " - " . $row["text_constant"];
    }
} else {
    echo "No notifications at this time.";
}
```
