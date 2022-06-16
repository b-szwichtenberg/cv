import java.util.LinkedList;
import java.util.Scanner;
import java.util.HashSet;

public class maaain {
        public static void main(String[] args){
            HashSet<String> food = new HashSet<String>();
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
                        b = input.next();
                        food.remove(b);
                        break;
                    case "print":
                        System.out.println(food);
                }
                System.out.println("Choose:put,take,print,exit");
                a = input.next();
            }
        }
}
