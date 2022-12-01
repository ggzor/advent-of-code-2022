{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/22.05";
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
          python-with-packages = pkgs.python310.withPackages pythonPackages;
      in {
        devShell = pkgs.mkShell {
          packages = [
            python-with-packages
          ];
        };
      }
    );
}
