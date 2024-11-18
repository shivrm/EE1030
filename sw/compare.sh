TIMEFORMAT="%R"

num_iter=4

for i in {1..20}
do
    n=$((5*$i))
    for j in {1..$num_iter}
    do
        ./bin/generate $n matrix.txt
        echo "Gram-Schmidt: n=$n: " && time ./bin/gram_schmidt $n matrix.txt > /dev/null 
        echo "Householder: n=$n: " && time ./bin/householder $n matrix.txt > /dev/null
    done
done

