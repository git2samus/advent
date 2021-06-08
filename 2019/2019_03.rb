require 'set'

def plot_coord(steps)
  Enumerator.new { |enum|
    position = [0, 0]
    steps.each { |step|
      direction, distance = step[0], step[1..].to_i

      breadcrumb = nil
      (1..distance).each { |delta|
        breadcrumb = position.clone

        case direction
        when "D"
          breadcrumb[1] -= delta
        when "U"
          breadcrumb[1] += delta
        when "L"
          breadcrumb[0] -= delta
        when "R"
          breadcrumb[0] += delta
        end

        enum << breadcrumb
      }

      position = breadcrumb
    }
  }
end

# transform step instructions into list of coordinates
wire1, wire2 = ARGF.each_line.map { |line|
  plot_coord(line.split(","))
}

# get list of intersecting points
intersections = wire1.to_set & wire2

# calculate minimum distance
puts intersections.map { |coord|
  coord[0].abs + coord[1].abs
}.min
