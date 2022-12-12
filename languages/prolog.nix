{ fetchFromGitHub, swiProlog }:
let
  func = fetchFromGitHub {
    owner = "mndrix";
    repo = "func";
    rev = "v0.4.2";
    sha256 = "0mkl31zvv2nrnkadq7fgv1wkdv4jmndd7603ajsf841dhw142vzf";
  };
  function_expansion = fetchFromGitHub {
    owner = "mndrix";
    repo = "function_expansion";
    rev = "0.1.2";
    sha256 = "0ah628gzi49fw428h0pnaah78gkd3hgrrwc23fpnjgmnl7yxviwp";
  };
  list_util = fetchFromGitHub {
    owner = "mndrix";
    repo = "list_util";
    rev = "v0.13.0";
    sha256 = "0lx7vffflak0y8l8vg8k0g8qddwwn23ksbz02hi3f8rbarh1n89q";
  };

  aoc_utils = ../utils;

  swiplWithPacks = swiProlog.override {
    extraPacks = map (dep-path: "'file://${dep-path}'") [
      func
      list_util
      function_expansion
      aoc_utils
    ];
  };
in {
  packages = [ swiplWithPacks ];
}
