from game.character_stats.player_stats import player
from game.movement.travel import room_choosing, rooms

game = room_choosing(player, rooms)
