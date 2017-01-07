// 絶対温度で処理するために、型、定数、関数を追加
package e1

import "fmt"

type Celsius float64
type Fahrenheit float64
type Kelvin float64 // 型

const (
	AbsoluteZero Celsius = -273.15
	FreezingC    Celsius = 0
	BoilingC     Celsius = 100
)

func (c Celsius) String() string    { return fmt.Sprintf("%g℃ ", c) }
func (f Fahrenheit) String() string { return fmt.Sprintf("%g℉ ", f) }
func (k Kelvin) String() string     { return fmt.Sprintf("%gK", k) } // 関数
