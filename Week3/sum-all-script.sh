
read -a arr
sum=0
for i in "${arr[@]}"
    do
    sum=`expr $sum + $i`
done

echo $sum


# arr=("$@") takes an array of numbers inline