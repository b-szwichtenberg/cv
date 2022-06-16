import java.util.Scanner;

public class LodowkaApp {
    public static void main(String[] args) {
     System.out.println("Wybierz:dodaj,wez,wyswietl,zamknij");
     Scanner input = new Scanner(System.in);
     String s=input.next();

     while (!s.equals("zamknij")){

         switch(s){
             case "dodaj":
                 System.out.println("Podaj nazwe jedzenia:");
                 String a=input.next();
                 System.out.println("Podaj ilosc:");
                 String b=input.next();
                 Lodowka.dodaj(a,Integer.parseInt(b));
                 break;
             case "wez":
                 System.out.println("Podaj nazwe do usuniecia:");
                 a=input.next();
                 System.out.println("Podaj ilosc:");
                 b=input.next();
                 System.out.println(Lodowka.wez(a,Integer.parseInt(b)));
                 break;
             case "wyswietl":
                 Lodowka.wyswietl();
                 break;
         }
         System.out.println("Wybierz:dodaj,wez,wyswietl,zamknij");
         s=input.next();
     }

    }
}

