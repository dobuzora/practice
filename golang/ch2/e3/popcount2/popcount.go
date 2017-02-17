package popcount2

var pc [256]byte

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&1)
	}
}

func PopCount(x uint64) int {
	var result byte
	for i := 0; i <= 8; i++ {
		result += pc[byte(x>>(uint64(i)*8))]
	}
	return int(result)
}
