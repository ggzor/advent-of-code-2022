args@{
  cmake
, clang_14
, fmt_9
, range-v3
}: {
  packages = builtins.attrValues args;
  shellHook = ''
    export CC=clang
    export CXX=clang++
  '';
}
