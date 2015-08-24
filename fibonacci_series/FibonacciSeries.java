import java.io.*;

public class FibonacciSeries {
    public static void main(String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;

        while ((line = buffer.readLine()) != null) {
            line = line.trim();

            int fibo = Integer.parseInt(line);

            System.out.println(fibonacci(fibo));
        }
    }

    private static int fibonacci(int number) {
        if (number == 1 || number == 2) {
            return 1;
        } else if (number == 0) {
            return 0;
        } else {
            return fibonacci(number - 2) + fibonacci(number - 1);
        }
    }
}
