package pacman

import (
	"math/rand"
	"time"

	"github.com/hajimehoshi/ebiten"
)

type ghost struct {
	kind                                            element
	currentImage                                    int
	previousPosition, currentPosition, nextPosition position
	initialPosition                                 position
	speed                                           int
	stepsLength                                     position
	steps                                           int
	direction                                       input
	vision                                          int
	countVulnerable                                 int
	vulnerableMove                                  bool
	eaten                                           bool
	lost                                            bool
}

func init() {
	rand.Seed(time.Now().UnixNano())
}

func newGhost(y, x int, k element) *ghost {
	return &ghost{
		kind:             k,
		previousPosition: position{y, x},
		currentPosition:  position{y, x},
		nextPosition:     position{y, x},
		initialPosition:  position{y, x},
		stepsLength:      position{},
		speed:            4,
		vision:           getVision(k),
	}
}

func getVision(e element) int {
	switch e {
	case pinkyElement:
		return 10
	case inkyElement:
		return 15
	case blinkyElement:
		return 50
	case clydeElement:
		return 60
	default:
		return 0
	}
}

func (g *ghost) draw(screen *ebiten.Image, imgs []*ebiten.Image) {
	if g.lost {
		return
	}
	x := float64(g.currentPosition.x*stageBlocSize + g.stepsLength.x)
	y := float64(g.currentPosition.y*stageBlocSize + g.stepsLength.y)
	op := &ebiten.DrawImageOptions{}
	op.GeoM.Translate(x, y)
	screen.DrawImage(g.image(imgs), op)
}

func (g *ghost) image(imgs []*ebiten.Image) *ebiten.Image {
	if g.isVulnerable() {
		i := g.currentImage + 8
		if i >= len(imgs) {
			i = 8
		}
		return imgs[i]
	}
	return imgs[g.currentImage]
}

func (g *ghost) isVulnerable() bool {
	if g.countVulnerable > 0 {
		return true
	}
	return false
}

func (g *ghost) move() {
	switch g.direction {
	case up:
		g.stepsLength.y -= g.speed
	case right:
		g.stepsLength.x += g.speed
	case down:
		g.stepsLength.y += g.speed
	case left:
		g.stepsLength.x -= g.speed
	}

	if g.steps%4 == 0 {
		g.updateImage()
	}
	g.steps++

	if g.vulnerableMove {
		g.countVulnerable++
		if g.steps == 16 {
			g.endMove()
			if g.countVulnerable >= 360 {
				g.endVulnerability()
			}
		}
		return
	}

	if g.steps == 8 {
		g.endMove()
	}
}

func (g *ghost) endVulnerability() {
	g.vulnerableMove = false
	g.countVulnerable = 0
	g.eaten = false
}

func (g *ghost) updateImage() {
	if g.isVulnerable() {
		if g.countVulnerable <= 310 {
			if g.currentImage == 0 {
				g.currentImage = 1
			} else {
				g.currentImage = 0
			}
		} else {
			if g.currentImage == 2 {
				g.currentImage = 3
			} else {
				g.currentImage = 2
			}
		}
		return
	}

	switch g.direction {
	case up:
		if g.currentImage == 6 {
			g.currentImage = 7
		} else {
			g.currentImage = 6
		}
	case right:
		if g.currentImage == 0 {
			g.currentImage = 1
		} else {
			g.currentImage = 0
		}
	case down:
		if g.currentImage == 2 {
			g.currentImage = 3
		} else {
			g.currentImage = 2
		}
	case left:
		if g.currentImage == 4 {
			g.currentImage = 5
		} else {
			g.currentImage = 4
		}
	}
}

func (g *ghost) endMove() {
	g.previousPosition = g.currentPosition
	g.currentPosition = g.nextPosition
	g.stepsLength = position{0, 0}
	g.steps = 0
}

func (g *ghost) isMoving() bool {
	if g.steps > 0 {
		return true
	}
	return false
}

func (g *ghost) findNextMove(m [][]element, pac position) {
	if g.isVulnerable() {
		g.vulnerableMove = true
		g.speed = 2
	} else {
		g.speed = 4
	}

	switch g.localisePlayer(m, pac) {
	case up:
		g.direction = up
	case right:
		g.direction = right
	case down:
		g.direction = down
	case left:
		g.direction = left
	default:

		for _, v := range rand.Perm(5) {
			if v == 0 {
				continue
			}
			direction := input(v)
			np := addPositionDirection(direction, g.currentPosition)
			if canMove(m, np) && np != g.previousPosition {
				g.direction = direction
				g.nextPosition = np
				return
			}
		}

		g.direction = oppDirection(g.direction)
	}
	g.nextPosition = addPositionDirection(g.direction, g.currentPosition)
}

func (g *ghost) localisePlayer(m [][]element, pac position) input {
	if g.isVulnerable() {
		return 0
	}

	maxY := len(m)
	maxX := len(m[0])

	if g.currentPosition.x == pac.x && g.currentPosition.y > pac.y {
		for y, v := g.currentPosition.y-1, 1; y >= 0 && v <= g.vision && !isWall(m[y][g.currentPosition.x]); y, v = y-1, v+1 {
			if y == pac.y {
				return up
			}
		}
	}

	if g.currentPosition.x == pac.x && g.currentPosition.y < pac.y {
		for y, v := g.currentPosition.y+1, 1; y < maxY && v <= g.vision && !isWall(m[y][g.currentPosition.x]); y, v = y+1, v+1 {
			if y == pac.y {
				return down
			}
		}
	}

	if g.currentPosition.y == pac.y && g.currentPosition.x < pac.x {
		for x, v := g.currentPosition.x+1, 1; x < maxX && v <= g.vision && !isWall(m[g.currentPosition.y][x]); x, v = x+1, v+1 {
			if x == pac.x {
				return right
			}
		}
	}

	if g.currentPosition.y == pac.y && g.currentPosition.x > pac.x {
		for x, v := g.currentPosition.x-1, 1; x >= 0 && v <= g.vision && !isWall(m[g.currentPosition.y][x]); x, v = x-1, v+1 {
			if x == pac.x {
				return left
			}
		}
	}

	return 0
}

func (g *ghost) makeVulnerable() {
	g.countVulnerable = 1
}

func (g *ghost) screenPosition() (y, x float64) {
	x = float64(g.currentPosition.x*stageBlocSize + g.stepsLength.x)
	y = float64(g.currentPosition.y*stageBlocSize + g.stepsLength.y)
	return
}

func (g *ghost) reset() {
	g.previousPosition, g.currentPosition, g.nextPosition = g.initialPosition, g.initialPosition, g.initialPosition
	g.stepsLength = position{}
	g.currentImage = 0
	g.direction = 0
	g.steps = 0
}

func (g *ghost) makeEaten() {
	g.eaten = true
}

func (g *ghost) isEaten() bool {
	return g.eaten
}

func (g *ghost) reinit() {
	g.reset()
	g.lost = false
	g.speed = 4
	g.endVulnerability()
}

func (g *ghost) gameover() {
	p := position{0, 0}
	g.previousPosition, g.currentPosition, g.nextPosition = p, p, p
	g.lost = true
}
