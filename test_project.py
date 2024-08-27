import pytest
from project import number_of_lines,set_goal,add,delete,clear

def test_number_of_lines():
    assert number_of_lines("Records.csv") == 0

def test_set_goal(monkeypatch):

    def mock_input(prompt):
        return '5'

    monkeypatch.setattr('builtins.input', mock_input)

    set_goal()
    assert number_of_lines("Goal.txt") == 1

def test_add(monkeypatch):

    def mock_input(prompt):
        if prompt == "What's the task? :":
            return "Chapter One"
        elif prompt == "Would you like to continue? (Y/N)":
            return "n"
    monkeypatch.setattr("builtins.input", mock_input)
    add()
    assert number_of_lines("Records.csv") == 2

def test_delete(monkeypatch):
    def mock_input(prompt):
        return 1
    monkeypatch.setattr("builtins.input", mock_input)
    delete()
    assert number_of_lines("Records.csv") == 1

def test_clear():
    clear("Records.csv")
    clear("Goal.txt")
    assert number_of_lines("Records.csv") == 0
    assert number_of_lines("Goal.txt") == 0









