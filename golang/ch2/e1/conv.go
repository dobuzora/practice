package e1

func CtoF(c Celsius) Fahrenheit { return Fahrenheit(c*9/5 + 32) }
func CtoK(c Celsius) Kelvin     { return Kelvin(c - AbsoluteZero) }

func FtoC(f Fahrenheit) Celsius { return Celsius((f - 32) * 5 / 9) }
func FtoK(f Fahrenheit) Kelvin  { return Kelvin(FtoC(f) - AbsoluteZero) }

func KtoC(k Kelvin) Celsius    { return Celsius(k + Kelvin(AbsoluteZero)) }
func KtoF(k Kelvin) Fahrenheit { return Fahrenheit(CtoF(KtoC(k))) }
