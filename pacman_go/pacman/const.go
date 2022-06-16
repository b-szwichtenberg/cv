package pacman

const (
	backgroundImageSize = 100
	stageBlocSize       = 32
)

type input int

const (
	_ input = iota
	up
	right
	down
	left
	rKey
)

type element int

const (
	w0                element = iota //0
	w1                               //1
	w2                               //2
	w3                               //3
	w4                               //4
	w5                               //5
	w6                               //6
	w7                               //7
	w8                               //8
	w9                               //9
	w10                              //a
	w11                              //b
	w12                              //c
	w13                              //d
	w14                              //e
	w15                              //f
	w16                              //g
	w17                              //h
	w18                              //i
	w19                              //j
	w20                              //k
	w21                              //l
	w22                              //m
	w23                              //n
	w24                              //o
	playerElement                    // p
	bigDotElement                    // q
	dotElement                       // r
	empty                            // s
	blinkyElement                    // t
	clydeElement                     // u
	inkyElement                      // v
	pinkyElement                     // w
	backgroundElement                //x
)
