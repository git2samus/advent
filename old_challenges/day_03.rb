#!/usr/bin/env ruby

File.open(ARGV[0]) {|f|
  puts f.each_line.map {|line|
    line.split.map {|n|
      Integer(n)
    }.sort
  }.map {|sides|
    (sides[0] + sides[1] > sides[2])? 1 : 0
  }.reduce :+
}
