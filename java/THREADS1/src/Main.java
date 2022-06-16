import java.sql.Array;

public class Main {
    public static void main(String[] args){
        Integer[] arr = new Integer[]{3,4,5,3,2,5,7,4,8,6};
        MinThread mn = new MinThread(arr);
        mn.start();
        MaxThread mx = new MaxThread(arr);
        mx.start();
    }
}
