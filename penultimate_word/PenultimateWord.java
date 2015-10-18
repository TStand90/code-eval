import java.io.*;

public class PenultimateWord {
    public static void main(String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;

        while ((line = buffer.readLine()) != null) {
            String words[] = line.trim().split("\\s+");

            System.out.println(words[words.length - 2]);
        }
    }
}