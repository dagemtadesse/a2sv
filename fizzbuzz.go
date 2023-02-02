import "fmt"

func fizzBuzz(n int) []string {
	var result []string

	for num := 1; num <= n; num++ {
		var newVal string = ""

		if num%3 != 0 && num%5 != 0 {
			newVal += fmt.Sprintf("%d", num)
		}

		if num%3 == 0 {
			newVal += "Fizz"
		}

		if num%5 == 0 {
			newVal += "Buzz"
		}
		result = append(result, newVal)
	}

	return result
}