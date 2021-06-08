#!/usr/bin/env ruby

puts ARGF.each_line.map { |line| line.to_i / 3 - 2 }.sum
