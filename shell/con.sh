# !/bin/bash


# If else
if [ 99 == 1 ]; then
    echo "True"
else
    echo "False"
fi

if [ 99 -eq 1 ]; then
    echo "True"
else
    echo "False"
fi

if [ 99 -ne 1 ]; then
    echo "True"
else
    echo "False"
fi

if [ 99 != 1 ]; then
    echo "True"
else
    echo "False"
fi


if [ 88 -ge 90 ]; then
    echo "Grade: A"
elif [ 88 -gt 60 ]; then
    echo "Grade: D"
else
    echo "Grade: F"
fi


# For loop
echo "For loop"
for i in {1..5}; do
    echo "Number: $i"
done


# While loop
echo "While loop"
i=1
while [ $i -le 5 ]; do
    echo "Number: $i"
    ((i++))
done
