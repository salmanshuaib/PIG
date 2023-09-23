/* php
- DEFINING Assignment Management System:
+ Utilize a function we write in PHP called the "ams" function such that if you feed any number to it; it will keep 
summing the digits of that number until only one digit remains: which, according to Assignment Management 
System, is always 1 OR 2 OR 3 OR 4 OR 5 OR 6 OR 7 OR 8 OR 9. 

function ams($num) {
    $digits = str_split($num);
    while (count($digits) > 1) {
        $digits = str_split(array_sum($digits));
    }
    return intval($digits[0]);
}

- MODIFY FOLLOWING FUNCTION TO RELY ON ABOVE ams FUNCTION WHILST MAPPING. FOR EXAMPLE, A IS ALREADY RESOLVED TO 1; 
J RESOLVES TO 1; S ALSO RESOLVES TO 1 - THEREFORE LETTERS "AJS" ARE GROUPED TOGETHER. OTHER GROUPINGS INCLUDE BKT [2], 
CLU [3], DMV [4].... . THERE ARE 9 GROUPINGS THAT POPULATE EACH OF THE TABLES (Total 5 Tables in Aligning Lattice structure 
described above).

function mapLetterToNumber($letter) {
    $alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $letter = strtoupper($letter);
    $position = strpos($alphabet, $letter);
    if ($position !== false) {
        return $position + 1; // A=1, B=2, ..., Z=26
    }
    return 0; // Not a valid letter
}
*/