import java.io.File

fun main(args: Array<String>) {

    var input = args[0];

    var data: String = File("Q1/inputs/$input").readLines()[1]

    val result = data.split(" ").map { it.toLong() }

    println("Using Binary Sort")

    TreeSort(result)
}