import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class PythonRunner {

    public static void main(String[] args) throws IOException {
        String style=args[1];

        String name=args[3];

        Scanner scanner=new Scanner(new FileReader("Q2/inputs/"+name));
        String str=scanner.nextLine();
        scanner.close();

        Runtime.getRuntime().exec("python Q2\name_transform.py -s "+ style + " -v " + str);
    }
}
