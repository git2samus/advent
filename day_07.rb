#!/usr/bin/env ruby

def has_abba?(node)
  node.split('')[0..-4].each_with_index { |char, index|
    return true if [
      node[index] != node[index+1], node[index] == node[index+3], node[index+1] == node[index+2],
    ].all?
  }
  false
end

File.open(ARGV[0]) { |f|
  puts f.each_line.select { |line|
    nodes = line.split(/\[\w+\]/)
    hypernet = line.scan(/\[\w+\]/).map { |node| node[1..-2] }

    nodes.any? { |node| has_abba?(node) } and not hypernet.any? { |node| has_abba?(node) }
  }.count
}
