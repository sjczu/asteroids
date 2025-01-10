from config.settings import PLAYER_SHAPE_HEIGHT

WEAPONS = [{
    "name": "Basic blaster",
    "damage": 1,
    "cooldown": 0.2,
    "speed": 500,
    "radius": 2.5
}, {
    "name": "Double blaster",
    "damage": 2,
    "cooldown": 0.2,
    "speed": 1000,
    "radius": 2.5
}, {
    "name": "Plasma blaster",
    "damage": 4,
    "cooldown": 0.5,
    "speed": 1500,
    "radius": 3.0
}, {
    "name": "Laser blaster",
    "damage": 8,
    "cooldown": 1.0,
    "speed": 2000,
    "radius": 4.0
}, {
    "name": "Rocket launcher",
    "damage": 6,
    "cooldown": 2.0,
    "speed": 1000,
    "radius": 5.0
}]

SHIELDS = [{
    "name": "Basic shield",
    "health": 10,
    "regen": 1,
    "radius": PLAYER_SHAPE_HEIGHT/2 + 5
}, {
    "name": "Double shield",
    "health": 20,
    "regen": 1,
    "radius1": PLAYER_SHAPE_HEIGHT/2 + 5,
    "radius2": PLAYER_SHAPE_HEIGHT/2 + 10
}, {
    "name": "Plasma shield",
    "health": 40,
    "regen": 4,
    "radius": PLAYER_SHAPE_HEIGHT/2 + 5
}, {
    "name": "Laser shield",
    "health": 60,
    "regen": 6,
    "radius": PLAYER_SHAPE_HEIGHT/2 + 5
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