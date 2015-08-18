import java.util.ArrayList;

public class SumOfPrimes {
    public static void main (String[] args) {
        int sum = 0;
        int numberOfPrimes = 0;
        int iterator = 2;

        while (numberOfPrimes < 1000) {
            if (isPrime(iterator)) {
                sum += iterator;
                numberOfPrimes += 1;
            }
            iterator++;
        }

        System.out.println(sum);
    }

    private static boolean isPrime (int number) {
        if (number == 0 || number == 1) {
            return false;
        }
        else if (number == 2) {
            return true;
        }
        else {
            for (int i = 2; i < number; i++) {
                if (number % i == 0) {
                    return false;
                }
            }
        }

        return true;
    }
}
