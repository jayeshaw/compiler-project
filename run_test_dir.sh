#!/bin/bash

# if [ $# -eq 1]; then
#     cd ./"$1"
# fi

for file in "$1"/*; do
    cat template.c > new.c
    cat "$file" >> new.c
    echo "------------ Testing: $file ------------"
    gcc -w new.c
    rm new.c
    ./a.out > gccOutput.txt
    ./compile_test.sh "$file"
    # DIFF = $(diff gccOutput.txt codeOutput.txt)
    # if [ $DIFF != "" ]
    # then 
    #     echo DIFF
    # else
    #     echo "TEST PASSED"

    # fi
    diff gccOutput.txt codeOutput.txt
    rm a.out gccOutput.txt codeOutput.txt
done
