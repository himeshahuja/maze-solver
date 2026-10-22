import asyncio
import random
import pygame
from gamestate import GameState
from game import game_loop
from menu import menu_loop



async def main():
    while True:
        state = GameState()
        await menu_loop(state)
        await game_loop(state, state.rows, state.cols, state.algorithm, [])


asyncio.run(main())
