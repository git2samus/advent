#!/usr/bin/env ruby

File.open(ARGV[0]) { |f|
  counts = nil

  f.each_line.map { |line|
    counts = Array.new(line.length).map { |a| Hash.new(0) } if counts.nil?

    counts.each_with_index { |count, index|
      count[line[index]] += 1
    }
  }

  puts counts.map { |count|
    count.max { |a, b|
      a[1] <=> b[1]
    }[0]
  }.join
}
