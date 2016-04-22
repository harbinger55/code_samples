#!/bin/bash

for i in {1..100}; do
  if ! (($i % 3)) && ! (( $i % 5 )); then
    echo "fizzbuzz"
  elif ! (( $i % 3 )); then
    echo "fizz"
  elif ! (( $i % 5)); then
    echo "buzz"
  else
    echo $i
  fi
done
