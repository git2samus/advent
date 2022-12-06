defmodule Main do
  def parse_line(line) do
    String.split(line, ",")
    |> Enum.map(&String.split(&1, "-"))
    |> Enum.map(fn
      items -> Enum.map(items, &String.to_integer/1)
    end)
  end

  def check_overlap([[l1, r1], [l2, r2]]) do
    (l1 <= l2 and l2 <= r1) or (l1 <= r2 and r2 <= r1)
    or
    (l2 <= l1 and l1 <= r2) or (l2 <= r1 and r1 <= r2)
  end
end

Utils.get_input
|> Stream.map(&Main.parse_line/1)
|> Stream.filter(&Main.check_overlap/1)
|> Enum.count
|> IO.inspect
