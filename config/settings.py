APP_VERSION="1.2a"

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

BGM_VOLUME = 1.0

PLAYER_SHAPE_HEIGHT = 40
PLAYER_SHAPE_BASE = 30
PLAYER_BASE_ACCELERATION = 1.0 # pixels per second^2
PLAYER_SPEED = 200 * PLAYER_BASE_ACCELERATION # pixels per second
PLAYER_TURN_SPEED = 300 # degrees per second
PLAYER_LEVEL_MAX = 100
PLAYER_BASE_SCORE = 0
PLAYER_BASE_LIVES = 3


LEVEL_UP_XP = 500
SCORE_TO_XP = 0.5 # 1 score = 0.5 xp

SHOT_RADIUS = 2.5
SHOT_SPEED = 500 # pixels per second
SHOT_COOLDOWN = 0.2 # seconds

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 1.0 # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_BASE_XP_DROP = 10
ASTEROID_BASE_SCORE = 20