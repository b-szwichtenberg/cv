import java.util.ArrayList;
public class Lodowka {
    static ArrayList<Jedzenie> Jedz = new ArrayList<>();
    public static void dodaj(String nazwa,int ilosc){
        Jedzenie noweJedzenie = new Jedzenie(nazwa,ilosc);
        Jedz.add(noweJedzenie);
    }
    public static String wez(String nazwa,int ilosc){
        String message = "Nie ma takiego jedzenia";
        for(int i=0;i<Jedz.size();i++){
            if(Jedz.get(i).getTitle().equals(nazwa)){
                message = "Jedzenie zostało usunięte!";
                if(Jedz.get(i).getAmount() > ilosc){
                    int a = Jedz.get(i).getAmount() - ilosc;
                    Jedzenie noweJedzenie = new Jedzenie(nazwa,a);
                    Jedz.set(i,noweJedzenie);
                }else{
                    Jedz.remove(i);
                }
                break;
            }
        }
        return message;
    }
    public static void wyswietl(){
        for(int i=0;i<Jedz.size();i++){
            System.out.println(Jedz.get(i).getTitle()+"("+Jedz.get(i).getAmount()+")");
        }
    }
}
