package pacman

type stage struct {
	matrix   []string
	lives    int
	maxLives int
}

// każdy znaczek odpowiada za konkretny element (ściana,duszek itp)
var stage1 = stage{
	[]string{
		"3888888888888888885",
		"gqrrrrrrrrrrrrrrrqg",
		"gr6rrrrrr6rrrrrr6rg",
		"grgrrrrrrgrrrrrrgrg",
		"grorrrrrrorrrrrrorg",
		"grrrrrrrrrrrrrrrrrg",
		"gr02rrrrrrrrrrr02rg",
		"grikrrrrrrrrrrrikrg",
		"grrrror39t75rorrrrg",
		"gr6rrrrgvuwgrrrr6rg",
		"grgrr6rl888nr6rrgrg",
		"grorrrrrrrrrrrrrorg",
		"grrrrrrrr6rrrrrrrrg",
		"gr02rrrrrgrrrrr02rg",
		"grikrrrrrorrrrrikrg",
		"gqrrrrrrrrrprrrrrqg",
		"l88888888888888888n",
	},
	1,
	2,
}

var defaultStage = &stage1
