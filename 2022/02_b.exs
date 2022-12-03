defmodule Main do
  @op_rock     "A"
  @op_paper    "B"
  @op_scissors "C"

  @pl_rock     "X"
  @pl_paper    "Y"
  @pl_scissors "Z"

  @res_lose    "X"
  @res_draw    "Y"
  @res_win     "Z"

  @sc_lose 0
  @sc_draw 3
  @sc_win  6

  def self_score(@pl_rock),     do: 1
  def self_score(@pl_paper),    do: 2
  def self_score(@pl_scissors), do: 3

  def match_score(@op_rock, @pl_rock),         do: @sc_draw
  def match_score(@op_rock, @pl_paper),        do: @sc_win
  def match_score(@op_rock, @pl_scissors),     do: @sc_lose
  def match_score(@op_paper, @pl_rock),        do: @sc_lose
  def match_score(@op_paper, @pl_paper),       do: @sc_draw
  def match_score(@op_paper, @pl_scissors),    do: @sc_win
  def match_score(@op_scissors, @pl_rock),     do: @sc_win
  def match_score(@op_scissors, @pl_paper),    do: @sc_lose
  def match_score(@op_scissors, @pl_scissors), do: @sc_draw

  def result_to_self(@op_rock, @res_lose),     do: @pl_scissors
  def result_to_self(@op_rock, @res_draw),     do: @pl_rock
  def result_to_self(@op_rock, @res_win),      do: @pl_paper
  def result_to_self(@op_paper, @res_lose),    do: @pl_rock
  def result_to_self(@op_paper, @res_draw),    do: @pl_paper
  def result_to_self(@op_paper, @res_win),     do: @pl_scissors
  def result_to_self(@op_scissors, @res_lose), do: @pl_paper
  def result_to_self(@op_scissors, @res_draw), do: @pl_scissors
  def result_to_self(@op_scissors, @res_win),  do: @pl_rock

  def calc_score([opponent, result]) do
    self = result_to_self(opponent, result)
    match_score(opponent, self) + self_score(self)
  end
end

Utils.get_input_tokens
|> Stream.map(&Main.calc_score/1)
|> Enum.sum
|> IO.inspect
