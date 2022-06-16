import java.util.LinkedList;
import java.util.Scanner;

public class main {
    public static void main(String[] args){
        LinkedList<String> food = new LinkedList<String>();
        Scanner input = new Scanner(System.in);
        System.out.println("Choose:put,take,print,exit");
        String a = input.next();
        while(!a.equals("exit")){
            switch(a){
                case "put":
                    String b = input.next();
                    food.add(b);
                    break;
                case "take":
                    food.removeFirst();
                    break;
                    case "print":
                        System.out.println(food);
            }
            System.out.println("Choose:put,take,print,exit");
            a = input.next();
        }

    }
}
