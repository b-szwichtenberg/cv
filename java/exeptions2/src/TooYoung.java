public class TooYoung extends  Exception{
    String s;
    TooYoung(String s){
        this.s=s;
    }
    public String getMessage(){
        return s;
    }
}
