:- use_module(library(aoc_utils)).

range_contains([[S1, E1], [S2, E2]]) :-
    S2 =< S1, E1 =< E2
  ; S1 =< S2, E2 =< E1.

range_overlaps([[S1, E1], [S2, E2]]) :-
  \+ (E1 < S2; E2 < S1).

solve(L, P1, P2) :-
  count(range_contains, L, P1),
  count(range_overlaps, L, P2).

%% Parser
input(L) --> sequence1(line, "\n", L).
line([R1, R2]) --> range(R1), ",", range(R2).
range([S, E]) --> integer(S), "-", integer(E).

%% Output
:- initialization(aoc_utils:run, main).
output(P1, P2) :- output_nums(P1, P2).
