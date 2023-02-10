package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	//"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)

	sc.Scan()
	N, _ := strconv.Atoi(sc.Text())
	var carlist []int

	for i := 0; i < N; i++ {
		sc.Scan()
		carNumber, _ := strconv.Atoi(sc.Text())
		carlist = append(carlist, carNumber)
	}

	count := 0
	exitCarNumber := 1

	for exitCarNumber < N {
		currentCar := carlist[0]
		carlist = carlist[1:]

		if currentCar != exitCarNumber {
			carlist = append(carlist, currentCar)

			if currentCar == N {
				count++
			}
		} else {
			exitCarNumber++
		}
	}
	fmt.Println(count)
}
