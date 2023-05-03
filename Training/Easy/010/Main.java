import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

class Score {
    final int score;

    Score(final int score) {
        if (score < 0) {
            throw new IllegalArgumentException("スコアが負です。");
        }
        this.score = score;
    }

    Score add(final Score otherScore) {
        final int addedScore = this.score + otherScore.score;
        return new Score(addedScore);
    }
}


class Main {
    public static void main(String[] args) {
        final Scanner sc = new Scanner(System.in);
        final int N = sc.nextInt();
        final ArrayList<Integer> a = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            a.add(sc.nextInt());
        }
        sc.close();

        Collections.sort(a, Collections.reverseOrder());

        Score alice = new Score(0);
        Score bob = new Score(0);
        for (int i = 0; i < a.size(); i++) {
            final Score getScore = new Score(a.get(i));
            if (i % 2 == 0) {
                alice = alice.add(getScore);
                continue;
            }
            bob = bob.add(getScore);
        }
        
        final int result = Math.abs(alice.score - bob.score);
        System.out.println(result);
    }
}
