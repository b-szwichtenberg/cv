package pacman

import (
	"container/list"

	"github.com/hajimehoshi/ebiten"
	pacmanImages "github.com/kgosse/pacmanresources/images"
)

type bigDotManager struct {
	dots   *list.List
	gc     *list.List
	images [2]*ebiten.Image
	count  int
}

func newBigDotManager() *bigDotManager {
	bd := &bigDotManager{}
	bd.dots = list.New()
	bd.gc = list.New()
	bd.loadImages()
	return bd
}

func (b *bigDotManager) loadImages() {
	b.images[0] = loadImage(pacmanImages.BigDot1_png)
	b.images[1] = loadImage(pacmanImages.BigDot2_png)
}

func (b *bigDotManager) add(y, x int) {
	b.dots.PushBack(position{y, x})
}

func (b *bigDotManager) draw(sc *ebiten.Image) {
	b.count++
	var img *ebiten.Image
	if b.count%10 == 0 {
		img = b.images[1]
	} else {
		img = b.images[0]
	}

	for e := b.dots.Front(); e != nil; e = e.Next() {
		d := e.Value.(position)
		x := float64(d.x * stageBlocSize)
		y := float64(d.y * stageBlocSize)
		op := &ebiten.DrawImageOptions{}
		op.GeoM.Translate(x, y)
		sc.DrawImage(img, op)
	}
}

func (b *bigDotManager) detectCollision(m [][]element, p position, cb func()) {
	if m[p.y][p.x] == bigDotElement {
		cb()
	}
}

func (b *bigDotManager) delete(p position) {
	for e := b.dots.Front(); e != nil; e = e.Next() {
		v := e.Value.(position)
		if v.x == p.x && v.y == p.y {
			b.gc.PushBack(b.dots.Remove(e).(position))
			return
		}
	}
}

func (b *bigDotManager) reinit(m [][]element) {
	e := b.gc.Front()
	for {
		if e == nil {
			break
		}
		v := e.Value.(position)
		cur := e
		e = e.Next()
		b.dots.PushBack(b.gc.Remove(cur))
		m[v.y][v.x] = bigDotElement
	}
}

func (b *bigDotManager) empty() bool {
	if b.dots.Len() == 0 {
		return true
	}
	return false
}
