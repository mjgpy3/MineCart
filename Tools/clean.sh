#!/bin/bash

n_pyc=0
n_swp=0

find .. -name "*.pyc" | xargs rm &> /dev/null && n_pyc=$(($n_pyc+1))
find .. -name "*.swp" | xargs rm &> /dev/null && n_swp=$(($n_swp+1))

echo "Number of PYC: $n_pyc"
echo "Number of SWP: $n_swp"
