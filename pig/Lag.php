function groupLettersByResolute($input) {
    $groups = [];
    foreach (str_split($input) as $letter) {
        $resolute = ams(mapLetterToNumber($letter));
        $groups[$resolute][] = $letter;
    }
    return $groups;
}
