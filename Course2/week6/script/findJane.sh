#!/usr/bin/env bash

> oldFiles.txt
var=/Users/rakeshravindran/PycharmProjects/PythonED/CourseraGoogle/Course2/week6
files=$(grep ' jane ' ../data/list.txt | cut -d' ' -f3 )

for file in $files; do
    if test -e $var$file; then echo $file >> oldFiles.txt;
    else echo "$file File doesn't exist";
    fi

done


