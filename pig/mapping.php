```php
// Define a function to map letters to numbers
function mapLetterToNumber($letter) {
    $alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $letter = strtoupper($letter);
    $position = strpos($alphabet, $letter);
    if ($position !== false) {
        return $position + 1; // A=1, B=2, ..., Z=26
    }
    return 0; // Not a valid letter
}
```