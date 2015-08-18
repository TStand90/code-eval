import java.io.*;

public class FizzBuzz {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;

        while ((line = buffer.readLine()) != null) {
            line = line.trim();

            String[] inputs = line.split(" ");
            int fizz = Integer.parseInt(inputs[0]);
            int buzz = Integer.parseInt(inputs[1]);
            int count = Integer.parseInt(inputs[2]);

            String fizzbuzz_output = "";

            for (int i = 1; i <= count; i++) {
                if (i % fizz == 0 && i % buzz == 0) {
                    fizzbuzz_output += "FB ";
                }
                else if (i % fizz == 0) {
                    fizzbuzz_output += "F ";
                }
                else if (i % buzz == 0) {
                    fizzbuzz_output += "B ";
                }
                else {
                    fizzbuzz_output += i + " ";
                }
            }

            System.out.println(fizzbuzz_output.trim());
        }
    }
}
