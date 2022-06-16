package pacman

import (
	"math"

	"github.com/hajimehoshi/ebiten"
	pacmanImages "github.com/kgosse/pacmanresources/images"
)

type ghostManager struct {
	ghosts              []*ghost
	images              map[element][8]*ebiten.Image
	vulnerabilityImages [5]*ebiten.Image
	eaten               int
}

func newGhostManager() *ghostManager {
	gm := &ghostManager{}
	gm.images = make(map[element][8]*ebiten.Image)
	gm.loadImages()
	return gm
}

func (gm *ghostManager) loadImages() {
	gm.images[blinkyElement] = loadGhostImages(pacmanImages.BlinkyImages)
	gm.images[clydeElement] = loadGhostImages(pacmanImages.ClydeImages)
	gm.images[inkyElement] = loadGhostImages(pacmanImages.InkyImages)
	gm.images[pinkyElement] = loadGhostImages(pacmanImages.PinkyImages)
	copy(gm.vulnerabilityImages[:], loadImages(pacmanImages.VulnerabilityImages[:]))
}

func (gm *ghostManager) draw(screen *ebiten.Image) {
	for i := 0; i < len(gm.ghosts); i++ {
		g := gm.ghosts[i]
		imgs, _ := gm.images[g.kind]
		images := make([]*ebiten.Image, 13)
		copy(images, imgs[:])
		copy(images[8:], gm.vulnerabilityImages[:])
		g.draw(screen, images)
	}
}

func (gm *ghostManager) move(m [][]element, pac position) {
	for i := 0; i < len(gm.ghosts); i++ {
		g := gm.ghosts[i]
		if !g.isMoving() {
			g.findNextMove(m, pac)
		}
		g.move()
	}
}

func (gm *ghostManager) makeVulnerable() {
	gm.eaten = 0
	for i := 0; i < len(gm.ghosts); i++ {
		gm.ghosts[i].makeVulnerable()
	}
}

func (gm *ghostManager) addGhost(y, x int, e element) {
	gm.ghosts = append(gm.ghosts, newGhost(y, x, e))
}

func (gm *ghostManager) detectCollision(pY, pX float64, cb func(bool, float64, float64)) {
	for i := 0; i < len(gm.ghosts); i++ {
		g := gm.ghosts[i]
		gY, gX := g.screenPosition()
		if math.Abs(pY-gY) < 32 && math.Abs(pX-gX) < 32 {
			if !g.isVulnerable() {
				cb(false, 0, 0)
				return
			}
			gm.eaten++
			g.makeEaten()
			g.reset()
			cb(true, gY, gX)
		}
	}
}

func (gm *ghostManager) reset(em *explosionManager, over bool) {
	for i := 0; i < len(gm.ghosts); i++ {
		g := gm.ghosts[i]
		y, x := g.screenPosition()
		em.addExplosion(pacmanImages.PacParticle_png, x, y)
		if over {
			g.gameover()
		} else {
			g.reset()
		}
	}
}

func loadGhostImages(g [8][]byte) [8]*ebiten.Image {
	var arr [8]*ebiten.Image
	copy(arr[:], loadImages(g[:]))
	return arr
}

func (gm *ghostManager) reinit() {
	for i := 0; i < len(gm.ghosts); i++ {
		g := gm.ghosts[i]
		g.reinit()
	}
}
