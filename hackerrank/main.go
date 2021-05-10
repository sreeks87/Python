package main

func main() {
	println("Pointer")
	var a int = 10
	p := &a
	println(a)
	println(&a)
	println(p)
	println(&p)
	println(*p)

}
