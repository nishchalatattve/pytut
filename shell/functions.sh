# !/bin/bash


fruits=("apple" "banana" "cherry")

print_fruits(){
    for fruit in "${fruits[@]}"; do
        echo "I like $fruit"
    done
}

print_fruits