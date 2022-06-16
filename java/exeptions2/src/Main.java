import java.io.FileWriter;
import java.io.IOException;
import java.util.*;
public class Main {
public static void main(String[] args) {
    //try{
      //  FileWriter fw = new FileWriter("text.txt");
        //        fw.write("HELLO");
        //fw.close();
    //}
    //catch(IOException e){
      //  System.out.println(e.getMessage());
    //}
    Scanner sc = new Scanner(System.in);
    int input;
    System.out.print("How tall are you (in cm)?: ");
    try{
        input = sc.nextInt();
        if(input < 0){
            throw new MyException("Not valid hights");
        }
        else{
            System.out.print("You entered: " + input);
        }

    }
    catch(MyException e){
        System.out.println(e.getMessage());
    }
    catch(InputMismatchException e){
        System.out.println("WHAT");
    }
    System.out.println("How old are you?");
    try{
        input = sc.nextInt();
        if(input < 18){
            throw new TooYoung("TOO YOUNG MY BOY");
        }
        else{
            System.out.print("You entered: " + input);
        }

    }
    catch(TooYoung e){
        System.out.println(e.getMessage());
    }
    sc.close();
}
}
