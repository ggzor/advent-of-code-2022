#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

#include <fmt/core.h>
#include <range/v3/action.hpp>
#include <range/v3/numeric.hpp>

int main(int argc, char **argv) {
  if (argc != 2)
    return 1;
  std::ifstream input{argv[1]};
  if (input.fail())
    return 1;

  std::vector<uint32_t> sums{0, 0, 0};
  const auto push = [&](auto x) {
    pop_heap(begin(sums), end(sums), std::greater());
    sums.back() = std::max(sums.back(), x);
    push_heap(begin(sums), end(sums), std::greater());
  };

  uint32_t currentSum = 0;
  std::string s;
  while (getline(input, s)) {
    if (s.empty()) {
      push(currentSum);
      currentSum = 0;
    } else {
      currentSum += stoi(s);
    }
  }
  push(currentSum);

  fmt::print("Part 1: {:d}\n", ranges::max(sums));
  fmt::print("Part 2: {:d}\n", ranges::accumulate(sums, 0));
}
