{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/22.11";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        languages = [
          ./languages/python.nix
          ./languages/prolog.nix
          ./languages/cpp.nix
        ];

        pkgs = nixpkgs.legacyPackages.${system};
        allPackages = map (path: pkgs.callPackage path {}) languages;

        mergePackagesAndHook = p1: p2: {
          packages = p1.packages or [] ++  p2.packages or [];
          shellHook = p1.shellHook or "" + "\n" +  p2.shellHook or "";
        };
        mergeMkShellParams = builtins.foldl' mergePackagesAndHook {} allPackages;
      in {
        devShell = pkgs.mkShell mergeMkShellParams;
      }
    );
}
