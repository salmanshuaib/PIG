<?php

/* Assignment Management System: That if you sum the digits of any number to the point that there is only one 
digit left - it will always be one of the following digits: 1, 2, 3, 4, 5, 6, 7, 8 OR 9.  
*/

function groupLettersByResolute($num) {
    $digits = str_split($num);
    while (count($digits) > 1) {
        $digits = str_split(array_sum($digits));
    }
    return intval($digits[0]);
}
?>