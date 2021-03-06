from life.world import World
from life.coordinate import Coordinate
import pytest

class TestWorldTriominoes():
    def test_triomino_1_start_state(self):
        starting_state = {Coordinate(*c) for c in {(3, 1), (1, 2), (2, 1)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.state
        expected_state = {Coordinate(*c) for c in {(2, 1), (2, 2)}}
        assert expected_state == next_state
        world.next_state()
        next_state = world.state
        expected_state = set()
        assert expected_state == next_state

    def test_triomino_2_start_state(self):
        starting_state = {Coordinate(*c) for c in {(3, 2), (1, 2), (2, 2)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.state
        expected_state = {Coordinate(*c) for c in {(2, 3), (2, 1), (2, 2)}}
        assert expected_state == next_state
        world.next_state()
        next_state = world.state
        assert starting_state == next_state

    def test_triomino_3_start_state(self):
        starting_state = {Coordinate(*c) for c in {(1, 1), (1, 2), (2, 1)}}
        world = World(starting_state)
        expected_state = {Coordinate(*c) for c in {(1, 1), (1, 2), (2, 1), (2, 2)}}
        for i in range(10):
            world.next_state()
            next_state = world.state
            assert expected_state == next_state

    def test_triomino_4_start_state(self):
        starting_state = {Coordinate(*c) for c in {(3, 1), (1, 3), (2, 2)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.state
        expected_state = {Coordinate(*c) for c in {(2, 2)}}
        assert expected_state == next_state
        world.next_state()
        next_state = world.state
        expected_state = set()
        assert expected_state == next_state
