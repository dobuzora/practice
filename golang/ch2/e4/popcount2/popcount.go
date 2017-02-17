package popcount2

var pc [256]byte

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&1)
	}
}

func PopCount(x uint64) int {
	count := 0
	for i := 0; i < 64; i++ {
		count += int(x>>uint64(i)) & 1
	}
	return count
}
