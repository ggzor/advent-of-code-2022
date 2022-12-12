{ python310 }:
let
  pythonPackages = pkgs: with pkgs; [
    more-itertools
    numpy

    # Development
    black
    pynvim
    rope
  ];
  pythonWithPackages = python310.withPackages pythonPackages;
in {
  packages = [ pythonWithPackages ];
}
