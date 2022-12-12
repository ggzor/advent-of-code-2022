:- use_module(library(aoc_utils)).

apply_stack_move(Hook, [Amount, From, To], SsOld, SsNew) :-
  nth1(From, SsOld, OldFrom),
  nth1(To,   SsOld, OldTo),

  length(Items, Amount), append(NewFrom, Items, OldFrom),
  call(Hook, Items, NewItems),

  append(OldTo, NewItems, NewTo),
  replace1(From, SsOld,  NewFrom, SsNew0),
  replace1(To,   SsNew0, NewTo,   SsNew).

solve_with_hook(Hook, Ss, Ms, R) :-
  foldl(apply_stack_move(Hook), Ms, Ss, Sn),
  maplist(last, Sn, Ls),
  string_chars(R, Ls).

solve([Ss, Ms], P1, P2) :-
  solve_with_hook(reverse,  Ss, Ms, P1),
  solve_with_hook(identity, Ss, Ms, P2).

%% Parser
input([Ss, Ms]) --> stacks(Ss), "\n\n", movements(Ms).

stacks(Ss) -->
  stack_lines(Ss0),
    { transpose(Ss0, Ss1)
    , maplist(reverse, Ss1, Ss2)
    , maplist(flatten, Ss2, Ss)
    },
  "\n", string_without("\n", _).

stack_lines(L) --> sequence1(stack_line, "\n", L).
stack_line(L) --> sequence1(stack, " ", L).

stack([C]) --> "[",[C0],"]", { char_type(C0, upper), char_code(C, C0) }.
stack([]) --> "   ".

movements(L) --> sequence1(movement, "\n", L).
movement([A, F, T]) --> "move ", integer(A), " from ", integer(F), " to ", integer(T).

%% Output
:- initialization(aoc_utils:run, main).
output(P1, P2) :- output_strings(P1, P2).
