**1. Resolute Function:**
```php
function resolute($num) {
    $digits = str_split($num);
    while (count($digits) > 1) {
        $digits = str_split(array_sum($digits));
    }
    return intval($digits[0]);
}
```