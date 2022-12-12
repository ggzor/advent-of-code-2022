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
    # Prepare compile_commands.json
    if ! ( mkdir -p build && cd build && cmake ..; ); then
      echo "Unable to generate compile_commands.json"
    fi
  '';
}
