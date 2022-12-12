:- module(aoc_utils,
          [ sequence1//2,
            sequence1//3,

            identity/2,

            map_sum/3,
            count/3,
            replace1/4,

            output_nums/2,
            output_strings/2,
            run/0
          ]).

:- reexport(library(clpfd)).
:- reexport(library(dcg/basics)).
:- reexport(library(func)).

% Helper higher-order dcgs
sequence1(Elem, [H|T]) -->
    call(Elem, H), sequence1(Elem, T).
sequence1(Elem, [H]) -->
    call(Elem, H).

sequence1(Elem, Sep, [H|T]) -->
    call(Elem, H), Sep, sequence1(Elem, Sep, T).
sequence1(Elem, _,   [H]) -->
    call(Elem, H).

% Helper relations
identity(X, X).

% Helper list relations
map_sum(F, L, R) :-
  maplist(F, L, Temp), sum_list(Temp, R).

count(Pred, L, C) :-
  include(Pred, L, Temp), length(Temp, C).

replace1(N, L, E, R) :-
  nth1(N, L, _, Temp),
  nth1(N, R, E, Temp).

% Helper output functions
output_nums(P1, P2) :-
  format("Part 1: ~d~n", [P1]),
  format("Part 2: ~d~n", [P2]).

output_strings(P1, P2) :-
  format("Part 1: ~s~n", [P1]),
  format("Part 2: ~s~n", [P2]).

% Default runner
:- use_module(library(pio)).
run :-
  current_prolog_flag(argv, [File]),
  phrase_from_file((input(L), ("\n" | [])), File),
  solve(L, P1, P2),
  output(P1, P2),
  halt(0).
