def solution(n: Int): String = {
  def isPrime(x: Int): Boolean = {
    val limit = Math.sqrt(x).toInt
    !(2 to limit).exists(x % _ == 0)
  }

  def generatePrimes(target: Int, current: Int = 2, soFar: String = ""): String = {
    if (target > soFar.length){
      val updated = if(isPrime(current)){ soFar + current } else { soFar }
      generatePrimes(target, current + 1, updated)
    } else {
      soFar
    }
  }

  generatePrimes(n + 5).slice(n, n + 5)
}


