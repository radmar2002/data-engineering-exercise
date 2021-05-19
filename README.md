# data-engineering-exercise

data-engineering-exercise

### T1:

Given an input as json array (each element is a flat dictionary) write a program that will parse this json, and return a nested dictionary of dictionaries of arrays, with keys specified in command line arguments and the leaf values as arrays of flat dictionaries matching appropriate groups
`python nest.py nesting_level_1 nesting_level_2 ... nesting_level_n`

Example:
`cat input.json | python nest.py currency country city`

### T2:

REST service from the first task
