from game.game_state import GameState

def main():
    try:
        game = GameState()
        game.run()
    except Exception as e:
        print(f"Error in game: {e}")

if __name__ == '__main__':
    main()