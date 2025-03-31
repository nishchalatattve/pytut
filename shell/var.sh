# !/bin/bash


a=99
echo $a

b="Hiiiii"
echo $b

fruits=("apple" "banana" "cherry")

for fruit in "${fruits[@]}"; do
    echo "I like $fruit"
done
