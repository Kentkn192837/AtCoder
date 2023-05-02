import java.util.Scanner;

class Distance {
    final int distance;

    Distance(final int distance) {
        if (distance < 0) {
            throw new IllegalArgumentException("距離が0以上ではありません。");
        }
        this.distance = distance;
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

        Distance result = new Distance(0);
        for (int i = 0; i < N; i++) {
            Distance a = new Distance(2 * x[i]);
            Distance b = new Distance(2 * (K - x[i]));
            final int minimumDistance = Math.min(a.distance, b.distance);
            Distance addedDistance = new Distance(minimumDistance);
            result = result.add(addedDistance);
        }

        System.out.println(result.distance);
    }
}
