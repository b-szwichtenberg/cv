package pacman

import (
	"github.com/hajimehoshi/ebiten"
	pacmanImages "github.com/kgosse/pacmanresources/images"
)

type player struct {
	images                                          [8]*ebiten.Image
	currentImage                                    int
	previousPosition, currentPosition, nextPosition position
	initialPosition                                 position
	speed                                           int
	stepsLength                                     position
	steps                                           int
	direction                                       input
	score                                           int
	countExplosion                                  int
	pm                                              *particleManager
	lost                                            bool
}

func newPlayer(y, x int) *player {
	p := &player{}
	p.loadImages()
	p.pm = newParticleManager(pacmanImages.PacParticle_png, 0, 0)
	p.currentPosition = position{y, x}
	p.previousPosition = position{y, x}
	p.nextPosition = position{y, x}
	p.initialPosition = position{y, x}
	return p
}

func (p *player) loadImages() {
	copy(p.images[:], loadImages(pacmanImages.PlayerImages[:]))
}

func (p *player) draw(screen *ebiten.Image) {
	if p.isExploding() {
		p.pm.draw(screen)
		return
	}
	if p.lost {
		return
	}
	x := float64(p.currentPosition.x*stageBlocSize + p.stepsLength.x)
	y := float64(p.currentPosition.y*stageBlocSize + p.stepsLength.y)
	op := &ebiten.DrawImageOptions{}
	op.GeoM.Translate(x, y)
	screen.DrawImage(p.image(), op)
}

func (p *player) image() *ebiten.Image {
	return p.images[p.currentImage]
}

func (p *player) move(m [][]element, direction input, cb func()) {
	// początek wybuchu
	if p.isExploding() {
		p.countExplosion++
		p.pm.move()
		// jego koniec
		if p.countExplosion == 60 {
			p.reset()
			cb()
		}
		return
	}
	// brak ruchu oraz kierunku
	if !p.isMoving() && direction == 0 {
		return
	}
	if !p.isMoving() && direction != 0 {
		if !canMove(m, addPositionDirection(direction, p.currentPosition)) {
			return
		}
		p.updateDirection(direction)
	}
	// określenie szybkości by ruch nie wyglądał jak teleportacja
	if p.steps <= 1 || p.steps >= 6 {
		p.speed = 4
	} else {
		p.speed = 5
	}
	switch p.direction {
	case up:
		p.stepsLength.y -= p.speed
	case right:
		p.stepsLength.x += p.speed
	case down:
		p.stepsLength.y += p.speed
	case left:
		p.stepsLength.x -= p.speed
	}

	if p.steps > 5 {
		p.updateImage(false)
	} else {
		p.updateImage(true)
	}

	p.steps++

	if p.steps >= 7 {
		p.endMove()
	}
}

func (p *player) reset() {
	p.currentPosition, p.previousPosition, p.nextPosition = p.initialPosition, p.initialPosition, p.initialPosition
	p.currentImage = 0
	p.countExplosion = 0
	p.stepsLength = position{0, 0}
	p.steps = 0
}

func (p *player) isMoving() bool {
	if p.steps > 0 {
		return true
	}
	return false
}

func (p *player) updateDirection(d input) {
	p.stepsLength = position{0, 0}
	p.direction = d
	p.nextPosition = addPositionDirection(d, p.currentPosition)
	p.previousPosition = p.currentPosition
}

func (p *player) endMove() {
	p.currentPosition = p.nextPosition
	p.stepsLength = position{0, 0}
	p.steps = 0
}

func (p *player) updateImage(openMouth bool) {
	switch p.direction {
	case up:
		if openMouth {
			p.currentImage = 7
		} else {
			p.currentImage = 6
		}
	case right:
		if openMouth {
			p.currentImage = 1
		} else {
			p.currentImage = 0
		}
	case down:
		if openMouth {
			p.currentImage = 3
		} else {
			p.currentImage = 2
		}
	case left:
		if openMouth {
			p.currentImage = 5
		} else {
			p.currentImage = 4
		}
	}
}

func (p *player) screenPosition() (y, x float64) {
	x = float64(p.currentPosition.x*stageBlocSize + p.stepsLength.x)
	y = float64(p.currentPosition.y*stageBlocSize + p.stepsLength.y)
	return
}

func (p *player) explode() {
	if p.isExploding() {
		return
	}
	x := float64(p.currentPosition.x*stageBlocSize + p.stepsLength.x)
	y := float64(p.currentPosition.y*stageBlocSize + p.stepsLength.y)
	p.currentPosition.x = 0
	p.currentPosition.y = 0
	p.pm.reset(x, y)
	p.countExplosion = 1
}

func (p *player) isExploding() bool {
	if p.countExplosion > 0 {
		return true
	}
	return false
}

func (p *player) reinit() {
	p.reset()
	p.score = 0
	p.lost = false
}

func (p *player) gameover() {
	p.lost = true
	p.currentPosition.x = 0
	p.currentPosition.y = 0
}
