import java.io.*;

public class SumOfDigits {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;

        while ((line = buffer.readLine()) != null) {
            int sum = 0;

            char[] inputs = line.toCharArray();

            for (int i = 0; i < inputs.length; i++) {
                sum += Character.getNumericValue(inputs[i]);
            }

            System.out.println(sum);
        } 
    }
}

