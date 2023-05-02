import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int N = sc.nextInt();
        final int K = sc.nextInt();
        final int[] x = new int[N];
        for (int i = 0; i < N; i++) {
            x[i] = sc.nextInt();
        }
        System.out.println("N: " + N);
        System.out.println("K: " + K);

        for (int i = 0; i < N; i++) {
            System.out.print(x[i] + " ");
        }
        System.out.println();
    }
}
