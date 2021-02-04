object Solution {
  private def isPrime(x: Int): Boolean = {
    !Range(2, x - 1).exists(x % _ == 0)
  }

  def solution(input: Int): String = {
    LazyList.from(2)
      .filter(isPrime)
      .take(input + 5)
      .mkString("")
      .substring(input, input + 5)
  }
}
