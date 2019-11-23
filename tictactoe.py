# -*- coding: utf-8 -*-

# Created on Mon Sep  9 15:54:45 2019
# @author: C.-C. Chan
# A python implementation of the tic-tac-toe game from David Tourezky's Lisp version
#
# -- P2_6497.py - Modified by Patrick M. Howard - For academic purposes only! --

import random

def makeBoard():
    return ['board', 0, 0, 0, 0, 0, 0, 0, 0, 0]

_computer = 10
_playerTwo = 10
_playerOne = 1
_triplets = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def convertToLetter(v):
    if v == 1:
        return 'O'
    elif v == 10:
        return 'X'
    else:
        return ' '
    
def printRow(x, y, z):
    print('\t {0:3} | {1:3} | {2:3} '.format(convertToLetter(x), convertToLetter(y), 
          convertToLetter(z)))
    
#need to fix print board layout    
def print_board(board):
    printRow(board[1], board[2], board[3])
    print('\t-----------------'.center(10))
    printRow(board[4], board[5], board[6])
    print('\t-----------------'.center(10))
    printRow(board[7], board[8], board[9])

def makeMove(player, pos, board):
    board[pos] = player
    return board

def sumTriplet(board, triplet):
    return board[triplet[0]] + board[triplet[1]] + board[triplet[2]]

def computeSums (board):
    return [sumTriplet(board, triplet) for triplet in _triplets]

def winnerP (board, twoPlayerGame):
    sums = computeSums(board)
    if twoPlayerGame:
        return 3 * _playerTwo in sums or 3 * _playerOne in sums
    else:
        return 3 * _computer in sums or 3 * _playerOne in sums

def playerOneMove(board, twoPlayerGame):
#    print('in opponent:')
#    print(board)
    print('\nPlayer one! Your turn!')
    pos = readALegalMove(board)
    new_board = makeMove(_playerOne, pos, board)
    print_board(new_board)
    if winnerP(new_board, twoPlayerGame):
        print('You win!')
    elif boardFullP(new_board):
        print('Tie game.')
    else:
        if twoPlayerGame:
            playerTwoMove(new_board, twoPlayerGame)
        else:
            computerMove(new_board)

def playerTwoMove(board, twoPlayerGame):
#    print('in opponent:')
#    print(board)
    print('\nPlayer two! Your turn!')
    pos = readALegalMove(board)
    new_board = makeMove(_playerTwo, pos, board)
    print_board(new_board)
    if winnerP(new_board, twoPlayerGame):
        print('You win!')
    elif boardFullP(new_board):
        print('Tie game.')
    else:
        playerOneMove(new_board, twoPlayerGame)

def readALegalMove(board):
    pos = int(input('Your move: (enter a number between 1 and 9) '))
    if not (type(pos) == int and (pos >= 1 and pos <=9)):
        print('Invalid input.')
        readALegalMove(board)
    elif board[pos] != 0:
        print('That space is already occupied.')
        readALegalMove(board)
    else:
        return pos

def boardFullP(board):
    return not 0 in board

def computerMove(board):
#    print('In computer move:')
#    print(board)
    best_move = chooseBestMove(board)
    pos = best_move[0]
    strategy = best_move[1]
    new_board = makeMove(_computer, pos, board)
    print('My move: {} '.format(pos))
    print('My strategy: {} '.format(strategy))
    print_board(new_board)
    if winnerP(new_board, False):
        print('I win!')
    elif boardFullP(new_board):
        print('Tie game.')
    else:
        return playerOneMove(new_board, False)

def chooseBestMove(board):
#    print('choose move: ')
#    print(board)
    possibilites = computeSums(board)
    i = 0
    for possibility in possibilites:
        if(possibility == 20) and (possibility <= 21):
            return completeThreeStrategy(board, i)
        elif(possibility == 2):
            return blockingStrategy(board, i)
        else:
            i += 1
            
    return randomMoveStrategy(board)

def completeThreeStrategy(board, tripletIndex):
    return [findEmptyPositionInTriplet(board, tripletIndex), "Complete Three Strategy"]

            
def blockingStrategy(board, tripletIndex):
    return [findEmptyPositionInTriplet(board, tripletIndex), "Blocking strategy"]

def findEmptyPositionInTriplet(board, tripletIndex):
    for position in _triplets[tripletIndex]:
        if board[position] == 0:
            return position


def randomMoveStrategy(board):
    pos = pickRandomEmptyPosition(board)
#    print('value of pos in random move strategy: ' + repr(pos))
    return [pos, 'random move']

def pickRandomEmptyPosition(board):
    pos = random.choice(list(range(9))) + 1
    if board[pos] == 0:
        return pos
    else:
        return pickRandomEmptyPosition(board)

def playAgainstTheMachine():
    choice = input('Would you like to go first? (y/n): ')
    if choice == 'y':
        playerOneMove(makeBoard(), False)
    else:
        computerMove(makeBoard())

def playAgainstAnotherPlayer():
    choice = input('Who should go first? (1/2): ');
    if choice == '1':
        playerOneMove(makeBoard(), True)
    else:
        playerTwoMove(makeBoard(), True)

def mainMenu():
    print('\nTic Tac Toe - Artificial Intelligence Project II');
    print('Created by Dr. Chan, Extended by Patrick M. Howard\n');
    print('0.) Play against the machine');
    print('1.) Play against another player');
    print('2.) Exit\n');

    selection = int(input('Please select an option: '));
    if not (type(selection) == int) and (selection < 0 or selection > 2):
        print(f'Not sure what {selection} is, please try again');
        mainMenu();
    
    if selection == 2:
        quit();
    elif selection == 1:
        playAgainstAnotherPlayer();
    elif selection == 0:
        playAgainstTheMachine();

mainMenu();