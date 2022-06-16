import java.util.Scanner;
import java.util.Stack;

public class MAIN {
    public static void main(String[] args){
        Stack<String> stack = new Stack<String>();
        Scanner input = new Scanner(System.in);
        System.out.println("Choose:put,take,print,exit.");
        String a= input.next();
        while(!a.equals("exit")){
            switch (a) {
                case "put":
                    System.out.println("Add item to bag:");
                    String b= input.next();
                    stack.push(b);
                    System.out.println("Successfully added an item.");
                    break;
                case "take":
                    stack.pop();
                    System.out.println("Successfully removed an item.");
                    break;
                case "print":
                    System.out.println(stack);
                    break;
            }
            System.out.println("Choose:put,take,print,exit.");
            a= input.next();
        }
    }
}
