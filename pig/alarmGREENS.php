**4. Time-Based Notifications for GREEN Team (PHP):**
```php
// Example code to check and trigger notifications for GREEN Team members
$current_time = date("h:i A");
$sql = "SELECT * FROM green_team WHERE alarm_time = '$current_time'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        // Trigger notifications for GREEN Team members
        echo "Notification for: " . $row["name"] . " - " . $row["text_constant"];
    }
} else {
    echo "No notifications at this time.";
}
```
