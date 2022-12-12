:- use_module(library(aoc_utils)).

solve(L, P1, P2) :-
  maplist(sum_list, L, Sums),
  sort(0, @>=, Sums, [A,B,C|_]),
  P1 = A,
  P2 = A + B + C.

%% Parser
input(L) --> sequence1(block, "\n\n", L).
block(L) --> sequence1(integer, "\n", L).

%% Output
:- initialization(aoc_utils:run, main).
output(P1, P2) :- output_nums(P1, P2).
