#!/usr/bin/env ruby

File.open(ARGV[0]) {|f|
  keypad = [[1,2,3], [4,5,6], [7,8,9]]
  x, y = 1, 1
  combination = ''

  f.each_line {|line|
    line.split('').each {|char|
      case char
      when 'U'
        y = [0, y-1].max
      when 'D'
        y = [2, y+1].min
      when 'L'
        x = [x-1, 0].max
      when 'R'
        x = [x+1, 2].min
      end
    }

    combination += String(keypad[y][x])
  }

  puts combination
}
