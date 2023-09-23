```php
// MODIFY FOLLOWING FUNCTION TO RELY ON resolute FUNCTION WHILST MAPPING. FOR EXAMPLE, J RESOLVES TO 1; S ALSO RESOLVES 
// TO 1; A IS ALREADY RESOLVED TO 1 - THEREFORE "AJS" ARE GROUPED TOGETHER. OTHER GROUPINGS INCLUDE BKT, CLU, DMV.... . 
THERE ARE 9 GROUPINGS THAT POPULATE EACH OF THE TABLES (5).  
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