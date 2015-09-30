import java.io.*;

public class Lowercase {
    public static void main(String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;

        while ((line = buffer.readLine()) != null) {
            System.out.println(line.trim().toLowerCase());
        }
    }
}