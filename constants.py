SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 1.0 # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_BASE_XP_DROP = 10
ASTEROID_BASE_SCORE = 20

# PLAYER_RADIUS = 20
PLAYER_SHAPE_HEIGHT = 40
PLAYER_SHAPE_BASE = 20
PLAYER_TURN_SPEED = 300 # degrees per second
PLAYER_SPEED = 200 # pixels per second
PLAYER_LEVEL = 0
PLAYER_LEVEL_MAX = 100
PLAYER_BASE_LEVEL_UP_XP = 100
PLAYER_BASE_ACCELERATION = 0.0 # pixels per second^2
PLAYER_BASE_LIVES = 3
PLAYER_BASE_SCORE = 0

SCORE_TO_XP = 0.5 # 1 score = 0.5 xp

SHOT_RADIUS = 5
SHOT_SPEED = 500 # pixels per second
SHOT_COOLDOWN = 0.2 # seconds

WEAPONS = [{
    "name": "Basic blaster",
    "damage": 1,
    "cooldown": 0.2,
    "speed": 500,
},{
  "name": "Double blaster",
    "damage": 2,
    "cooldown": 0.2,
    "speed": 1000,
}, {
    "name": "Plasma blaster",
    "damage": 4,
    "cooldown": 0.5,
    "speed": 1500,
}, {
    "name": "Laser blaster",
    "damage": 8,
    "cooldown": 1.0,
    "speed": 2000,
}, {
    "name": "Rocket launcher",
    "damage": 6,
    "cooldown": 2.0,
    "speed": 1000,
}]

SHIELDS = [{
    "name": "Basic shield",
    "health": 10,
    "regen": 1,
}, {
    "name": "Double shield",
    "health": 20,
    "regen": 1,
}, {
    "name": "Plasma shield",
    "health": 40,
    "regen": 4,
}, {
    "name": "Laser shield",
    "health": 60,
    "regen": 6,
}]

THRUSTERS = [{
    "name": "Basic thruster",
    "acceleration": 0.1,
}, {
    "name": "Double thruster",
    "acceleration": 0.2,
}, {
    "name": "ION thruster",
    "acceleration": 0.4,
}, {
    "name": "Gravity thruster",
    "acceleration": 0.6,
}]