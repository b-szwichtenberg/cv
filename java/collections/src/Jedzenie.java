public class Jedzenie {
    public String nazwa;
    public int ilosc;
    Jedzenie(String foodname,int amount){
        nazwa=foodname;
        ilosc=amount;
    }
    public String getTitle(){
        return nazwa;
    }
    public int getAmount(){
        return ilosc;
    }
}
