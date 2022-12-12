:- use_module(library(aoc_utils)).

priority(C, P) :-
    char_type(C, lower), char_code('a', Orda), P is  1 + (C - Orda)
  ; char_type(C, upper), char_code('A', OrdA), P is 27 + (C - OrdA).
common(Ls, V) :- maplist(member(V), Ls).

common_by_line(Line, R) :-
  length(X, N), length(Y, N),
  append(X, Y, Line),
  common([X, Y], R).

chunks(_, [], []).
chunks(N, L, [C|Cs]) :-
  length(C, N),
  append(C, Rest, L),
  chunks(N, Rest, Cs).

solve(L, P1, P2) :-
  map_sum(priority of common_by_line, L, P1),

  chunks(3, L, Cs),
  map_sum(priority of common, Cs, P2).

%% Parser
input(L) --> sequence1(line, "\n", L).
line(L)  --> sequence1(char, L).
char(C)  --> [C], { char_type(C, alpha) }.

%% Output
:- initialization(aoc_utils:run, main).
output(P1, P2) :- output_nums(P1, P2).
