package pacman

import (
	"github.com/hajimehoshi/ebiten"
	"github.com/hajimehoshi/ebiten/inpututil"
)

//w przypadku wciśnięcia odpowiedniego przycisku oddany jest dany kierunek bądź funkcja (restart)
func keyPressed() input {
	if inpututil.KeyPressDuration(ebiten.KeyLeft) > 0 {
		return left
	}
	if inpututil.KeyPressDuration(ebiten.KeyUp) > 0 {
		return up
	}
	if inpututil.KeyPressDuration(ebiten.KeyDown) > 0 {
		return down
	}
	if inpututil.KeyPressDuration(ebiten.KeyRight) > 0 {
		return right
	}
	if inpututil.KeyPressDuration(ebiten.KeyA) > 0 {
		return left
	}
	if inpututil.KeyPressDuration(ebiten.KeyW) > 0 {
		return up
	}
	if inpututil.KeyPressDuration(ebiten.KeyS) > 0 {
		return down
	}
	if inpututil.KeyPressDuration(ebiten.KeyD) > 0 {
		return right
	}
	if inpututil.IsKeyJustPressed(ebiten.KeyR) {
		return rKey
	}

	return 0
}
