:- use_module(library(aoc_utils)).

% {X, Y} coded as 0: Rock,    1: Paper, 2: Scissors
% R      coded as 0: Y loses, 1: tie,   2: Y wins
match(X, Y, R) :-
  X in 0..2, Y in 0..2, R in 0..2,
  R #= (Y - X + 1) mod 3.

score(_, P2, R, S) :- S is (P2 + 1) + R * 3.

player_player([X, Y], Score) :-
  match(X, Y, R), score(X, Y, R, Score).
player_result([X, R], Score) :-
  match(X, Y, R), score(X, Y, R, Score).

solve(L, P1, P2) :-
  map_sum(player_player, L, P1),
  map_sum(player_result, L, P2).

%% Parser
input(L) --> sequence1(game, "\n", L).
game([X, Y]) --> [X0], " ", [Y0],
  { char_code('A', OrdA), X is X0 - OrdA,
    char_code('X', OrdX), Y is Y0 - OrdX
  }.

%% Output
:- initialization(aoc_utils:run, main).
output(P1, P2) :- output_nums(P1, P2).
