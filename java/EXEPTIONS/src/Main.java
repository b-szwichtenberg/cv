import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String input;
         int i = 0;
         int j=0;
        boolean a = false;
        System.out.println("Enter first int value:");
        while(!a) {
            try {
                input = sc.next();
                i = Integer.parseInt(input);
                System.out.println("You entered: " + i);
                a = true;
            } catch (NumberFormatException e) {
                a = false;
                System.out.println("YOU DID NOT ENTER AN INT VALUE!");
            }
        }
        System.out.println("Enter second int value:");
        a = false;
        while(!a) {
            try {
                input = sc.next();
                j = Integer.parseInt(input);
                System.out.println("You entered: " + j);
                a = true;
            } catch (NumberFormatException e) {
                a = false;
                System.out.println("YOU DID NOT ENTER AN INT VALUE!");
            }
        }
        try{
            System.out.println(i/j);
        }
        catch (ArithmeticException e){
            System.out.println("YOU CANNOT DIVIDE BY ZERO");
        }
        finally {
            sc.close();
        }
    }
}
