TIMEFORMAT="%R"

num_iter=4

for i in {1..50}
do
    n=$((5*$i))
    for j in {1..$num_iter}
    do
        ./bin/generate $n matrix.txt
        echo "Householder: n=$n: " && time ./bin/householder $n matrix.txt > /dev/null
    done
done

