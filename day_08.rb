#!/usr/bin/env ruby

def pp(display)
  puts '  ' + '1234567890'*5
  for offset in 0..($display_height-1)
    puts "#{offset+1} " + display[offset*$display_width..(offset+1)*$display_width-1].map { |px|
      px ? '#' : '.'
    }.join
  end
  puts
end

$display_width, $display_height = 50, 6

File.open(ARGV[0]) { |f|
  display = Array.new($display_width * $display_height, false)

  f.each_line { |line|
    case
    when line.start_with?('rect')
      width, height = /rect (\d+)x(\d+)/.match(line).captures.map { |n| Integer(n) }

      for offset in 0..(height-1)
        display.fill(true, offset*$display_width, width)
      end
    when line.start_with?('rotate row')
      row_y, by = /rotate row y=(\d+) by (\d+)/.match(line).captures.map { |n| Integer(n) }

      row = display[$display_width*row_y, $display_width].rotate(-by)
      display[$display_width*row_y, $display_width] = row
    when line.start_with?('rotate column')
      col_x, by = /rotate column x=(\d+) by (\d+)/.match(line).captures.map { |n| Integer(n) }

      col = (col_x...display.length).step($display_width).map { |n| display[n] }.rotate(-by)
      (col_x...display.length).step($display_width).each_with_index { |n, i| display[n] = col[i] }
    end

    puts line
    pp(display)
  }

  puts "lit #{display.count { |px| px }} pixels"
}
