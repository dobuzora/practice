run:
	g++ -o merge merge_sort.cpp
	go build -o go-merge merge_sort.go
	gcc -o partition partition.c
	go build -o go-partition partition.go
	gcc -o quick quick_sort.c
	gcc -o counting counting_sort.c

clean:
	rm -f merge partition quick counting a.out go-merge go-partition
