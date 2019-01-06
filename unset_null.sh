#!/bin/bash

A=asdf

echo ${A=str}
unset A

echo ${A=str}

B=/home
C=$PATH
echo "$C"
C:=$B
echo "$C"


