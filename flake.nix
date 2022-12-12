{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/22.11";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};
          pythonPackages = pkgs: with pkgs; [
            more-itertools
            numpy

            # Development
            black
            pynvim
            rope
          ];
          pythonWithPackages = pkgs.python310.withPackages pythonPackages;
      in {
        devShell = pkgs.mkShell {
          packages = with pkgs; [
            pythonWithPackages
            swiProlog
            # C++
            llvmPackages_14.clang
            cmake
            fmt_9
            range-v3
          ];
          shellHook = ''
            export CC=clang
            export CXX=clang++
          '';
        };
      }
    );
}
