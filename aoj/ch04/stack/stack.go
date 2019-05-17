package stack

type Stack struct {
	Top int
	S   [1000]int
}

func (s *Stack) Push(x int) {
	s.Top++
	s.S[s.Top] = x
}

func (s *Stack) Pop() int {
	s.Top--
	return s.S[s.Top+1]
}

func New() *Stack {
	return &Stack{
		Top: 0,
		S:   [1000]int{},
	}
}
