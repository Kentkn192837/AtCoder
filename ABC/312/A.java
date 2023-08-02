import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> strArg = new ArrayList<String>(){
            {
                add("ACE");
                add("BDF");
                add("CEG");
                add("DFA");
                add("EGB");
                add("FAC");
                add("GBD");
            }
        };

        String S = sc.next();
        for (String msg : strArg) {
            if (msg.equals(S)) {
                System.out.println("Yes");
                return;
            }
        }
        System.out.println("No");
    }
}
