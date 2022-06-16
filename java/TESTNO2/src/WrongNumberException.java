public class WrongNumberException extends Exception {
    String s;
    WrongNumberException(String s){
        this.s = s;
    }
    public String getMessage(){
        return s;
    }
}
