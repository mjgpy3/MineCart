#!/bin/bash

find .. -name "*.pyc" | xargs rm &> /dev/null
find .. -name "*.swp" | xargs rm &> /dev/null

