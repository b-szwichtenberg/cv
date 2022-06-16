import java.util.Random;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number of items: ");
        int input = sc.nextInt();
        int[] arr = new int[input];
        Random rand = new Random();
        for (int i = 0; i < input;i++){
            arr[i] = rand.nextInt(100);
        }
        MyThread mt = new MyThread(arr);
        mt.start();
    }
}






