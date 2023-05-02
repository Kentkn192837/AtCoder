import java.util.Scanner;

class Distance {
    final int distance;

    Distance(final int distance) {
        if (distance < 0) {
            throw new IllegalArgumentException("距離が0以上ではありません。");
        }
        this.distance = distance;
    }


    void showDistance() {
        System.out.println(this.distance);
    }

    Distance add(final Distance otherDistance) {
        final int amount = this.distance + otherDistance.distance;
        return new Distance(amount);
    }
}

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

        Distance a = new Distance(8);
        Distance b = new Distance(5);
        Distance newdist = a.add(b);
        newdist.showDistance();
    }
}
