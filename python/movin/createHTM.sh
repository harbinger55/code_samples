#!/bin/bash

mkdir -p ./moveit
for i in {1..2000}; do dd if=/dev/urandom bs=1 count=1 of=./moveit/file$i.htm; done
